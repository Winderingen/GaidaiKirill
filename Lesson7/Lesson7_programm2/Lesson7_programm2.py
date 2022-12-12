import random
from random import randint
def f(n):
    num = []
    s = 0
    for i in range(n):
        t = randint(1, 100)
        print(t)
        num.append(t)
        if num[-1] > 5:
            s += num[-1]
    print(s)
n=10
print(f(n))