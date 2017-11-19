
'''
catch multi exception, put them in a tuple and result in exp
'''
try:
    open(abc)
except (NameError, FileNotFoundError) as exp: # multi exception put in tuples 
    print("I catch it.")
    print(exp)

'''
catch multi exception, put them in a tuple
'''
try:
    open(abc)
except (NameError, FileNotFoundError): # multi exception put in tuples 
    print("I catch it. no Name")

'''
catch one exception
'''
try:
    open("abc.txt")
except FileNotFoundError: # multi exception put in tuples 
    print("I catch it no file.")

'''
catch all exception
'''
import time
try:
    print(ddd)
except Exception as result:
    print(result)
