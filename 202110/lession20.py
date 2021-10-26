'''
文件读写
打开文件模式为r, 为只读，不能写入
注意打开文件模式为 r+，向文件写入时，不会删除原有文件内容，在文件末尾写入
打开文件模式为w+，向文件写入时，会删除原来文件内容，从头开始写
'''
# 打开一个文件（如果不存在会创建),往里面从头开始写数据
f = open("1.txt", 'w')
f.write('a')
f.write('b')
#最后要关闭文件
f.close()


# 为了避免忘记关闭文件，可以使用with as，系统会隐式关闭文件
with open("1.txt", 'w+') as f:
    #写一个字符
    f.write('c')
    #写入一个数组
    names = ["1\n", "2\n", "3\n", "hahhah\n"]
    f.writelines(names)

#读取一个文件
with open("1.txt", "r+") as f:
    # 一个字符 一个字符的读取，读取所有
    # print(f.read())
    # # 读取指定个数字符
    print(f.read(3))
    # #读取一行
    print(f.readline())
    # #读取多行, 返回一个数组
    print(f.readlines())
    #这种模式下写文件，不会删除之前的内容
    f.write("fff")

# 实现文件复制
f1 = open("1.txt", 'r')
f2 = open("2.txt", 'w')
f2.writelines(f1.readlines())
f1.close()
f2.close()
