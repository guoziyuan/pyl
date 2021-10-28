# coding="utf-8"

"""

python3中提供的异步任务库，通过消息循环实现异步

"""

import threading
import asyncio


# asyncio
# 注意只支持3.4版本，从3.5版本开始废弃了
# @asyncio.coroutine
# def hello():
#     print("start hello ", threading.currentThread().name)
#     name = yield from asyncio.sleep(1)
#     print("end hello", threading.currentThread().name)


# 3.5版本及以后，使用 async  await
async def hello_word():
    print("start hello ", threading.currentThread().name)
    name = await asyncio.sleep(1)
    print("end hello %s, name %s" % (threading.currentThread().name, name))


async def read_file(file_name):
    print("start read_file ", threading.currentThread().name)
    with open(file_name, 'w') as f:
        for i in range(10):
            f.write(str(i))
    print("end read_file ", threading.currentThread().name)


async def wget(host):
    conn = asyncio.open_connection(host, 80)
    reader, writer = await conn
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
        # Ignore the body, close the socket
    writer.close()


if __name__ == "__main__":
    # 获得eventloop
    loop = asyncio.get_event_loop()

    # coroutine 任务队列
    task = [hello_word(), read_file("6.txt"), wget("www.sina.com.cn")]
    loop.run_until_complete(asyncio.wait(task))
    print("run ", threading.currentThread().name)
    # 关闭loop
    loop.close()
