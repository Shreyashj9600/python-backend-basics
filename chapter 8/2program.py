# class and instance Attribute

# class.attr
# obj.attr 

class Student :
    collage_name = "ABC Collage"       
    # name = "anonymous"     # class attr 

#  constructor
    def __init__(self,name,marks):
        self.name = name  # obj attr > class attr
        self.marks = marks
        print('Adding new student in database')

#   methods 
    def welcome(self):
        print('welcome student ,' , self.name)
        
s1 = Student('karan' , 97)
# print(Student.name) # construcor
s1.welcome()





