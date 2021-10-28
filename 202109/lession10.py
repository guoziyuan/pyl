# coding="utf-8"

"""
 yield 深入理解
 生成器函数f有两个关键函数
 1、next(f)  调用一次，恢复Generator执行
 2、f.send(value) 调用一次，恢复Generator执行 ，并向使用value 替代中断位置的yield 表达式，实现数据传递，
    返回值是下一个yield表达式的参数，如果没有下一个yield表达式，则会中断
"""


def fun():
    k = yield 1
    print("k:" + str(k))
    n = yield 2
    print(("n" + str(n)))


if __name__ == "__main__":
    f = fun()
    print("next")
    # 启动生成器函数f, 返回第一个yield 表达式的参数 1
    p = f.send(None)
    print("p : " + str(p))
    # 发送数据给第一个yield表达式，返回第二个yield 表达式的参数 2
    g = f.send(11)
    print("g : " + str(g))
    # 发送数据给第二个yield表达式，因为没有yield表达式了，会中断程序， q不会被赋值
    q = f.send("22")
    print("q:"+str(q))
