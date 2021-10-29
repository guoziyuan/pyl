# coding="utf-8"
#
# import logging;
#
# logging.basicConfig(level=logging.INFO)
# from aiohttp import web
# import asyncio, os, json, time
# from datetime import datetime
#
# host = "127.0.0.1"
# port = 9000
#
#
# def index(request):
#     return web.Response(b'<h1>welcome</h1>')
#
#
# # https://docs.aiohttp.org/en/stable/web_advanced.html#aiohttp-web-app-runners
# async def init():
#     app = web.Application()
#     app.router.add_get("/", index)
#     runner = web.AppRunner(app)
#     await runner.setup()
#     site = web.TCPSite(runner, host, port)
#     srv = await site.start()
#     logging.info("server start at {}:{}".format(host, port))
#     return srv
#
#
# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     # 运行协程，直到完成
#     loop.run_until_complete(init())
#     # 运行协程，直到调用 stop()
#     loop.run_forever()
#
#
'''
async web application.
'''

import logging;

logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web


def index(request):
    return web.Response(body=b'<h1>Awesome</h1>')


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv


# loop = asyncio.get_event_loop()
# loop.run_until_complete(init(loop))
# loop.run_forever()
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # 运行协程，直到完成
    loop.run_until_complete(init(loop))
    # 运行协程，直到调用 stop()
    loop.run_forever()
