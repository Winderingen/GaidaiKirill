def f(a,b):
    while a!=0 and b!=0:
        if a>b:
            a=a%b
        else:
            b=b%a
    return a+b
def d(a,b):
    nok=a*b/f(a,b)
    return nok
a=int(input())
b=int(input())
print(d(a,b))
print(f(a,b))