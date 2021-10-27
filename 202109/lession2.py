'''
进程池

'''

from multiprocessing import Pool, pool
import random
import os
import time

def sub_fun(test):
    print("%s start" % (test))
    t1 = time.time()
    time.sleep(random.random() * 5)
    t2 = time.time()
    print("%s cost %s" % (test, t2-t1))

if __name__ == "__main__" :
    print("process id : " + str(os.getpid()))
    mypool = Pool(4)
    # 创建多个进程
    for i in range(1, 7):
        mypool.apply_async(sub_fun, (i,))

    # 关闭进程池
    mypool.close()
    # 等待进程结束
    mypool.join()
    print("all process done")