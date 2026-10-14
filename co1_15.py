list1=input("enter color-list:").split()
list2=input("enter color-list:").split()
result=[x for x in list1 if x not in list2]
print(result)
