from functools import partial
import websockets
from aiohttp import web
import asyncio
# Dies ist ein Kommentar. Überrascht?

loop = asyncio.get_event_loop()  # Eine AbstractEventLoop
app = web.Application(loop=loop)  # web.Application

router = app.router  # Setze "router" auf "app.router"
async def handle_hello(req):  # Definiere eine Coro
    return web.Response(text="Hello")  # Gib "Hello" zurück
router.add_route("GET", "/test", handle_hello)

async def stop(req):
    exit(1)
router.add_route("GET", "/close", stop)  # Erstelle Route "close"

async def fabian(req): # test
    file = open("./webapp/fabian.html", "rb").readlines()
    return web.Response(text=file, content_type="text/html")
router.add_route("GET", "/fabian", fabian) # WOOW PARTIALS!

handler = app.make_handler()  # Erstelle einen Handler
future = loop.create_server(handler, "localhost", 8080)  # EIN SERVER!

loop.create_task(future)  # Starte den Server
 
async def handle_ws(ws, path):
    async for message in ws:
        print(message)
        await ws.send("HELLO")

loop.run_until_complete(websockets.serve(handle_ws, "localhost", 8765))  # Lasse den WS-Server laufen, bis er fertig ist. *Ist er nie* ;) ;) ;)

loop.run_forever()  # Lasse die Loop für immer laufen