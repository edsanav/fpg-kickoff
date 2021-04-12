import random

from aiohttp import web


async def handle(request):
    if random.choice([True, False]):
        return web.json_response(data={"status":"GREAT!"}, status=200)
    else:
        raise Exception("BOOO")

app = web.Application()
app.router.add_route('GET', '/random', handle)

web.run_app(app)