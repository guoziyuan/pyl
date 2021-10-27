'''
进程：资源分配最小单元

Unix系统中，提供fock()函数，可以复制一个子进程，然后分别在父进程和子进程中返回
子进程返回0，父进程返回子进程id
'''
import os

print("pid : %s" % os.getpid())
# windows 上没有fork
pid = os.fork()
if pid == 0:
    print("子进程返回，子进程id：%s， 父进程id：%s" % (os.getpid(), os.getppid()))
else:
    print("父进程返回，子进程id：%s， 父进程id：%s" % (pid, os.getpid()))

# 有些操作系统不支持fork()，Python 提供了multiprocessing库
from multiprocessing import Process
import time
import random

def run_on_process(arg):
    time.sleep(random.random() * 3)
    print("pid : {}, ppid: {}, arg : {}".format(os.getpid(), os.getppid(), arg))

if __name__ == '__main__':
    print("当前进程id：" + str(os.getpid()))
    # 创建子进程
    p = Process(target = run_on_process, args=("test",))
    # 启动子进程
    print("start")
    p.start()

    # 等待子进程执行结束
    p.join()
    print("end")