'''
模块
系统模块、自定义模块、第三方模块
'''
#系统模块 
import os
print("cpu_count:%s"% os.cpu_count())

import sys
print(sys.path)
print(sys.argv)
print(sys.platform)

import time
print(time.localtime())
print(time.ctime())

import math

print(math.cos(90))
print(math.exp(2))
import random
#范围内取一个随机数
for data in range(1,10):
    print("random:%s" % random.randrange(1, 100, 2))

#范围内随机取一个
names = ["小明", "小红", "小王", "小黑"]
for data in range(1,10):
    print("choice:%s" % random.choice(names))



