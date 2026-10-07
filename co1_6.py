Names=input("Enter a names:").split()
count=0
for name in Names:
    count+=name.lower().count('a')
print("Number of a=",count)