str=input("Enter a string: ")
length=len(str)
if length>2:
    if str[-3:]=="ing":
        
        print(str+"ly")
    else:
        print(str+"ing")

else:
    print("wrong input")        