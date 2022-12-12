def f(A,B):
    while A>B:
        if A%2==1:
            print(A)
        A=A-1    
A=int(input())
B=int(input())
print(f(A,B))