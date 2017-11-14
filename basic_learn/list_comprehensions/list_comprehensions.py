'''
variable = [out_exp for out_exp in input_list if out_exp == 2]
'''
multiples = [i for i in range(30) if i % 3 is 0]
print(multiples)

squared = [x**2 for x in range(10)]
print(squared)

my_set = { i*i for i in range(1, 21) if i % 2 != 0 }
print(my_set)

my_dic = { i:i*i for i in range(30, 40) if i% 2 != 0 }
print(my_dic)

import os
my_dir = [item for item in os.listdir(os.path.expanduser('~')) if os.path.isdir(item)]
print(my_dir)
