# coding="utf-8"

"""
死锁：多个线程在占用一部分资源的同时尝试获取对方已占用的资源，就会造成死锁

死锁处理办法：
1、重构代码，避免死锁逻辑
2、争抢资源时给出超时时间
lock2.acquire(timeout = 10)
"""
from threading import Thread, Lock
import time

# 定义两把锁，代表两份资源
lock1 = Lock()
lock2 = Lock()


# 线程A
class ThreadA(Thread):
    def run(self):
        if lock1.acquire():
            print("{} 获得资源{}".format("A", 1))
            # 休眠1s, 代表处理逻辑
            time.sleep(1)
            # 尝试获取资源2
            if lock2.acquire(timeout=10):
                print("{} 获得资源{}".format("A", 2))
                time.sleep(1)
                # 使用完，释放
                lock2.release()
            lock1.release()


# 线程B
class ThreadB(Thread):
    def run(self):
        if lock2.acquire():
            print("{} 获得资源{}".format("B", 2))
            # 休眠1s, 代表处理逻辑
            time.sleep(1)
            # 尝试获取资源2
            if lock1.acquire():
                print("{} 获得资源{}".format("B", 1))
                time.sleep(1)
                # 使用完，释放
                lock1.release()
            lock2.release()


if __name__ == "__main__":
    t1 = ThreadA()
    t2 = ThreadB()
    t1.start()
    t2.start()
