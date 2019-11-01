#Class is a blueprint of the real-life entity. 
#In Python, it is created using the class keyword as shown in the following code snippet.


# Let's take an example:

# Suppose Parrot is a class. There can be multiple parents 
# but we take any one parent(1 instance) which is the object.

# Hence an Object is an Instance of a class

# A parrot has two characterstics:

# 1. name, age, color are attributes
# 2. singing, dancing are behavior

# Hence to summarize Objects are instance of class 
# An object has two characteristics:
# 1. attributes
# 2. behavior
# Input:
# Hello world today

# Output:
# today world Hello

# class – Here is a class named Person.
class Person:
    name = 'Hello'
    age = 'World'
    def __init__(self, name, age):
        Person.name = name
        Person.age = age
 
# Constructors have the default name __init__. They are functions that are implicitly called when an object of the class is created.
# All instance methods including the constructor have their first parameter as self.
# self refers to instance that is being referenced while calling the method.
# name and age are the instance variables.
    def get_name_age(self):
        return Person.name,Person.age


if __name__ == "__main__":

    person1 = Person("Ajay",30)
    print(person1.get_name_age())


    person2 = Person("Ganesh", 24)

    print(person2.get_name_age())



# Once a Person class is defined you can use it to 
# create an instance by passing values as shown below.
    
    # print(person1.name)
    # print(person1.age)

    # print(person2.name)
    # print(person2.age)


    #You can set the property of object this way:
    # p.name="Ganesh R"

    #You can Delete this way
    # del p.age

