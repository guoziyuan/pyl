'''
多线程会出现线程安全问题

需要锁保证


'''

# 抢票程序，100张票， 3个人抢票

import time, random
import threading

# ticket = 100

# def get_ticket():
#     global ticket
#     while(ticket > 0) :
#         id = ticket
#         ticket-=1
#         # time.sleep(random.random())
#         print("%s 抢到了第 %s号票" % (threading.current_thread().name, id))
       
#     print("no ticket")


# th1 = threading.Thread(target=get_ticket, name="甲")
# th2 = threading.Thread(target=get_ticket, name="乙")
# th3 = threading.Thread(target=get_ticket, name="丙")

# th1.start()
# th2.start()
# th3.start()
# th1.join()
# th2.join()
# th3.join()
# print("ticket :" + str(ticket))

# 取钱问题

# 存款为0
balance = 0

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
        change_id(i)
        time.sleep(random.random())

# 丈夫和妻子同时去操作账户
hus = threading.Thread(target=run_thread, name="丈夫")
wife = threading.Thread(target=run_thread, name="妻子")
hus.start()
wife.start()
hus.join()
wife.join()
print("balance:" + str(balance))
