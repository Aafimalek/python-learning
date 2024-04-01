collection ={1,2,3,"hello",19}
print(type(collection))
print(collection)
#no duplicate values it ignore it 
ct = set() #to create empty set otherwise it will be like dictionary 
collection.add(92)
collection.remove(3)
collection.clear()
collection.pop()
print(collection)
#u can add immutable items as string,tuple etc but not mutable items as lists
set2 = {"aafikhan malek",19,"hello",3}
print(collection.union(set2))
print(collection.intersection(set2))

