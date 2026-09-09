text=input("Enter a string: ")
seen={} #create an empty dictionary to store characters and their counts
for char in text:
    if char in seen:
        print("The first repeating character is: ", char)
        break
    else:
        seen[char]=True