def f(n):
    s=0
    for i in range(1,n+1):
        s+=i**3
    print(s)    
n=int(input())
print(f(n))