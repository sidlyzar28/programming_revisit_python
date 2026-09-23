n=int(input())
num=list(map(int,input().split()))
x=int(input("Enter element to search:"))
found=False 
for i in range(n):
    if num[i]==x:
        found=True
        break
if found:
    print(x,"found")
else:
    print(x,"not found")