n=int(input())
num=list(map(int,input().split()))
even=0
odd=0
for i in range(n):
    if num[i]%2==0:
        even=even+1
    else:
        odd=odd+1
print("No of even no:",even)
print("No of odd no:",odd)