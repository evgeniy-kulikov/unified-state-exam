""" https://kompege.ru/task """

"""
352
1332 
9360 9774
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


# 1332 Danov2101 (Уровень: Средний)
for n in range(3, 1000, 2):
    b = f'{n:b}'
    b = b[0] + ''.join(['01'[i=='0'] for i in b[1:]])
    if int(b, 2) + n > 99:
        print(n)  # 65
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


# 9774 Основная волна 20.06.23 (Уровень: Средний)
def f(n, b=3):
    r = ''
    while n:
        r = str(n % b) + r
        n //= b
    return r

res = 10**10
for n in range(1, 10000):
    b = f(n)
    if n % 3:
        b += f(n % 3 * 5)
    else:
        b += b[-2:]
    r = int(b, 3)
    if r > 133:
        res = min(res, r)
print(res)  # 141





