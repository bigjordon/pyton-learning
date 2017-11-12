import sys
file_name = sys.argv[1]
f_read = open(file_name)
index = file_name.rfind(".")
file_name2 = file_name[:index] + "[attach]" + file_name[index:]
f_write = open(file_name2, "w")


read_len = 2048
content = f_read.read(read_len)
while content != "":
    f_write.write(content)
    content = f_read.read(read_len)

f_read.close()
f_write.close()


#os.rename()
#os.getcwd()
#os.listdir()

list_1 = [["aa", "bb", "cc"], ["dd", "cc"]] 
str_1 = '[["aa", "bb", "cc"], ["dd", "cc"]]' 
str_2 = "[['aa', 'bb', 'cc'], ['dd', 'cc']]" 
str_3 = "[[\"aa\", \"bb\", \"cc\"], [\"dd\", \"cc\"]]" 
#str_3 = "[["aa", "bb", "cc"], ["dd", "cc"]]" #error 
str_a = str(list_1) 
print(str_a)
list_my = eval(str_a)
print("-"*30)
print(list_my)

