l=0
sum=0
while True:
    n=int(input())
    if n==0:
        break
    l+=1
    sum+=n
print(sum/l)