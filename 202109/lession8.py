'''
分布式
多进程通信是通过quene来进行数据共享，分布式就是通过网络把quene共享出去，实现不同机器上进程之间的通信
master
'''

import os, random, time, queue
# 分布式管理模块
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()

# 接受结果队列
result_queue = queue.Queue()

class QueueManager(BaseManager):
    pass

def get_task_q():
    return task_queue
def get_result_q():
    return result_queue

if __name__ == "__main__":
    # 把queue注册到网络中
    QueueManager.register("get_task_queue", callable=get_task_q)
    QueueManager.register("get_result_queue", callable=get_result_q)

    # 配置端口，验证码
    manager = QueueManager(address=("", 5000), authkey=b'abc')
    # 启动
    manager.start()
    # 通过网络访问queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # 放入任务
    for i in range(100):
        n = random.randint(0, 100)
        task.put(n)
        print("master put task " + str(n))

    # 获取结果
    for i in range(10):
        k = result.get(timeout=10)
        print("manager get result :" + str(k))

    # 关闭
    manager.shutdown()
    print("manager exit")
