# parent class
class Person(object):
 
    # __init__ is known as the constructor
    def __init__(self, name, idnumber, salary, post):
        self.name = name
        self.idnumber = idnumber
        self.salary = salary
        self.post = post
 
    def display(self):
        print(self.name)
        print(self.idnumber)
        print(self.salary)
        print(self.post)

 
# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        # invoking the __init__ of the parent class
        super().__init__(name, idnumber, salary, post)
 
# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")
 
# calling a function of the class Person using its instance
a.display()  
