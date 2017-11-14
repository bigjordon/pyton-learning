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


map( lambda x: x*x, [y for y in range(10)] )
#class map(object)
#|  map(func, *iterables) --> map object
#|  
#|  Make an iterator that computes the function using arguments from
#|  each of the iterables.  Stops when the shortest iterable is exhausted.
#|  
#|  Methods defined here:
#|  
#|  __getattribute__(self, name, /)
#|      Return getattr(self, name).
#|  
#|  __iter__(self, /)
#|      Implement iter(self).
#|  
#|  __new__(*args, **kwargs) from builtins.type
#|      Create and return a new object.  See help(type) for accurate signature.
#|  
#|  __next__(self, /)
#|      Implement next(self).
#|  
#|  __reduce__(...)
#|      Return state information for pickling.
