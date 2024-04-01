class Person:
    name = "anonymous"

    #def changename(self,name):
       # self.name = name
        #Person.name = name 
        #self.__class__.name = "malek"
    @classmethod
    def changename(cls,name):
        cls.name = name


p1 = Person()
p1.changename("aafi")
print(p1.name)
print(Person.name)