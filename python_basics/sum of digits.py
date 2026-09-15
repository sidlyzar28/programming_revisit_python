num=int(input("Enter a number: "))
sum=0
if num==0:
    sum=0
else:
    while num>0:
        digit=num%10
        sum=sum+digit
        num=num//10
print("Sum of digits is:",sum)