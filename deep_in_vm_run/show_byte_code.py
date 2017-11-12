# use command `` to show byte code

import sys

name = sys.argv[1]
s = open(name).read()
co = compile(s, name, 'exec')
import dis
dis.dis(co)

def test():
    s = 0
    print(["in func test"] + dir()) 
    print(s)
if __name__ == "__main__":  # each module will be assigned a __name__  be same as file name 
                            #excepte the main module will be assigned the name of __main__
    test()
    print(["end"] + dir()) ## show the namespace default current
    print(["__builtins__"] + dir(__builtins__))

# LEGB
# local -> enclosing function -> globals -> builtins
