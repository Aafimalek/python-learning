#multilevel inheritence
class Car:
    #color = "black"
    @staticmethod
    def start():
        print("car started")
    
    @staticmethod
    def stop():
        print("car stopped")

class Toyotacar(Car): #inheritence 
    def __init__(self,brand):
        self.brand = brand
        print(self.brand)

class Fortuner(Toyotacar):
    def __init__(self,type):
        self.type = type
        print(self.type)

car1 = Fortuner("disel")
car1= Toyotacar("skoda")
car1.start()
