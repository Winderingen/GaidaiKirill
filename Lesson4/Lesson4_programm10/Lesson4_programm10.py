n=int(input())
k=int(input())
f1=0
f2=1
s=0
sum=0
for i in range(0,n+k-1):
    if i>=n-1:
        sum=sum+f1    
    s=f1+f2
    f1=f2
    f2=s    
print(sum)