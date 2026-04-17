""" https://kompege.ru/task """

"""
352
9360
"""



# 352 (Уровень: Базовый)
for n in range(1, 1000):
    b = f'{n:b}'
    if n % 2:
        b += '0'
    else:
        b = '1' + b
    b += '10'[b.count('1') % 2]
    if int(b, 2) > 228:
        print(n)
        break


# 9360 Джобс 10.06.23 (Уровень: Базовый)
res = []
for n in range(1, 1000):
    b = f'{n:b}'
    if n % 3:
        b += f'{n % 3 * 5:b}'
    else:
        b += '010'
    r = int(b, 2)
    if r > 300 and not r % 2:
        res.append((r, n))
res.sort()
print(res[0][1])  # 39