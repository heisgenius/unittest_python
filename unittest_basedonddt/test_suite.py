import unittest
# 导入测试类
from ut_demo_01.testclass_01 import TestAdd
from ut_demo_01 import testclass_01
from ut_demo_01.readfromexcel import doExcel
import HTMLTestRunnerNew
from ut_demo_01.configstu import readConfig

button = readConfig().readconfig('testcase.conf','option','button')
caseid = eval(readConfig().readconfig('testcase.conf','option','caseid'))
# 加载测试用例
'''
suite  中文解释为  测试套件 或者是测试用例的容器
'''
suite = unittest.TestSuite()#创建了TestSuite的实例
testdata= doExcel().do_excel()
if button == 'on':
    final_data  = testdata
else:
    final_data =[]
    for item in testdata:
        if item['caseid'] in caseid:
            final_data.append(item)

# 把用例放进测试套件里面去
"""A test suite is a composite test consisting of a number of TestCases.

   For use, create an instance of TestSuite, then add test case instances.
   When all tests have been added, the suite can be passed to a test
   runner, such as TextTestRunner. It will run the individual test cases
   in the order in which they were added, aggregating the results. When
   subclassing, do not forget to call the base class constructor.
   这是源码里面的解释，下面用翻译软件解释一下
   测试套件是由许多测试用例组成的复合测试。为了使用，创建一个TestSuite实例，然后添加测试用例实例。
   在添加了所有测试之后，可以将套件传递给测试，运行器，如TextTestRunner。它将运行各个测试用例
   按照它们被添加的顺序，聚合结果。当子类化时，不要忘记调用基类构造函数。
   """
# 方法一
for item in testdata:
    # print('正在执行的测试为{}'.format(item['desc']))
    suite.addTest(TestAdd(item['a'],item['b'],item['expected'],item['desc'],item['caseid']))
# suite.addTest(TestAdd('test_add_1'))


# 方法二
# loader = unittest.TestLoader()
# 可以直接加载某个测试类里面的所有用例
# 也可以直接加载某个模块里面的用例
# suite.addTest(loader.loadTestsFromTestCase(TestAdd))#根据类名
# suite.addTest(loader.loadTestsFromModule(testclass_01))#根据模块名


# 执行用例
'''
TextTestRunner   专门执行测试套件（suite）里面的类
'''
with open('testres.html','wb+') as file:#二进制的文件，写入方式写成wb+，然后encoding不写
    # runner = unittest.TextTestRunner(file,verbosity=2)
    runner = HTMLTestRunnerNew.HTMLTestRunner(file,verbosity=2,title='testres',description='dumy',tester='WWWW')
    runner.run(suite)

