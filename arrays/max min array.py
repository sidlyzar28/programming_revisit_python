n=int(input("Enter the number of elements in the list:"))
num=list(map(int,input().split()))
max_num=num[0]
min_num=num[0]
for i in range(1,n):
    if num[i]>max_num:
        max_num=num[i]
    if num[i]<min_num:
        min_num=num[i]
print("The maximum number in the list is:",max_num)
print("The minimum number in the list is:",min_num)



    