import unittest
from ut_demo_01.math_method import MathMethod#导入被测试类

class TestAdd(unittest.TestCase):
    #每一条用例都是一个类函数
    #def test_后缀(self)，
    def test_add(self):
        t=MathMethod()
        res = t.add(3,8)
        print('测试结果是{}'.format(res))

    def test_add_1(self):
        t = MathMethod()
        res = t.add(11, 8)
        print('测试结果是{}'.format(res))

if __name__ == '__main__':
    unittest.main()