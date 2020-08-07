import unittest
from ut_demo_01.math_method import MathMethod#导入被测试类
from ut_demo_01.readfromexcel import doExcel

class TestAdd(unittest.TestCase):
    #每一条用例都是一个类函数
    #def test_后缀(self)，
    def setUp(self):
        self.t=MathMethod()
        self.d = doExcel()
        print('start')

    def __init__(self,a,b,expected,desc,caseid):
        super(TestAdd,self).__init__('test_add')
        self.a=a
        self.b=b
        self.expcted=expected
        self.caseid =caseid
        self.desc = desc
    def test_add(self):
        print("正在执行的是{0}".format(self.desc))
        print("a的值是{0}".format(self.a))
        print("b的值是{0}".format(self.b))
        print("期望结果是{0}".format(self.expcted))

        res = self.t.add(self.a,self.b)
        try:
            self.assertEqual(self.expcted,res)
            testResult = 'PASS'
        except AssertionError as e:

            print('errrrr,err is {}'.format(e))
            testResult = 'FAIL'
            raise e
        finally:
            self.d.writeBack(self.caseid+1,res,testResult)


    def tearDown(self):
        print('end')
    # def test_add_1(self):
    #     t = MathMethod()
    #     res = t.add(11, 8)
    #     print('测试结果是{}'.format(res))

if __name__ == '__main__':
    unittest.main()