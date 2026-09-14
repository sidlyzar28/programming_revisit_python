n=int(input("Enter the number of elements in the list: "))
arr=list(map(int,input().split()))
seen={}
result=[]
for num in arr:
    if num not in seen:
        seen[num]=True
        result.append(num)
print("The list after removing duplicates while preserving order is:",*result)   