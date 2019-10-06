
a = "Global Variable"
x = 10

def GlobalScopeFn():
    print('Inside Method GlobalScopeFn: ' + a)

print('Global Print: ' + a)
GlobalScopeFn()

def x():
    x = 100
    x()

def x():
    print('Inside Function x: ' + x)
    def y():
        print('y')
    y()

x()

def a(f, x):
    print(x)
    f(x)

def func1(x):
    print(x)

a(func1, x)

#Recursion:
def f(x):
    print(x)
    if(x<5):
        x+=1
        f(x)
        print('exiting many times')
        return
    else:
        print('exiting once')

f(1)
