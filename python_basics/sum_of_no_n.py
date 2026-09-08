n=int(input("Enter a number: "))
num=list(map(int,input("Enter numbers separated by space: ").split()))
print("Sum of the numbers is",sum(num))

#without using sum function
n=int(input("Enter a number: "))
num=list(map(int,input("Enter numbers separated by space: ").split()))
sum=0
for i in num:
    sum+=i
print("Sum of the numbers is",sum)