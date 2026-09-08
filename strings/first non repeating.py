text=input("Enter a string: ")
freq={}
for char in text:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
for char in text:
    if freq[char]==1:
        print("First non-repeating character is:",char)
        break