class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("aafi")
print(s1.name)
#del keyword 
del s1.name
print(s1.name)