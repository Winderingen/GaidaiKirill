def f(n):
    t=1
    for i in range(1,n+1):
        t=t*i
    print(t)    
n=int(input())
print(f(n))