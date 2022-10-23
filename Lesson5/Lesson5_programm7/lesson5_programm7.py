p=0
l=0
while True:
    n=int(input())
    if n==0:
        break
    if n>p:
        l+=1
    p=n
print(l-1)