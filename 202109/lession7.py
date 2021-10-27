'''
ThreadLocal
保证了每个线程只能获取自己的那一份关联对象

每个线程有自己的一份对象，多线程调用时，同一线程每次调用都想获得自己的对象，不受其它线程干扰
'''

import threading
import random

# 三个老师给学生打分
class Student():
    def __init__(self, name) -> None:
        self.__name__ = name
        self.__score__ = 0

    def set_score(self, score):
        self.__score__ = score

    def __str__(self) -> str:
        return "name is {}, score is {}".format(self.__name__, self.__score__)

local = threading.local()


def fun_thread(name):
    local.stu = Student(name)
    # 打分
    fun_score()
    # 打印成绩单
    fun_show()

def fun_score():
    stu = local.stu
    stu.set_score(random.choice([0, 10,20, 30, 40, 50, 60, 70, 80, 90, 100]))

def fun_show():
    stu = local.stu
    print(stu)


th1 = threading.Thread(target=fun_thread, args=("小明",), name="thread-1")
th2 = threading.Thread(target=fun_thread, args=("小红",), name="thread-2")
th1.start()
th2.start()
th1.join()
th2.join()
