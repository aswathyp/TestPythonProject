# Following is the example of a simple Employee Python class −

class Employee:
   'Common base class for all employees'
   empCount = 0

# The variable empCount is a class variable whose value is shared among all instances of a this class. 
# This can be accessed as Employee.empCount from inside the class or outside the class.

#The first method __init__() is a special method, which is called class constructor 
#or initialization method that Python calls when you create a new instance of this class.
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1


#You declare other class methods like normal functions with the exception that the 
# first argument to each method is self. 
# Python adds the self argument to the list for you; 
# you do not need to include it when you call the methods.

   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)



if __name__ == "__main__":

    "This would create first object of Employee class"
    emp1 = Employee("Akash", 2000)

    "This would create second object of Employee class"
    emp2 = Employee("Anirudh", 5000)


    emp1.displayEmployee()
    emp2.displayEmployee()

    
    
    print ("Total Employee %d" % Employee.empCount)