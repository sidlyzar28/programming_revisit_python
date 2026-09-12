n=int(input("Enter the number of elements in the list: "))
arr=list(map(int,input().split()))
target=int(input("Enter the target sum: "))
freq={}
for i in range(n):
    comp=target-arr[i]
    if comp in freq:
        print("Indices of the two elements that add up to the target sum are:",freq[comp],i)
        break
    
    freq[arr[i]]=i
else:
    print("No two elements found that add up to the target sum.")