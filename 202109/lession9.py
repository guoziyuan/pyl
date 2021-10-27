'''
分布式 
worker
'''

from multiprocessing.queues import Queue
import queue, time, sys
from multiprocessing.managers import BaseManager

# 管理器对象
class Manager(BaseManager):
    pass

if __name__=="__main__":
    # 注册
    Manager.register("get_task_queue")
    Manager.register("get_result_queue")

    # 服务器地址
    sever_addr = "127.0.0.1"
    m = Manager(address=(sever_addr, 5000), authkey=b'abc')

    # 连接
    m.connect()

    #获取taskqueue对象
    task  = m.get_task_queue()
    result = m.get_result_queue()

    # 从任务队列中取任务，并把结果放到结果队列中
    for i in range(10):
        try:
            k = task.get(timeout = 1)
            print("run task %s * %s" % (k, k))
            r = '%d * %d = %d' % (k, k, k*k)
            result.put(r)
            time.sleep(1)
        except queue.Empty :
            print('task queue is empty.')

    print("work exit")