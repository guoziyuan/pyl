'''
字典

定义
使用：增、删、改、查
'''
a = {
    "张三":100,
    "李四":90,
    "王五":0
}

print(a)

a["王五"] = 80

print(a)

a["小明"] = 30

print(a)

del a["张三"]
print(a)