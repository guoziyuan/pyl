# coding="utf-8"

"""
https://github.com/python-greenlet/greenlet/blob/adca19bf1f287b3395896a8f41f3f4fd1797fdc7/src/greenlet/tests/test_generator.py#L1
greenlet是一个用C实现的协程模块，
相比与python自带的yield，它可以使你在任意函数之间随意切换，而不需把这个函数先声明为generator
"""

from greenlet import greenlet
import time
import random


def task1():
    print("start task1")
    for i in range(10):
        print("task1 :" + str(i))
        t2.switch()
        # 执行一次需要休息一段时间
        time.sleep(random.randrange(1, 5))


def task2():
    print("start task2")
    for i in range(10):
        print("task2 :" + str(i))
        t3.switch()
        # 执行一次需要休息一段时间
        time.sleep(random.randrange(1, 5))


def task3():
    print("start task3")
    for i in range(10):
        print("task3 :" + str(i))
        t1.switch()
        # 执行一次需要休息一段时间
        time.sleep(random.randrange(1, 5))


if __name__ == "__main__":
    t1 = greenlet(task1)
    t2 = greenlet(task2)
    t3 = greenlet(task3)
    t1.switch()
