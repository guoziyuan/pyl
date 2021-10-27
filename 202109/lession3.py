'''
进程间通信
quene 、pipes
'''

from multiprocessing import process, Queue
from multiprocessing.context import Process
import os
import time
import random

# 生产者
def write_proc(quene):
    print("write data :%s" % (str(os.getpid())))
    for word in ["a", "b", "c", "d"]:
        quene.put(word)
        print("put :" + word)
        time.sleep(random.random() * 2)
# 消费者
def read_proc(quene):
    print("read data: %s" % str(os.getpid()))
    while True:
        word = quene.get(True)
        print("get:"+word)

if __name__ == "__main__":
    # 共享队列
    qu = Queue()
    # 生产者进程
    pw = Process(target=write_proc, args=(qu,))
    # 消费者进程
    pr = Process(target=read_proc, args=(qu,))
    pw.start()
    pr.start()

    # 等待生产者结束
    pw.join()
    # 强制终止消费
    pr.terminate()