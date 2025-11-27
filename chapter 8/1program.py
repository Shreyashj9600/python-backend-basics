# oop in python
# to map whit real world scenarios we started using object in code this is called object oriented programming.

# class and object in python
# class is a blueprint for creating objects.

# creating class

# class Student:
#       name = "karan kumar"
#
# creating object(instance)
# s1 = Student()
# print(s1.name)

class Car:
    color = "blue"
    brand = 'tata'

car1 = Car()
print(car1.color)

# constructor in python

class Student:
    def __init__(self,name,marks):
      self.name = name 
      self.marks = marks
      print('adding new student in database')

s1 = Student("karan",97)
print(s1.name)
print(s1.marks)       
