'''
元组

元组特点：生成之后，元素指向不可改变，可以查询
元组本身可以被删除
空元组 ()
'''

'''
声明一个只有一个元素的元组，逗号不能省略
'''
a = (1,)
print(type(a))

print(a[0])

'''
元组与元组之间可以进行 连接 和 迭代 操作
'''
b = (2,3,4,5,6)

c = a + b

print(c)

d = b * 5

print(d)

del a

'''
理解元组元素指向不变

元组中的元素可以是一个数组，这个数组中的元素是可以改变的
'''
g = [1, 2, 3]

g.append(919)
f = (1, 2, g)
print(type(g))
print(f)
g.append(99)
print(g)
print(f)
g[-1] = 99
f[2][0] = 100
print(f)
f[2].clear()
print(f)
f[2].append(90)
print(f)
f[2].append(90)
print(f)
f[2].append(90)
print(f)
f[2].append(90)
print(f)

print(f[2] == g)

print(g)