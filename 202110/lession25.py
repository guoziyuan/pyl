'''
单元测试
给定输入，比较输出

单测成功几个，失败几个，
单测要正确、全面，才能保证被测程序的正确性
'''

# 假设要测试一个加法方法的正确性
def add(a, b):
    return a + b

import unittest

class TestAdd(unittest.TestCase):

    def test_add1(self):
        r1 = add(1, 1)
        self.assertEqual(r1, 2)

    def test_add2(self):    
        r2 = add(0, 1)
        self.assertEqual(r2, 1)

    def test_add3(self):
        r3 = add(-1, 12)
        self.assertEqual(r3, 0)
    
if __name__=="__main__":
    unittest.main()
