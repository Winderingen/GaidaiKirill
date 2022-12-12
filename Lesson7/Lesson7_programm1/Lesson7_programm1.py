def f(n):
    import random 
    from random import randint
    mas=[]
    for value in range(n):
        value=randint(1,100)
        mas.append(value)
    element=max(mas)
    print('Наибольший элемент массива:',element)
    b=0
    m=0
    r=0
    for i in mas:
        if i>element:
            print(i,">",element)
            b+=1
        elif i<element:
            print(i,"<",element)
            m+=1
        elif i==element:
            print(i,"==",element)
            r+=1
    print("элементов >",b)
    print("элементов <",m)
    print("элементов ==",r)
n=10
print(f(n))