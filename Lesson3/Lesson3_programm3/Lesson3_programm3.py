n=int(input())
if n>=60:
    h=n//60
    n=n%60
    if h>=24:
        h=h%24
print(h,':',n)