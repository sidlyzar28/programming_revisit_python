num=int(input("Enter a number: "))
temp=num
count=0

#counting digits:
while temp>0:
    temp=temp//10
    count+=1
#calulating sum of digits:
temp=num
sum=0
while temp>0:
    digit=temp%10
    sum=sum+digit**count
    temp=temp//10
if sum==num:
    print(num,"is an Armstrong number.")
else:
    print(num,"is not an Armstrong number.")
