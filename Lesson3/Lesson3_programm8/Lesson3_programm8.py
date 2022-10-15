def f(x,y,z):
    if x==y and x==z:
        print('3')
    elif x==y or x==z or y==z:
        print('2')
    else:
        print('0')
x=int(input())
y=int(input())
z=int(input())
print(f(x,y,z))