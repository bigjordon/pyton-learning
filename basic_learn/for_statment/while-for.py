i = 0
print(id(i))
while i<3 :
    print("yes")
    i += 1
    print(id(i))
else:
    print("else") # do this

print("-"*30)
while True:
    print("yes")
    break
else:
    print("else") # no do this

print("-"*30)
print(id(i))
print(i) # i = 3
i = 0
print(id(i))
while i<3 :
    print("yes")
    i += 1
    if i == 3:
        continue
else:
    print("else") # do this

