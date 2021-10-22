'''
输入输出
'''

s = input("请输入你选择的水果：")
print("您选择了" + s)
d = input("请输入重量（kg）：")
print("您需要%skg%s"%(d, s))

print("您需要{}kg{}".format(d, s))

print("您需要"+str(d)+"kg"+s)