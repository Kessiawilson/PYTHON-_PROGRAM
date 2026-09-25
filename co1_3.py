#positive numbers
n = [-10,15,-3,8,0,22,-5]
positive_numbers = [x for x in n if x>0]
print("positive numbers:",positive_numbers)

#square of N number
n=5
squares = [x*x for x in range(1,n+1)]
print("square of n numbers:",squares)

#list of vowels
word = "python programming"
vowels = [char for char in word if char in "aeiousAEIOUS"]
print("vowels in the word:",vowels)

#list ordinal Value
word = "hello"
ordinal_values=[ord(x) for x in word]
print("ordinal value:",ordinal_values)