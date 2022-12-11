def posl():
    u = int(input())
    if u == 0:
        return int()
    return max([u, posl()])
print(posl())