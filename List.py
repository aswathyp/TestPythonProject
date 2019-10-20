
a=[]

for i in range(0,10):
    a.append(i)
    print(a)

b=[0]*10
for i in range(0,10):
    b[i]=i
    print(b)

def x():
    print('x')

def y():
    print('y')

b[0] = x
b[1] = y

b[0]()
b[1]()

