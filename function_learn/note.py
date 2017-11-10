g_a = 100

g_list = [11, 33]
print(g_a)
print(g_list)
def test():
   # global g_a # no declear will be local for unghangeable 
    g_a = 200 
    global g_list
    g_list.append(44) # changeble no need global declear
    print(g_a)
    print(g_list)
test()
print(g_a)
print(g_list)
