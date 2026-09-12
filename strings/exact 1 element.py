n=int(input("Enter the number of elements in the list: "))
arr=list(map(int,input().split()))
freq={}
for num in arr:
 freq[num]=freq.get(num,0)+1
for key in freq:
 if freq[key]==1:
  print("The first non-repeating element is:",key)
  break 
