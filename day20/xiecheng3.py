# coding="utf-8"

"""
greenlet 能够实现一个线程内方法切换，但是都需要程序指定调用时机，很麻烦

通过gevent可以较轻松实现并发同步或异步编程
"""

import gevent
import time
import random


def task1():
    print("start task1")
    for i in range(10):
        print("task1 :" + str(i))
        # 执行一次需要休息一段时间
        gevent.sleep(random.randrange(1, 5))


def task2():
    print("start task2")
    for i in range(10):
        print("task2 :" + str(i))
        # 执行一次需要休息一段时间
        gevent.sleep(random.randrange(1, 5))


def task3():
    print("start task3")
    for i in range(10):
        print("task3 :" + str(i))
        # 执行一次需要休息一段时间
        gevent.sleep(random.randrange(1, 5))


if __name__ == "__main__":
    gevent.joinall([gevent.spawn(task1), gevent.spawn(task2), gevent.spawn(task3)])
