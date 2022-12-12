def f(n):
    i=2
    t=1
    while i<=n:
        i*=2
        t+=1
    print(t-1,i//2)    
n=int(input())
print(f(n))