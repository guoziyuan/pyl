'''
循环
'''

'''
遍历list
'''
a = [1, 2, 3, 4, 5]

for i in a:
    print(i)

for index, data in enumerate(a):
    print(index, data)

'''
遍历map
'''
b = {
    "张三":100,
    "李四":90,
    "王五":70
}
for key, value in b.items():
    print(key, value)

for key in b.keys():
    print(key)

for value in b.values():
    print(value)

'''
遍历字符串
'''
c = "python"
for tmp in c:
    print(tmp)

'''
利用range控制遍历位置
'''

for i in range(1,3):
    print(a[i])
    