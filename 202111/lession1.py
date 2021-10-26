'''
有n块2*1的矩形，将其不重叠放进2*n的矩形盒子里，有多少种放法
解法
斐波拉契数列
f(n) = f(n-1) + f(n-2)
'''

# 递归实现
def fabo(n) :
    if n ==1 :
        return 1
    elif n == 2 :
        return 2
    else:
        return fabo(n-1) + fabo(n-2)


# 非递归实现
def feibo(n) :
    if n == 1 :
        return 1
    elif n==2 :
        return 2
    else:
        a = 0
        b = 1
        c = 2
        i = 3
        while i <= n :
            i+=1
            a = b
            b = c 
            c = a + b
        return c

import time

t1 = time.time()
print(fabo(30))
t2 = time.time()
print(feibo(30))
t3 = time.time()

print("t2 - t1 = %s, t3 - t2 = %s" % (t2-t1, t3-t2))