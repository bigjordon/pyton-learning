class ClassA:  # default :  class ClassA(Object)
    __static_num = 0 # like C++ static atrribute that Class's attribute
    def __new__(cls): # before __init__ called imploy a object
        print("new is called")
        return super().__new__(cls) # must call super's __new__
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.__b = b # __b will be protetcted attribute
        print("do init") 
    def do_a(self):
        print("i did")

    def pr_a(self):
        print(self.attribute1) ## access atrribute
    def __private_me(self):    ## private method
        print("iam private")
    @classmethod
    def setNum(cls, newNum):
        cls.__static_num = newNum
    @classmethod
    def getNum(cls):
        return cls.__static_num
    @staticmethod
    def call_me():
        print("whoever can call me, can use Class call directly")

ca = ClassA(1,2)
ca.do_a()
ca.attribute1 = "ggo"          # add a atrribute 1
ca.pr_a()
#ca.__b = 1 erro can not access __b


class ChildA(ClassA):
    def do_child(self):
        print("i am child")
child_a = ChildA(3,4) # child has no parent's private method  and attribute but not __init__ __del__
child_a.do_child()
child_a.do_a()

# muti derive which has the same method will derive the first method
# use class's method __mro__ to see which to call

ClassA.setNum(5) # is _ClassA__static_num
ClassA.__static_num = 4 # is new real _static_num
print(ClassA.getNum())
print(dir(ClassA))
