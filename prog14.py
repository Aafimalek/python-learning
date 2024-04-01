nums = [10,20,30,40,50,60,70,80,90,100]
def length_list(lists):
    print(len(lists))

#length_list(nums)
def print_list(list):
    for item in list:
        print(item,end=" ")

#print_list(nums)


def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)

#fact(5)

def currency(a):
    a*=83
    print(a)

#currency(2)

def even_odd(a):
    if(a%2==0):
        print("even",a)
    else:
        print("odd",a)

even_odd(7)