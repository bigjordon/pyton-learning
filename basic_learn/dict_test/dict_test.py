my_dict = {"name": "zhangq", "age": "26"}
print(my_dict["name"])
print(my_dict.get("name"))
for temp in my_dict.items():
    print("%s %s"%(temp[0], temp[1]))
print("-----------------")
for key, value in my_dict.items():
    print(key)
    print(value)
print("-----------------")
for key, value in enumerate(my_dict):
    print(key, value)
print("-----------------")
for key in my_dict.keys():
    print(key)
print("-----------------")
for value in my_dict.values():
    print(value)
print("-----------------")
my_dict.clear()
print(my_dict)
print("-----------------")
del my_dict
print(my_dict) # error
