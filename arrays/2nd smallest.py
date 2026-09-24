n=int(input())
arr=list(map(int,input().split()))
smallest=second=999999
for i in arr:
    if i < smallest:
        second=smallest
        second=i
    elif i<second and i!=smallest:
        second=i
print("Second smallest:",second)