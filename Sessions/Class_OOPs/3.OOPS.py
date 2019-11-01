# The concept of OOP in Python focuses on creating reusable code. 
# This concept is also known as DRY (Don't Repeat Yourself).

# In Python, the concept of OOP follows some basic principles:

# 1.Inheritance	    A process of using details from a new class without modifying existing class.
# 2.Encapsulation	Hiding the private details of a class from other objects.
# 3.Polymorphism	A concept of using common operation in different ways for different data input.
# 4.Abstraction     hiding the complexity and only showing the essential features of the object

#Inheritance

# parent class
class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        super().swim()
        print("Penguin")

    def run(self):
        print("Run faster")


peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()


#In the above program, we created two classes i.e. Bird (parent class) and Penguin (child class). 
#The child class inherits the functions of parent class. We can see this from swim() method. 
#Again, the child class modified the behavior of parent class. We can see this from whoisThis() method. Furthermore, we extend the functions of parent class, by creating a new run() method.

#Additionally, we use super() function before __init__() method. 
# This is because we want to pull the content of __init__() method from the parent class 
# into the child class.