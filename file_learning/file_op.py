f = open("file_op.py", "r") # can not write "r" default is r
print(f)
# data = f.read() # read all
length = 20
data = f.read(length) # read all
data_line = f.readlines() # read all
print(data)
print(data_line)

