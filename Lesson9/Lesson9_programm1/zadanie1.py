from random import randint


def Matrica():
    n = randint(1,4)
    matrica = [[randint(0,9) for i in range(n)] for u in range(n)]
    stolbi = []
    
    for i in range(len(matrica)):
        for x in range(len(matrica[i])):
            stolbi.append(matrica[i][x])
    a = [stolbi[i::n] for i in range(n)]
    print('значения в столбцах')
    for y in a:
        print(min(y))
    print('значения в строках')
    for d in matrica:
        print(max(d))
Matrica()


