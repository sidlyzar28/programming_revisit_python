n=int(input("Enter the number of elements:"))
num=list(map(int,input().split()))
sum=0
for i in range(n):
     sum=sum+num[i]
print("Sum of the elements of the array is:",sum)