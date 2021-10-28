# coding="utf-8"
"""
协程：在一个线程内，通过程序控制方法的中断与恢复，达到类似多线程的处理任务的方法
好处：1、避免线程切换开销
     2、在同一个线程内，不存在线程安全问题，不需要锁，执行速度快
实现方式：使用yield表达式来实现函数阻断与恢复
"""


# 案例生产者与消费者模型

# 消费者
def consumer():
    count = 1
    while True:
        n = yield count
        if not n:
            return
        # 消费
        print("consume No: " + str(n))
        count += 1
    print("close consumer")


# 生产者
def producer(c):
    # 激活生成器，返回第一个yield的参数 count，并赋值给count
    count = c.send(None)
    print("start NO :" + str(count))
    # 开始生产
    for i in range(1, 10):
        print("produce NO :" + str(i))
        count = c.send(i)
        print("next NO :" + str(count))
    # 生产结束，关闭消费
    c.close()
    print("close, no next NO:" + str(count))


if __name__ == "__main__":
    # 获得生成器对象
    c = consumer()
    # 生成器对象作为参数传递
    producer(c)
