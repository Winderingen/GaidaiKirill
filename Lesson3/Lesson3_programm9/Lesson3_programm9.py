def f(n,m,k):
    if (k < m * n) and ((k % m == 0) or (k % n == 0)):
        print('да')
    else:
        print('нет')
n=int(input())
m=int(input())
k=int(input())
print(f(n,m,k))