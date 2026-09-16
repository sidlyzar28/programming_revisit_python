a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
i= a if a<b else b

while i>0:
    if a%i==0 and b%i==0:
        print("GCD of",a,"and",b,"is:",i)
        break
    i=i-1