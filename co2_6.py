s=input("enter a string:")
freq={}
for char in s:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
    print("charcter frequancy :")
    for char, count in freq.items():
        print(char, ":", count)