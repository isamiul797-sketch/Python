#Create a Parent Class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

#Create a Child Class
class Student(Person):
  pass

#Add the __init__() Function
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

#Use the super() Function
#Python also has a super() function that will make the child class inherit all the methods and properties from its parent

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

#Add Properties
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

#Add Methods
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

