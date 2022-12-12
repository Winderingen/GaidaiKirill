def f(n):
    f=1
    s=0
    for i in range(1,n+1):
        f=f*i
        s=s+f
    print(s)    
n=int(input())
print(f(n))