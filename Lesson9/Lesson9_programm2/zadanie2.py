

from random import randint
def Matrica():  
    N = randint(1,5)
    if N % 2 == 0:
        print('Число четное :(')
    else:
        b = [[randint(0,9) for i in range(N)] for j in range(N)]
        for i in b:
            print(i)
        print()
 
        diagonal = sum(b, [])
        max1 = max(diagonal[::N+1])
        max2 = max(diagonal[N-1::N-1][:N])
        if max1 > max2:
            i1 = j1 = diagonal[::N+1].index(max1)
        else:
            i1 = diagonal[N-1::N-1][:N].index(max2)
            j1 = N - 1 - i1
        b[N//2][N//2], b[i1][j1] = b[i1][j1], b[N//2][N//2]
 
        for i in b:
            print(i)
Matrica()