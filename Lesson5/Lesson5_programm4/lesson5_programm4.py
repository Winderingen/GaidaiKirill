x=int(input())
y=int(input())
d=0
p=0
while p < y:
    p+=x
    x+=(x*0.1)
    d+=1
print(d)
