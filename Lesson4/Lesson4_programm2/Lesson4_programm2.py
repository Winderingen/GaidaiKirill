A=int(input())
B=int(input())
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