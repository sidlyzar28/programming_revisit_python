n=int(input())
num=list(map(int,input().split()))
pos=0
neg=0
for i in range(n):
    if num[i]>0:
        pos=pos+1
    else:
        neg+1
print("positive",pos)
print("negative",neg)