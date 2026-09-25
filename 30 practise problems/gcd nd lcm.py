a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
#GCD
i= a if a<b else b

while i>0:
    if a%i==0 and b%i==0:
        print("GCD of",a,"and",b,"is:",i)
        break
    i=i-1
    
#LCM
j=a if a>b else b

while j>0:
    if j%a==0 and j%b==0:
        print("LCM of",a,"and",b,"is:",j)
        break
    j=j+1