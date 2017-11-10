def fun(a):
    print(id(a))
    a += a
    #a = a + a # is differ  a += a rember it attention
    print(id(a))

A = 100          # can not change
B = [100, 200]   # can change

print(A)
fun(A)
print(A)


print(B)
fun(B)
print(B)
