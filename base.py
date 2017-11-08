name = 'zhangqian'
addr = "xiao-jia-he"
age  = 33
age_more  = 23

# erro print(name + addr + age)
print(name + addr + str(age))
print(name + addr + "%d"%age) # could not have no () for age 
print(name + addr + "%d %d"%(age, age_more)) 

# print add  newline defaultly
# use help(print) to see print usage, int python interactive mode
print("-------------")
#print(name + addr + str(age), end="") #only in python3
print(name + addr + str(age)), #only in python2 
print(name + addr + "%d"%age) # could not have no () for age 

    #i_name = input("intput: ") # python3 same to 3's raw_input
    #print("you inputs: " + i_name)
# age = input() if you input number then age will be type int but not in python3. python3 will not analys the input for safty


print("-------------")
a = 7
b = 3
c = a/b
d = a//b # same as / int C languse
print(c)
print(d)
print(d * 100)
print(d ** 100) # power of 100
print("d" * 100)
print("-------------")
x = "4"
y = "5"
z = x + y
zz = int(x) + int(y) #same as str() and others

if zz > 8:
    print("yes") # tab is necessary
elif zz > 9:
    print("no")
else:
    print("no")
    # no need endif
    
if x == "4":
#if int(x) == int("4"):
    xxxx = 5
    print(x+" yes 4")
#if y <> "4":  # erro do not know why
    print(xxxx)
    print(y+" yes 5")
print(xxxx)
if y != "4":
    print(y+" yes 5")

if not (x and y):
    print(True);
print(False);
# 'if statment' recrusive need strictly tab align
