
# OOPs - attributes & behaviour

class Employee:
    empCount = 0

    def __int__(self):
        print('Base Constructor')

    def __init__(self, name = '', age = 20, salary = 4000):
        self.name = name
        self.age = age
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print('Total Employee %d' %Employee.empCount)

    def displayEmployee(self):
        print('Name: ', self.name, 'Age: ', self.age, 'Salary: ', self.salary)

if __name__ == '__main__':
    emp1 = Employee('Aswathy', 35, 5000)
    print('Current Employee Count: ', Employee.empCount)
    emp2 = Employee('Arun', 30, 10000)

    #Employee.displayCount() - It will fail because the displayCount is a method in class with self.
    # Only instances can call the methods in a class because methods in a class by default have self as first parameter.

    emp1.displayEmployee()
    emp2.displayEmployee()
    emp1.displayCount()
    Employee().displayCount()

# Inheritance, Encapsulation, Polymorphism, Abstraction