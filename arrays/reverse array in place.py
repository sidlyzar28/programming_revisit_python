n=int(input())
num=list(map(int,input().split()))
rev=[]
for i in range(n-1,-1,-1):
    rev.append(num[i])
print("reversed array:",rev)