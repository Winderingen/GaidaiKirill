import math
def s(p1, p2):
    boob = math.sqrt(p1 * (p1 - ab) * (p1 - bc) * (p1 - ac)) + math.sqrt(p2 * (p2 - da) * (p2 - cd) * (p2 - ac))
    return boob
ab = int(input('Введите длину стороны ab'))
bc = int(input('Введите длину стороны bc'))
cd = int(input('Введите длину стороны cd'))
da = int(input('Введите длину стороны da'))
ac = int(input('Введите длину диагонали ac'))
p1 = (ab + bc + ac) // 2
p2 = (da + cd + ac) // 2
print(s(p1, p2))