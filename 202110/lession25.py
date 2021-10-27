'''
单元测试
给定输入，比较输出

单测成功几个，失败几个，
单测要正确、全面，才能保证被测程序的正确性

 单元测试特点：
 1、继承unittest.TestCase
 2、测试用例以”test_“开头
 3、setUp会在一条测试用例之前执行，teardown会在这一条测试用例后执行，可以用来处理一些前置初始化和后置释放资源操作

'''

# 假设要测试一个加法方法的正确性
def add(a, b):
    return a + b

import unittest

class TestAdd(unittest.TestCase):

    def setUp(self) -> None:
        print("test start")
        return super().setUp()

    def test_add1(self):
        r1 = add(1, 1)
        self.assertEqual(r1, 2)

    def test_add2(self):    
        r2 = add(0, 1)
        self.assertEqual(r2, 1)

    def test_add3(self):
        r3 = add(-1, 12)
        self.assertEqual(r3, 0)
    
    def tearDown(self) -> None:
        print("test end")
        return super().tearDown()
    

if __name__=="__main__":
    unittest.main()
