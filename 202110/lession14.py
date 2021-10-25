'''
map
对一组元素分别按照同一规则进行操作，得到一组新的数据

reduce
对一组数据中数据分步操作，得到一个结果
'''
a = range(1, 11)
def fun(k):
    return k**3

print(a)
# 对列表中的数据分别做乘方操作
b = map(fun, a)
print(list(b))


#求列表中最大的元素
from functools import reduce

def max(a, b):
    if a > b :
        return a
    else:
        return b

c = reduce(max, a)
print("最大数：%s" % c)