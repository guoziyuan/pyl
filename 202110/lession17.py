'''
闭包
闭包3个条件
1、函数中有局部函数
2、局部函数用到了外部函数变量
3、外部函数返回值为局部函数
'''

# 计算乘方

def fun(n) :
    def cheng(k) :
        return k ** n
    return cheng

# 平方
ping = fun(2)

# 立方
li = fun(3)

for i in range(1, 10):
    print(ping(i), end=" ")
   
print("")

for i in range(1, 10):
    print(li(i), end=" ")