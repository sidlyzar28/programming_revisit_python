text=input("Enter a string: ")
rev=""
for i in range(len(text)-1,-1,-1):
    rev+=text[i]
print("Reverse of the string is:",rev)
print("Reverse of the string is using slicing:",text[::-1])