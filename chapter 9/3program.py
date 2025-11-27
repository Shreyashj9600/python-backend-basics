# inheritance
# we one class (child/derived) derives the properties & method of another class(parent/base)

# singel inheritance
class car :
    color = "black"
    @staticmethod   
    def start():
        print("car started")

    @staticmethod
    def stop():
        print('car stopped')    

class ToyotaCar(car):
    def __init__(self,name):
        self.name = name

car1 = ToyotaCar('fortuner')
car2 = ToyotaCar('prius')                

print(car1.start())
print(car1.color)


# type of inheritance 
# * single inheritance
# * Multi-level inheritance
# * Multiple inheritance


# Multi-level inheritance
class car :
    @staticmethod   
    def start():
        print("car started")

    @staticmethod
    def stop():
        print('car stopped')    

class ToyotaCar(car):
    def __init__(self,name):
        self.name = name

class fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = fortuner("diesel")        
car1.start()