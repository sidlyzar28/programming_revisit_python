str=input("Enter a string to reverse:")
rev=""
for i in range(len(str)-1,-1,-1):
    rev=rev+str[i]
print("REversed string is:",rev)