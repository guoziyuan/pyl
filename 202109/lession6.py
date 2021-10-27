'''
任何时间都只能有一个线程获得锁对象

'''

import time, random
import threading
balance = 0

#获得锁对象
lock = threading.Lock()

def change_id(n):
    # 声明为global
    global balance
    balance += n
    # 增加出错可能
    time.sleep(1)
    balance -= n
    print("%s操作账户后存款为%s" % (threading.current_thread().name, balance))
  
    

def run_thread():
    for i in range(10):
        # 获得锁，才能往下执行
        lock.acquire()
        try:
            change_id(i)
        finally:
        # 释放锁
            lock.release()
        time.sleep(random.random())

# 丈夫和妻子同时去操作账户
hus = threading.Thread(target=run_thread, name="丈夫")
wife = threading.Thread(target=run_thread, name="妻子")
hus.start()
wife.start()
hus.join()
wife.join()
print("balance:" + str(balance))