n=int(input())
num=list(map(int,input().split()))
tot=0
for i in range(n):
    tot=tot+num[i]
avg=tot/n
print("the average is:",avg)