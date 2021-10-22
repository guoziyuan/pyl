'''
数据结构
'''

'''
列表
定义，增、删、改、查
'''
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = []

print(a)
print(b)
print(len(a))
print(len(b))

print(a[1])

print("----------添加、删除-----------")
a.remove(0)
b.append(1)

print(a)
print(b)
print(len(a))
print(len(b))

print(a[1])

print("---------修改、查询-----------")
a[0] = 999
b[0] = 1000
print(a[:5:2])
print(b)