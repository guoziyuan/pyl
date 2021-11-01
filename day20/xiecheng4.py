# coding="utf-8"

"""
协程gevent与猴子补丁
前面gevent 在休眠的时候，各个函数中都是使用gevent的sleep
如果我们使用time.sleep，可以使用猴子补丁达到同样效果
"""

from gevent import monkey
import time, random
import gevent

# 需要放在所有函数面, 运行时会将注册的函数中的time.sleep()替换成gevent.sleep()
monkey.patch_all()


def task1():
    print("start task1")
    for i in range(10):
        print("task1 :" + str(i))
        # 执行一次需要休息一段时间
        time.sleep(random.randrange(1, 5))


def task2():
    print("start task2")
    for i in range(10):
        print("task2 :" + str(i))
        # 执行一次需要休息一段时间
        time.sleep(random.randrange(1, 5))


def task3():
    print("start task3")
    for i in range(10):
        print("task3 :" + str(i))
        # 执行一次需要休息一段时间
        time.sleep(random.randrange(1, 5))


if __name__ == "__main__":
    t1 = gevent.spawn(task1)
    t2 = gevent.spawn(task2)
    t3 = gevent.spawn(task3)
    gevent.joinall([t1, t2, t3])
