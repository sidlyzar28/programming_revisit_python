text=input("Enter a string: ")
first=text[0]
last=text[-1]
print("First character is:",first)
print("Last character is:",last)
###################################

text=input("Enter a string: ")
first=None
last=None
for i in range(len(text)):
    if i==0:
        first=text[i]
   # if i==len(text)-1:
    #    last=text[i]
    else:
        last=text[i]
print("First character is:",first)
print("Last character is:",last)