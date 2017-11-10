student = [] 
while True:
    print("="*30)
    print(" student management system")
    print("1 add something")
    print("2 del something")
    print("3 mod something")
    print("4 qur something")
    print("5 shw something")
    print("0 exit")
    print("="*30)

    key = input("input your selection")
    if "0" == key:
        break 
    if "1" == key:
        name = input("input you name")
        age  = input("input you age")
        sex  = input("input you sex")
        tmps = {"name":"", "age":"", "sex":""}
        tmps['name'] = name 
        tmps['age']  = age
        tmps['sex']  = sex 
        student.append(tmps)
    if "5" == key:
        print(student)
