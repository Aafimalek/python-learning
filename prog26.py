#multiple inheritance 
class A:
    varA = "wc to class A"

class B:
    varB = "wc to class b"

class C(A,B):
    varC = "wc to class c"

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)