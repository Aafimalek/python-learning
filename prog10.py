nums=(1,4,9,16,25,36,49,64,81,100)
x=int(input("number u want to search: "))
index = 0
while index< len(nums):
    if(nums[index]==x):
        print("found at idx :",index)
        break
    index+=1 
else: 
        print("invalid no")
      


i=0
while i<=5:
    if(i==3):
        i+=1
        continue
    print(i)
    i+=1

    

    
    