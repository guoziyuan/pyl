'''
装饰器
背景：想要给所有函数加上一行日志输出
传统做法对每个函数一个个去修改，重复且麻烦
装饰器就可以较为优雅解决这个问题

装饰器特点是：
是一个闭包函数，函数参数是一个函数
'''

def derector(fun):
    def wrap(*args, **kvArgs):
        print("---------log------")
        return fun(*args, **kvArgs)
    return wrap


'''
装饰器函数可以把函数传入，得到装饰后的函数，也可以使用注解的形式
'''

# 加法
@derector
def add(*args):
    i = 0
    for x in args:
        i+=x
    return i

# 乘法
@derector
def muliti(*args):
    i = 1
    for x in args:
        i*=x
    return i

print(add(1, 2, 3, 4))
print(add(1, 2,4))

print(muliti(1, 3, 8))