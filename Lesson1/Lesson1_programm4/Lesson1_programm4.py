sec=int(input())
d=sec//86400
sec%=86400
h=sec//3600
sec%=3600
m=sec//60
sec%=60
print (d,':',h,':',m,':',sec)