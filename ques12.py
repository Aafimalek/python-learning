with open("practice.txt","r") as f:
    data = f.read()
    word = "learning"
    if(data.find(word)!=-1):
        print("found")