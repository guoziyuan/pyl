'''
序列化：内存中的对象存储到文件中或者网络传输时，需要序列化
反序列化：把文件或者网络传输内容还原成内存中的对象，即是反序列化
序列化前后两个对象内存地址是不同的
'''

# 把一个字典写入文件
d = {"1":20, "2": 30, "3":40}
from os import rename
import pickle
# python 中可以使用pickle把对象转化成二进制文件
print(pickle.dumps(d))
d1 = pickle.loads(pickle.dumps(d))
print(d1)
# x写入文件
fileName ="3.txt"
with open(fileName, 'wb') as f :
    pickle.dump(d, f)

# 从文件中恢复
with open(fileName, 'rb') as f:
    d2 = pickle.load(f)
    print(d2)
   

# 编程语言之间传递对象需要标准格式，开发中一般使用JSON来格式化对象

import json
d = {"1":20, "2": 30, "3":40}
mylist = ["1", "2"]
print(json.dumps(d))
print(json.dumps(mylist))

# 自定义类对象怎么转JSON呢

class Student():
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age
    }
s = Student("xiaowang", 20)
# lambda obj :obj.__dict__  将对象转成字典
s1 = json.dumps(s, default= lambda obj :obj.__dict__)
s2 = json.dumps(s, default=student2dict)

print(s1)
print(s2)
# json转对象  object_hook函数负责把dict转换为Student实例：
def dict2student(dict):
    return Student(dict["name"], dict["age"])
s3 = json.loads(s1, object_hook = dict2student)
print(s3)