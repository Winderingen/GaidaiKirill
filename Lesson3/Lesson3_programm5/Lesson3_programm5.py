def f(x,y,z):
    if x>y and x>z:
        print(x)
    if x>y and x<z:
        print(z)
    if x<y and z<y:
        print(y)
x=int(input())
y=int(input())
z=int(input())
print( f(x,y,z))