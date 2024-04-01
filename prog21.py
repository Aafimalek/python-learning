try:
    a = int(input("enter ur no:"))
    print(a+3)
except Exception as e:
    print("some error occured")
    print(e)
finally:
    print("end")