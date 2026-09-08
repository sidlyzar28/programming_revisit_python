text=input("Enter a string: ")
rev=""
for i in range(len(text)-1,-1,-1):
    rev+=text[i]
if text==rev:
        print("The string is a palindrome")
else:
        print("The string is not a palindrome")
############
text=input("Enter a string: ")
if text==text[::-1]:
        print("The string is a palindrome")
else:
        print("The string is not a palindrome")