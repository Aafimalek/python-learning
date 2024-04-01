class Car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("car started")
    
    @staticmethod
    def stop():
        print("car stopped")

class Toyotacar(Car): #inheritence 
    def __init__(self,name,type):
        self.name = name
        super().__init__(type)
        super().start()
        
        
car1 = Toyotacar("prius","electric")
print(car1.type)