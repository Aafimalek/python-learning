class Student:
    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks
    @staticmethod
    def college_name():
        print("L.D. COLLEGE OF ENGINEERING")

    def get_avg(self):
        sum=0
        for val in self.marks:
            sum += val
        print("hi",self.name,"ur marks is:",sum/3) 


s1 = Student("aafi malek",[92,95,99])
s1.get_avg()
s1.college_name()
