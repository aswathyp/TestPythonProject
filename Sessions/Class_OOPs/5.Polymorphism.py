# Polymorphism is an ability (in OOP) to use common interface for multiple form (data types).

# Suppose, we need to color a shape, there are multiple shape option (rectangle, square, circle). 
# However we could use same method to color any shape. This concept is called Polymorphism.

class Parrot:
    
    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)

# In the above program, we defined two classes Parrot and Penguin. 
# Each of them have common method fly() method. However, their functions are different. To allow polymorphism, we created common interface i.e flying_test() function that can take any object. 
# Then, we passed the objects blu and peggy in the flying_test() function, it ran effectively.