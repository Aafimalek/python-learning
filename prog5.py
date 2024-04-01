info = {
"subjects" : ["python","c","java"],
 "topics" : ("dictionaries","set"),
    "name" : "aafi",
    "age" : 20,
    "marks" : 95,
}
null_dict = {}
info["name"] = "malek"
info["surname"] = "khan"
print(info)
print(type(info))
print(info["name"])
#nested dictionary 
student = {
    "name" : "AAFIKHAN MALEK",
    "subjects": {
        "phy" : 82,
        "chem" :98,
        "math" : 78
    }
}
#print(student)
#print(student["subjects"])
#print(student["subjects"]["chem"])
#print(student.keys())
#print(student.values())
#print(student.items())
print(student.get("subjects"))
student.update({"city":"ahmedabad"})
print(student)