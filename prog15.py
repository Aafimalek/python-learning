#recursive function 
def show(n):
    if(n==0):
        return 0
    return show(n-1)+n
  
sum = show(5)
print(sum)


#recusrive factorial 
def fact(n):
    if(n==0 or n==1):
        return 1
    #return n * fact(n-1)
    
#print(fact(4))

def print_list(list,i=0):
    if(i==len(list)):
        return 
    print(list[i])
    print_list(list,i+1)

nums = [1,2,3,4,5,6,7,8,9,10]
print_list(nums)





