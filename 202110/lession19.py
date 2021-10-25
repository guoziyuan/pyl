'''
面向对象
封装
继承
多态
'''

class Person():
    def __init__(self, name, age) -> None:
        print("person init")
        self.__name = name
        self.__age = age

    def work(self):
        print("do work")

    def show(self):
        print("%s is %s years old" % (self.__name, self.__age))

class Teacher(Person):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
        print("Teacher init")

    def work(self):
        print("teaching")

class Student(Person):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
        print("Student init")

    def work(self):
        print("study")

student = Student("小明", 19)
teacher = Teacher("老李", 40)

student.work()
student.show()
# 这种方式无法访问私有变量， 实际是为对象新增了一个字段__age
student.__age = -90
student.show()

teacher.work()
teacher.show()