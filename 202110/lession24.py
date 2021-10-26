

'''
异常处理
'''

try:
    a = 9/0
except ZeroDivisionError:
    print("出错了，除数不能为0")
else:
    print("程序正常："+ str(a))
finally:
    print("这里一定会被执行")


'''
程序调试技巧

1、print输出
2、assert 断言
3、断点调试
'''

def divide(a, b):
    if b == 0 :
        print("除数为0！")
    assert b!=0 , "除数为0"
    return a/b

divide(9, 9)
divide(9, 0)