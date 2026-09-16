n=int(input("Enter how many terms: "))
first=0
second=1
if n<=0:
    print("Please enter a positive integer.")
elif n==1:
    print("Fibonacci sequence upto",n,":")
    print(first)
else:
    print("Fibonacci sequence upto",n,":")
    print(first, second, end=" ")
    for _ in range(2, n):
        next_term = first + second
        print(next_term, end=" ")
        first = second
        second = next_term
         