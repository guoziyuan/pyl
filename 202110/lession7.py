'''
集合
特点 ： 无序、不存在相同元素

'''

a = {1, 2, 3, 4}
print(type(a))
'''add'''
a.add(5)
print(a)
a.add(1)
print(a)

'''随机删除一个'''
a.pop()
print(a)

'''
删除指定
'''
a.remove(2)
print(a)

'''
清空
'''
a.clear()
print(a)

'''
集合 交、并、差运算
'''
a = {1, 2, 4}
b = {1, 3, 5}
print(a & b)
print(a | b)
print(a - b)
print(b -a)