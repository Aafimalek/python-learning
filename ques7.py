nums = [1,4,9,16,25,36,49,64,81,100]
x=int(input("enter element: "))
index=0
for el in nums:
    if(el==x):
     print("element found",nums[index])
     break
    index+=1

     
    #else:
     #print("element not found")
     