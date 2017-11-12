class Singleton(object):
    __instance = None
    __first_init = False
    
    def __new__(cls, arg1):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance
    def __init__(self, arg1):
        if not self.__first_init:
            self.arg = arg1;
            Singleton.__first_init = True

a = Singleton(1)
print(str(id(a)) + str(a.arg))
b = Singleton(2)
print(str(id(b)) + str(b.arg))
