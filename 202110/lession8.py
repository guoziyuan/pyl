'''
分支结构
'''

'''
给定2个数，从小到大输出
'''
a = input("input a:")
b = input("input b:")

a = int(a)
b = int(b)
if a > b :
    a,b = b,a
print("{},{}".format(a, b))

'''
红灯停，绿灯行，黄灯等一等
'''
light= "red"
if light == "red" :
    print("停")
elif light == "green":
    print("行")
else:
    print("等一等")


'''
内联if ： if表达式在一行表示
比如取两个数中最大值
'''
a = 1
b = 2
c = a if a > b else b
print(c)

'''
条件表达式中的逻辑运算符 与（and） 或（or）非（not）
'''
age = 10

if age >= 18 and age <= 60 :
    print("是成年人")
else:
    print("不是成年人")

a = 100
b = -80

if a >= 0 or b >= 0 :
    print("有非负数")
else:
    print("都是负数")

if not age < 18:
    print("可以进网吧")
else:
    print("不能进网吧")