""""""
"""
Task 14
Подготовка к ЕГЭ информатика
https://stepik.org/course/57248?auth=login
"""


""" 7.21 ЕГЭ Тренировка 14 """

# https://stepik.org/lesson/421052/step/1?auth=login&unit=410662
from string import digits, ascii_uppercase
def conv(n, base):
    alfa = digits + ascii_uppercase
    res = ''
    while n:
        res = alfa[n % base] + res
        n //= base
    return res

for el in range(4, 37):
    n = conv(325, el)
    if n[-1] == '1' and len(n) == 3:
        print(el, n)  # 9 401
        break
# 9 401
# 12 231
# 18 101


# https://stepik.org/lesson/421052/step/2?auth=login&unit=410662
for el in range(5, 37):
    if int('124', el + 1) - int('132', el) == 11:
        print(el)  # 6
        break


# https://stepik.org/lesson/421052/step/3?auth=login&unit=410662
n = 64 ** 115 + 8 ** 305 - 512
n = 8 ** 230 + 8 ** 305 - 8 ** 3
n = oct(n)
print(n.count('7'))  # 227


# https://stepik.org/lesson/421052/step/4?auth=login&unit=410662
n = ((9 * 5 ** 20 + 9) * 5 ** 19 + 9) * 5 ** 18 + 9
res = ''
while n:
    res = str(n % 5) + res
    n //= 5
# print(res)  # 14000000000000000000140000000000000000014000000000000000014
print(f"0 - {res.count('0')},1 - {res.count('1')},2 - {res.count('2')},3 - {res.count('3')},4 - {res.count('4')}")


# https://stepik.org/lesson/421052/step/5?auth=login&unit=410662
n = (2 * 343 ** 123 + 2401) * (3 * 343 ** 137 - 2401)
res = ''
while n:
    res = str(n % 7) + res
    n //= 7
print(res.count('6'))  # 407


# https://stepik.org/lesson/421052/step/6?auth=login&unit=410662
def fn(n):
    res = ''
    while n:
        res = str(n % 9) + res
        n //= 9
    return res

mn = 100000
mx = 0
for n in range(1, 100000):
    m = fn(n)
    if len(m) == 3 and m.count('3') and len(fn(n * 3)) == 3:
        mn = min(mn, n)
        mx = max(mx, n)
print(mn, mx)  # 84 237
print(fn(mn + mx))  # 386


# https://stepik.org/lesson/421052/step/7?auth=login&unit=410662
def fn(n):
    res = ''
    while n:
        res = str(n % 4) + res
        n //= 4
    return res

for n in range(1, 1000):
    m = 64 ** 11 - 4 ** 10 + 96 - n
    if sum(map(int, fn(m))) == 71:
        print(n)  # 16
        break


""" 7.22 ЕГЭ Тренировка 14 """
# https://stepik.org/lesson/615398/step/1?auth=login&unit=610935
print(f'{(4**2016 + 2**2018 - 6):b}'.count('1'))  # 2017


# https://stepik.org/lesson/615398/step/3?auth=login&unit=610935
alf = '0123456789abcdef'
for h in range(16):
    for k in range(8):
        if int(f'1{alf[h]}0', 16) == int(f'56{alf[k]}', 8):
            print(int(f'56{alf[k]}', 8))  # 368


# https://stepik.org/lesson/615398/step/4?auth=login&unit=610935
def f(n):
    s = ''
    while n:
        s = str(n % 5) + s
        n //= 5
    return s
res = 4 * 125**4 - 25**4 +9
print(f(res).count('4'))


# https://stepik.org/lesson/615398/step/6?auth=login&unit=610935
for n in range(6, 20):
    if int('214', n) == int('165', n+1):
        print(n)  # 8
        break



""" 7.23 ЕГЭ Тренировка 14 """
# https://stepik.org/lesson/797045/step/1?auth=login&unit=799874
# Хорошая задачка по условию!
a = '0123456789abcdefg'
res = []
for y in range(17):
    for x in range(15):
        r = int(f'123{a[x]}5', 15) + int(f'67{a[y]}9', 17)
        if not r % 131:
            res.append([a[y], r // 131])
res.sort()
if res: print(res[0][-1])  # 686


# https://stepik.org/lesson/797045/step/2?auth=login&unit=799874
from string import printable as p
res = []
for x in p[:22]:
    for y in p[:13]:
        r = int(f'{x}23{x}5', 22) - int(f'67{y}9{y}', 13)
        if not r % 57:
            res.append([int(f'{x}', 22) + int(f'{y}', 13), r // 57])
res.sort()
if res: print(res[0][-1])  # -2897  ...но принимается 25871
# res = [[6, -2897], [14, 25871], [15, 58773], [22, 54639], [30, 83407]]


# https://stepik.org/lesson/797045/step/3?auth=login&unit=799874
from string import printable as p
for x in p[:11]:
    for y in p[:11]:
        r = int(f'7{y}23{x}5', 25) + int(f'67{x}9{y}', 11)
        if not r % 131:
            print(r // 131)  # 552647

