#   arg : operation
lambda a:a+1

fun = lambda a:a+1
print(fun(3))

def test(a, b, X):
    return X(a, b)

print(test(1, 2, lambda x,y:x-y))
print(test(1, 2, lambda x,y:x+y))
print(test(1, 2, lambda x,y:x*y))


A = [{"name": "aa", "age":24}, {"name": "bb", "age":26},\
    {"name": "cc", "age":27}] 
print(A)
A.sort(key=lambda x:x["age"])
print(A)


B = [{"name": "aa", "age":24}, {"name": "bb", "age":26},\
    {"name": "cc", "age4":27}]  
print(B)
B.sort(key=lambda x:x["age"]) # error age4 can not find
print(B)
