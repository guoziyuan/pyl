'''
切片
切片特点，左闭右开，默认步长为1，步长为1时可以省略
逆向操作，步长为负数，不能省略
增、删、改、查
'''

data = list(range(1, 11))
print(data)

# 顺序查
print(data[:])
print(data[0:2])
print(data[0])
#逆序查
print(data[::-1])
print(data[-1:-3:-1])
print(data[-1])

#指定步长查询
print(data[0::2])
print(data[1::2])

#增加（片段插入）
length = len(data)
# 在尾部插入
data[length:] = [100, 90]
print(data)
#在头部插入
data[:0] = [-100,-90]
print(data)
#在中间指定区域插入
data[2:2] = [22,11]
print(data)

data[20:20] = [22,11]
print(data)

#修改 (替换)

#等长修改（片段置换）
data[0:2] = [-2,-1]
print(data)
#不等长修改 （片段置换）
data[0:2] = [-3]
print(data)
data[0:2] = [-3,-2,-1]
print(data)
#间隔修改,注意左右长度要相等，否则会报错
data[::6] = ["x","y","z"]
print(data)

#删除
data[0:1] = []
print(data)

del data[0:3]
print(data)