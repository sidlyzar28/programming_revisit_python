num=int(input("Enter a number to check if it's prime: "))
if num<=1:
    print("The number is not prime")
else:
    for i in range(2,num): 
        #for i in range(2,int(num**0.5)+1):->#optimized
        if num%i==0:
            print("The number is not prime")
            break
    else:
        print("The number is prime")