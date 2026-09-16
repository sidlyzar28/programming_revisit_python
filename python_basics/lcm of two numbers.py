a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
i= a if a>b else b

while i>0:
    if i%a==0 and i%b==0:
        print("LCM of",a,"and",b,"is:",i)
        break
    i=i+1