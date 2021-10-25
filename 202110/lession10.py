'''
函数基本使用
'''

#基本函数
def sum(a, b):
    return a+b

f = sum(1, 2)
print("1 + 2 = " + str(f))

# 局部函数，函数作用范围内定义函数
def counter(mode, a, b):
    def add(a, b):
        return a+b
    def subtraction(a, b):
        return a-b
    if(mode == "+"):
        return add(a, b)
    if(mode == "-"):
        return subtraction(a, b)

print("add :%s"% counter("+", 1, 2))

# 匿名函数，lambda
def computer(mode):
    if(mode == "+"):
        return lambda a,b : a+b
    if(mode == "-"):
        return lambda a,b : a-b
f = computer("+")
print("add :%s"% f(1, 2))
'''
函数作用范围内，改变全局变量的值，只在函数作用方位内生效，如果需要全局生效，需要global关键字
'''

message = "Python is so easy"

def modify():
    message = "python is difficult"
    print("modify:" + message)

modify()
print(message)

def tran():
    #声明全局
    global message
    message = "python"
    print("tran:" + message)
tran()
print(message)