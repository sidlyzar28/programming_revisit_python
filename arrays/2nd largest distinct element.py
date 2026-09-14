n=int(input())
arr=list(map(int,input().split()))
largest=second=None
for num in arr:
    if largest is None or num>largest:
        second=largest
        largest=num
    elif num!=largest and (second is None or num>second):
        second=num
print("The second largest distinct element in the list is:",second)