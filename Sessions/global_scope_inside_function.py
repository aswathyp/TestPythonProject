def GlobalScope():
    print(a)

a = "Globalscope"
GlobalScope()


#Error
def LocalScope():
    a = "Localscope"

LocalScope()
print(a)


#global same variable, local scope
#if some variable is modified inside the function,
#the variable becomes a local variable
#and its modification will not change a global variable with the same name.
#its modification will not change a global variable with the same name.
def f():
    a = 50
    print(a)

a = 100
f()
print(a)

#local variable modified before assignment.
#in the function f() the identifier a becomes a local variable,
#since the function contains the command which modifies the variable a.
#The modifying instruction will never be executed,
#but the interpreter won't check it. Therefore, when you try to print the variable a,
#you appeal to an uninitialized local variable.
def f():
    print(a)

a = "Error Condition"
f()

def a():
    def c():



#global keyword
#bad idea, use return inside
#

def f():
    global a
    a = 1
    print(a)

a = 0
f()
print(a)