fil = open(r'C:\Users\dirpu\Desktop\demichev_project\Gaidai-K.A Y-224_vvod2.txt')

file_dlia_w = open(r'C:\Users\dirpu\Desktop\demichev_project\Gaidai-K.A Y-224_vivod2.txt', 'w+')
O = fil.readlines(9)
M = fil.readlines(9)
P = fil.readlines(9)
R = fil.readlines(9)
Q = fil.readlines(9)
q1 = [int(x) for x in O]
q2 = [int(x) for x in M]
q3 = [int(x) for x in P]
q4 = [int(x) for x in R]
q5 = [int(x) for x in Q]
a = [q1,q2,q3,q4,q5]
def Matrica(): 
    for i in a:
        file_dlia_w.write(str(i))
        file_dlia_w.write('\n')
 
    diagonal = sum(a, [])
    max1 = max(diagonal[::6])
    max2 = max(diagonal[4::4][:5])
    if max1 > max2:
        i1 = j1 = diagonal[::6].index(max1)
    else:
        i1 = diagonal[4::4][:5].index(max2)
        j1 = 4 - i1
    a[5//2][5//2], a[i1][j1] = a[i1][j1], a[5//2][5//2]
    file_dlia_w.write('\n')
 
    for i in a:
        file_dlia_w.write(str(i))
        file_dlia_w.write('\n')
Matrica()