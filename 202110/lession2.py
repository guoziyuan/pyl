'''
数据类型

数值型（整型int，浮点型float）、布尔型（True，False）、字符型（str，repr）
'''
a = 1
b = 2.5
c = True
d = False
e = "python"
f = '@'
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

'''
str 和 repr区别，repr可以让输出结果带上引号
'''
temp = "I like python"
print(temp)
print(repr(temp))

'''
数值和字符类型转换
'''
a = 4
b = 5
print(a+b)
print(str(a)+str(b))