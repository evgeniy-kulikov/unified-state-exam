""""""
"""
https://pro100ege.org/bank/
"""


""" 05 """
# 12098
def b3(n):
    r = ''
    while n:
        r += str(n % 3)
        n //= 3
    return r[::-1]

mn = 100**100
for n in range(1, 100000):
    r = b3(n)
    if not n % 3:
        r = r + r[-2:]
    else:
        sm = sum(int(i, 3) for i in r)
        r += b3(sm)
    r = int(r, 3)
    if r > 220:
        mn = min(mn, r)
print(mn)  # 222


""" 07 """
# 12114
"""
300 * 300 * i / 8 = 5 MB
150 * 150 * 4 = 512 KB   (2**4 = 16)

i = 5 * 1024 * 8 / 300**2
4 = 512 * 8 / 150**2

i =  (4 * (5 * 1024 * 8 / 300**2)) / (512 * 8 / 150**2)
"""
i = (4 * (5 * 1024 * 8 / 300**2)) / (512 * 8 / 150**2)  # 10
print(2**i)  # 1024


# 12108
"""
1280 * 960 * i / 8 / 1024 = 920 KB * 1.15
"""
i = 920*8*1024 * 1.15/(1280*960) # i = 7
print(2**int(i))  # 128




""" 24 """
# 12037
from re import *
reg = r'[1-9ABCD]{1}[0-9ABCD]*[02468AC]{1}'
max_n = 0
with open('add/24/24_4.txt') as f:
    for n in finditer(reg, f.read()):
        d = sum(int(i, 14) for i in n.group())
        max_n = max(max_n, d)
print(max_n) # 13223



""" 26 """
# 11336
with open('add/26/301_26.txt') as fl:
    n = int(fl.readline())
    d = sorted(map(int, fl), reverse=1)
    ls = [d[0]]
    for i in range(1, len(d) - 1):
        if ls[-1] - d[i] >= 3:
            ls.append(d[i])
print(len(ls))  # 2767
print(*ls[-1:])  # 51
# print(d[-8:])  # подстраховка


# 11326
with open('add/26/325_26.txt') as fl:
    busy, rows, cols = map(int, fl.readline().split())  # кол-во занятых мест, кол-во рядов, кол-во мест в ряду
    d = dict()
    for f in fl:
        row, col = map(int, f.split())
        d.setdefault(col, [0])
        d[col] += [row]

    res = [[0, 0]]  # ряд, кол-во своб. кресел перед выбранным местом
    for col in d:
        row = sorted(d[col])  # 0 + список занятых кресел в ряду (список этих рядов)
        tmp = row[0] - 2  # кол-во свободных кресел перед выбранным местом
        for i in range(1, len(row)):
            tmp = max(tmp, row[i] - row[i - 1] - 2)
            if tmp >= res[-1][-1]:
                if tmp > res[-1][-1]:
                    res = [[row[i] - 1, tmp]]  # row[i]-1   ряд для покупки
                else:
                    res.append([row[i] - 1, tmp])
# print(res)
print(*min(res, key=lambda x: x[0]))  # 68217 33508

