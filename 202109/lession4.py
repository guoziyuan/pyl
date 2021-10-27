'''
线程
python中线程实现有Thread 和 Threading库， Threading是对Thread的封装，一般使用Threading

'''
import threading
import random, time

def fun():
    print("thread name:" + threading.current_thread().name)
    time.sleep(random.random() * 5)
    print("%s thread end"  % threading.current_thread().name)


if __name__=="__main__":
    print("thread name:" + threading.current_thread().name)
    myThread = threading.Thread(target=fun, name="thread-1")
    myThread.start()
    myThread.join()
    print("%s thread end"  % threading.current_thread().name)

