num=int(input("Enter a number to check palindrome:"))
rev=0
temp=num
if num==0:
    rev=0
    print("The number is a palindrome")
else:
    while num>0:
        digit=num%10
        rev=rev*10+digit
        num=num//10
    if rev==temp:
        print("The number is a palindrome")
    else:
        print("The number is not a palindrome")