n=int(input("Enter the number of elements in the list: "))
arr=list(map(int,input().split()))
smallest=second=None
for num in arr:
    if smallest is None or num<smallest:
        second=smallest
        smallest=num
    elif num!=smallest and (second is None or num<second):
        second=num
print("The second smallest distinct element in the list is:",second)