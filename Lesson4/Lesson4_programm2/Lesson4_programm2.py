def f(A,B):
    if A<B:
        while A<B:
            print(A)
            A+=1
        print(B)
    else:
        while B<A:
            print(A)
            A -=1
        print(A)    
A=int(input())
B=int(input())
print(f(A,B))
