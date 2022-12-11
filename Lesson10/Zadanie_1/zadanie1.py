
fil = open(r'C:\Users\dirpu\Desktop\demichev_project\Gaidai-K.A Y-224_vvod1.txt')

file_dlia_w = open(r'C:\Users\dirpu\Desktop\demichev_project\Gaidai-K.A Y-224_vivod1.txt', 'w+',encoding = 'utf-8')
O = fil.readlines(5)
M = fil.readlines(5)
P = fil.readlines(5)
q1 = [int(x) for x in O]
q2 = [int(x) for x in M]
q3 = [int(x) for x in P]
a = [q1,q2,q3]
def Matrica():
    stolbi = []
    
    for i in range(len(a)):
        for x in range(len(a[i])):
            stolbi.append(a[i][x])
    A = [stolbi[i::3] for i in range(3)]

    file_dlia_w.write('значения в столбцах')
    file_dlia_w.write('\n')
    for y in A:

        file_dlia_w.write(str(min(y)))
        file_dlia_w.write('\n')
    file_dlia_w.write('значения в строках')
    file_dlia_w.write('\n')
Matrica()
file_dlia_w.close()
  