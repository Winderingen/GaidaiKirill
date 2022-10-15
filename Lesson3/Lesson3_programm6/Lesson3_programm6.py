def f(a1,b1,a2,b2): #сумма координат клеток различных цветов различна
    if (a1 + b1)%2==0 and (a2+b2)%2==0:
        print('цвет одинаков')
    elif (a1+b1)%2==1 and (a2+b2)%2==1:
        print('цвет одинаков')
    else:
        print('цвет различен')
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
print(f(a1,b1,a2,b2))