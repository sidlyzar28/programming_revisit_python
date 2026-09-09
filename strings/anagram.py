s1=input("EnTer the first string: ")
s2=input("Enter the second string: ")
if sorted(s1)==sorted(s2): 
    print("The two strings are anagrams.")
else:
    print("The two strings are not anagrams.")
##############################################
s1=input("Enter the first string: ")
s2=input("Enter the second string: ")
freq1={}
freq2={}
for ch in s1:
    if ch in freq1:
        freq1[ch]+=1
    else:
        freq1[ch]=1
for ch in s2:
    if ch in freq2:
        freq2[ch]+=1
    else:
        freq2[ch]=1
if freq1==freq2:
    print("Anagram")
else:
    print("Not Anagram")
    
    
    

























