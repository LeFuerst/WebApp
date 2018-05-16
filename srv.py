from aiohttp import web
import asyncio


loop = asyncio.get_event_loop()
app = web.Application(loop=loop)
handler = app.make_handler()
future = loop.create_server(handler, "localhost", 8080)
loop.run_until_complete(future)

router = app.router

router.add_route("GET", "/test", handle_hello)

async def handle_hello(req):
    return web.Response("Hello")
