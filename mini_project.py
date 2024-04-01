import random

target = random.randint(1,100)

while True:
    userchoice =(input("guess the target or Quit(Q):"))
    if(userchoice=="Q"):
        print("you Quit")
        break
    userchoice = int(userchoice)
    if(userchoice==target):
        print("correct guess")
        break
    elif(userchoice<target):
        print("number small! take a bigger guess")
    else:
        print("number too large! take a smaller guess")
    

print("-----game over------")


