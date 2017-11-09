string = '01234567890123456789'
print(string.find("34")) # 6
print(string.find("8888")) # -1 not find
print(string.index("34")) # 6 
#print(string.index("888")) # error 
print(string.rfind("34")) # 6
print(string.count("3"),0, len(string)) #2 threre is 2 "3“ 

print(string.replace("34", "dd")) 
print(string.rsplit("34")) # 012 56789012 56789 
print(string.rsplit()) # default use " " 


print(string.center(10)) 
print(string.center(30)) 


print(string.rjust(30)) 
print(string.ljust(30)) 

print(string.lstrip("01")) # remove the the left 01 

con = "$$"
name = "zhangqi"
li = ["bb", "44", "gg"]
print(con.join(li)) # bb$$44$$gg
print(con.join(name)) #z$$h$$a$$n$$g$$q$$i 
