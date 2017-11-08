j = 9
k = 0
while k < 9:
    k += 1
    l = 0
    while l < k:
        l += 1
        print("%d*%d=%2d "%(l, k, (l)*(k)), end = "")
    print()
