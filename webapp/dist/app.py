# coding="utf-8"

import logging;

logging.basicConfig(level=logging.INFO)
from aiohttp import web
import asyncio, os, json, time
from datetime import datetime

host = "127.0.0.1"
port = 9000


def index(request):
    return web.Response(b'<h1>welcome</h1>')


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route("GET", "/", index)
    app_runner = web.AppRunner(app)
    srv = await loop.create_server(app_runner.app.make_handler(), host, port)
    logging.info("server start at {}:{}".format(host, port))
    return srv

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # 运行协程，直到完成
    loop.run_until_complete(init(loop))
    # 运行协程，直到调用 stop()
    loop.run_forever()