import ujson as json
from aiohttp import web
from asyncio import Queue

work_queue = Queue()
jobcount = 0
responses = {}


async def submit_job_request(request):
    global jobcount
    jobid = jobcount
    jobcount += 1
    data = await request.json()
    responses[jobid] = Queue()
    await work_queue.put(json.dumps({"jobid": jobid, "data": data}))
    result = await responses[jobid].get()
    return web.Response(text=result)


async def get_work(request):
    data = await work_queue.get()
    return web.Response(text=data)


async def work_done(request):
    data = await request.json()
    await responses[data["jobid"]].put(json.dumps(data))
    return web.Response(text="ok")


app = web.Application()
app.add_routes(
    [
        web.post("/submit", submit_job_request),
        web.get("/work", get_work),
        web.post("/work", work_done),
    ]
)
