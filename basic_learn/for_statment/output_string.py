a = 1
b = 2
print("a: %d, b: %d"%(a,b))
a,b =  b,a
print("a: %d, b: %d"%(a,b))

name = "ab"
print(name)
for n_i in name:
    print(n_i)
print("---------------")
i = 0
while i < len(name):
    print(name[i])
    i += 1
print("---------------")
string = "0123456789"
print("string[0:4]: "   + string[0:4])
print("string[0:]: "    + string[0:])    # all the string
print("string[:]: "     + string[:])     # all the string
print("string[0::]: "   + string[0::])   # all the string
print("string[0::-1]: " + string[0::-1])   # 0 a:b:c if not write a b the defalt stat and end is decide by c, if c is positive a=0 b=last; c is negtive a=0 b=1
print("string[len(string)::-1]: " + string[len(string):0:-1])   # example of up 
print("string[::-1]: " + string[::-1])   # rever it  
print("string[0::2]: "  + string[0::2])  # all the string
print("string[0:9:2]: " + string[0:9:2])
print("string[0:-1]: " + string[0:-1])   # -1 the last 9 so no include it
print("string[0:-1:2]: "+ string[0:-1:2])
print("string[-1:0]: " + string[-1:0]) #nothing  
