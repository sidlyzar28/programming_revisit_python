n1=int(input())
arr1=list(map(int,input().split()))
n2=int(input())
arr2=list(map(int,input().split()))
set1={}
for num in arr1:
    set1[num]=True
for num in arr2:
    if num in set1:
        print(num, end=" ")