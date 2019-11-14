import unittest
from ut_demo_01.math_method import MathMethod#导入被测试类

class TestAdd(unittest.TestCase):
    #每一条用例都是一个类函数
    #def test_后缀(self)，
    def setUp(self):
        self.t=MathMethod()
        print('start')

    def __init__(self,a,b,expected):
        super(TestAdd,self).__init__('test_add')
        self.a=a
        self.b=b
        self.expcted=expected
    def test_add(self):

        res = self.t.add(self.a,self.b)
        try:
            self.assertEqual(self.expcted,res)
        except AssertionError as e:

            print('errrrr,err is {}'.format(e))
            raise e


    def tearDown(self):
        print('end')
    # def test_add_1(self):
    #     t = MathMethod()
    #     res = t.add(11, 8)
    #     print('测试结果是{}'.format(res))

if __name__ == '__main__':
    unittest.main()