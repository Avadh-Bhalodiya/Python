#   decorators
#   also us fun as parameter in decor   than    modified func and return modified func

def change(normal):
    def inner():
        print("\nBefore Enhancing")
        normal()
        print("After enhanching \n")
    return inner

@change
def normal():
    print("Hie")
    print("What are you doing?")

normal()

#   2nd example

def change(num):
    def inner():
        a = num()
        add = a+5
        return add
    return inner

@change
def num():      #   randome function i don't know origin but i modified this fun that time i use decorater
    return 10

print(num())

#   Multiple time enhanced      #   multiple use decorator

def decor1(num):
    def inner():
        a = num()
        multi = a*5
        return multi
    return inner

def decor(num):
    def inner():
        b = num()
        add =  b+5
        return add
    return inner
@decor
@decor1
def num():
    return 10

print(num())
