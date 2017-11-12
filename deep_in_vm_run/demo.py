import foo
a = [1, "test"]
a = "a string"

def func():
    a = 1
    b = 333
    print(a + b)

print(a)

if __name__ == "__main__":
    func()
    print(foo.add(1, 2))
