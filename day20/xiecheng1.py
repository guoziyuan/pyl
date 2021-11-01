# coding="utf-8"

"""
协程理解：微线程，在一个线程内，多个任务存在io操作，可以在一些任务io操作时，
        执行其它任务，从而充分利用cpu资源，达到任务并行的减少cpu空等的目的

协程本质：一个线程内，方法间协调调用

Python中 协程是通过生成器实现 yield
"""
import time


# 定义一个生成器函数
def consumer():
    print("start consumer:")
    while True:
        result = yield
        if not result:
            return
        print('消费 ： ' + str(result))
    print("close consumer")


# 定义一个在一定时间调用生成器的函数
def producer(c):
    print("init consumer")
    # 最开始生成器没有待赋值对象，需要发送空值激活生成器
    c.send(None)
    print("start producer")
    # 生产10件物品，每生产1件，需要1s时间做一些其他操作，cpu空闲
    for i in range(1, 11):
        # 向生成器函数发送数据，生成器函数激活
        print("生产：" + str(i))
        c.send(i)
        time.sleep(1)
    # 告诉生成器函数，执行完了
    c.close()


if __name__ == "__main__":
    # 生成器函数初始化，得到生成器函数对象
    c = consumer()

    # 生成器函数对象作为参数，可以控制生成器运行
    producer(c)
