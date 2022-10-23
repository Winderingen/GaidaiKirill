a=int(input())
n=1
while n <= a:
    n = n + 1
    if a % n == 0:
        print(n)
        break