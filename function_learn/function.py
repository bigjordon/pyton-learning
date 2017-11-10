# function user reference to pass the argument
def my_func():
    print("do some thing")
my_func()  

def add2num(a,b):
    return a+b

a = 5
b = 6
print(add2num(a, b))


def my_func1(a, b, c =0, d=66): # the default arg must the last
    print(a + b + c + d)

my_func1(1, 2, d=4) # you can designate the default arg


def my_func2(a, b, *args): # Variable length args
    print("do")            # args will be tuple


def my_fun3(a, b, *args, **kwargs): # Variable length args
    print("do")            # args will be dict

my_fun3(1,2,3,4,5) # 3,4,5 all will be give args
my_fun3(1,2,3,4,5, mm=2, nn=5) # 3,4,5 all will be give args
                               # mm=2 nn=5 will give dict

A=[11, 22, 33]
B={"aa":33, "bb":55}
my_fun3("dd", "ff", A, B)
my_fun3("dd", "ff", *A, **B) # my_fun3(dd, ff, 11, 22, 33, aa=33, bb =55)

vv = 100
vvv = vv ## vvv same as us the same id vv copy on write 
print(id(vv))
print(id(vvv))
vv = 40 # the the id of vv chenaged since type(100) can not change
print(id(vv)) 

vv = [1,2]
vvv = vv 
vv = [3,4] # not change since [] can change
