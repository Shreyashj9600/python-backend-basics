# Private(like) attributes & methods

# concepthual implementation in python 
# private Attribute & method are meant to use only within the class and are not accessible from out side the class. 

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12345" , "abcde")
print(acc1.acc_no)
print(acc1.reset_pass())


#------------

class person:
    __name = "anonymous"

    def __hello(self,):
        print('hello person')

    def welcome(self):
        self.__hello()

p1 = person()
print(p1.welcome())