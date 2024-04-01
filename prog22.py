class Student:
    college_name = "ld college"#class.attr
    def __init__(self,name,marks):
        self.name = name #obj.attr
        self.marks = marks
    
    def hello(self):
        print("welcome student,",self.name)

    def get_marks(self):
        return self.marks

s1 = Student("aafi malek",99)
s1.hello()
print(s1.get_marks())
print(s1.college_name)





