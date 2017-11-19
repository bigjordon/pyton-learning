my_list = ["zhanqi", 444, ["aa", "bb"]]
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

nameList = ["lilek", "asdii", "rr4444"]
for name_t in nameList:
    if name_t == "lilek":
        print("find it.")
        break;
    print("not find it.")


nameList.append("good")
print(nameList)

nameList.append([333, 444])
print(nameList)

nameList.insert(3, "bod")
print(nameList)

nameList.extend(my_list)
print(nameList)
print(nameList[nameList.index([333, 444])][1])
nameList[1] = "do it"
print(nameList)

if "do it" in nameList:
    print("find it agin")
if "d" in "do it":
    print("find d agin")

nameList.count('asdii')
nameList.index('asdii')
if 'asdii' in nameList:
    print("")
if 'asdii' not in nameList:
    print("")
