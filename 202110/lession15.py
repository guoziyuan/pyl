'''
迭代器 
可迭代对象：数组、元组、集合、字典、字符串

'''

a = range(1, 11)
# 获得迭代器对象

b = iter(a)
i = 0
while(i < len(a)):
    print(next(b), end=" ")
    i+=1



print("")


'''
生成器
可以减少程序运行内存占用和时间
'''
# 标准定义 yield关键字
def fun(n):
    for i in range(n):
        yield i * i

#获得生成器对象
g = fun(5)
# 输出生成器中的内容
for i in g:
    print(i, end=" ")

print("")

# 简化定义生成器
k = (i * i for i in range(5))
for i in k:
    print(i, end=" ")

print("")

import sys
import time

t1 = time.time()
myList = [i * 2 for i in range(1000000)]
t2 = time.time()
print("t2-t1= %s" % (t2 - t1))
print(sys.getsizeof(myList))


print("")
# 使用生成器，占用内存少，耗费时间少
t3 = time.time()
gen = (i*2 for i in range(1000000))
t4 = time.time()
print("t4-t3= %s" % (t4 - t3))
print(sys.getsizeof(gen))

# 计算
def fa(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fa(n-1) + fa(n-2)