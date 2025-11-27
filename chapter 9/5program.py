# Super method 
# super() method is use to access method of the parent class.

class car :
    def __init__(self,type):
        self.type = type

    @staticmethod   
    def start():
        print("car started")

    @staticmethod
    def stop():
        print('car stopped')    

class ToyotaCar(car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name = name

car1 = ToyotaCar("prius","electric")
print(car1.type)