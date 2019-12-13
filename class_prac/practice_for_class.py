class A:
    def __init__(self,name):
        self.name=name
        print('这是父类的初始化方法')
    def show(self):
        print('这是父类的show方法')

class B(A):
    def __init__(self,name,age):
        super(B,self).__init__(name=name)
        self.age =age
        print(age,name)
    def show(self):
        super(B,self).show()
b = B('JACK','19')
b.__init__('jack','10')