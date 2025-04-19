"""
Task 25
ЕГЭ Питоныч
https://stepik.org/course/100138
"""

# https://stepik.org/lesson/559890/step/5?unit=553935
# поиск простого числа
def fn(n):
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True
[print(n) for n in range(101, 150) if fn(n)]


# https://stepik.org/lesson/559890/step/8?unit=553935
def fn(n):
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True

cnt = 0
for n in range(4331641, 4331714):
    if fn(n):
        cnt += 1
        print(cnt, n)


# https://stepik.org/lesson/559890/step/10?unit=553935
def fn(n):
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True

for n in range(4331641, 4331814):
    if fn(n) and str(n)[-1] == '3':
        print(n)


# https://stepik.org/lesson/559891/step/3?unit=553936
def fn(n):
    res = set()
    for i in range(1, int(n ** 0.5) + 1):
        if not n % i:
            res.add(i)
            res.add(n // i)
    return sorted(res)

for n in range(123123, 123154):
    if len(fn(n)) == 4:
        print(n)


# https://stepik.org/lesson/559891/step/4?unit=553936
def fn(n):
    d = set()
    for i in range(1, int(n ** 0.5) + 1):
        if not n % i:
            d.add(i)
            d.add(n // i)
    return len(d) == 4, d

for n in range(123123, 123154):
    res = fn(n)
    if res[0]:
        print(*sorted(res[1]))


# https://stepik.org/lesson/559891/step/5?unit=553936
def fn(n):
    d = set()
    for i in range(1, int(n ** 0.5) +1):
        if not n % i:
            d.add(i)
            d.add(n // i)
    return len(d) == 4

for n in range(123153, 123124, -1):
    if fn(n):
        print(n)


# https://stepik.org/lesson/559891/step/6?unit=553936
def fn(n):
    d = set()
    for i in range(1, int(n ** 0.5) +1):
        if not n % i:
            d.add(i)
            d.add(n // i)
    return sorted(d, reverse=True)

for n in range(123123, 123154):
    res = fn(n)
    if len(res) == 4:
        print(*res)


# https://stepik.org/lesson/559891/step/9?unit=553936
def fn(n):
    d = set()
    for i in range(2, int(n ** 0.5) +1):
        if not n % i:
            d.add(i)
            d.add(n // i)
    return len(d) == 6, d

for n in range(12312320, 12312351):
    res = fn(n)
    if res[0]:
        print(*sorted(res[1])[-2:])


# https://stepik.org/lesson/559891/step/10?unit=553936
def fn(n):
    d = set()
    for i in range(1, int(n ** 0.5) + 1):
        if not n % i:
            d.add(i)
            d.add(n // i)
    res = [i for i in d if not i % 2]
    if len(res) == 4:
        return sorted(res)

for n in range(123123, 123151):
    res = fn(n)
    if res:
        print(*res)

# https://stepik.org/lesson/559891/step/12?unit=553936
from math import prod
def fn(n):
    d = set()
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            d.add(i)
            d.add(n // i)
    if len(d) == 4:
        return prod(d), sorted(d, reverse=True)

ls = []
for n in range(174457, 174521):
    res = fn(n)
    if res:
        ls.append(res)
ls.sort(key=lambda x: -x[0])
[print(*i[1]) for i in ls]


# https://stepik.org/lesson/877936/step/2?unit=882403
def fn(n):
    d = set()
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            d.add(i)
            d.add(n // i)
    if d:
        return max(d) - min(d)

cnt = 4
for n in range(600_000, 1_000_000):
    res = fn(n)
    if res and res % 10 == 6:
        print(n, res)
        cnt -= 1
    if not cnt:
        break

# Короче
def fn(n):
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return abs(i - n // i)

cnt = 4
for n in range(600_000, 1_000_000):
    res = fn(n)
    if res and res % 10 == 6:
        print(n, res)
        cnt -= 1
    if not cnt:
        break


# https://stepik.org/lesson/1401988/step/2?unit=1418958
def fn(n):
    d = set()
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            d.add(i)
            d.add(n // i)
    ls = [k for k in d if all([str(k)[-2:] == '17', k != 17, k != n])]
    if ls:
        return min(ls)

cnt = 6
for n in range(600_000, 1_000_000):
    res = fn(n)
    if res:
        print(n, res)
        cnt -= 1
    if not cnt:
        break


# https://stepik.org/lesson/559892/step/2?unit=553937
def fn(n):
    d = set()
    for i in range(1, int(n**0.5 + 1)):
        if not n % i:
            d.add(i)
            d.add(n // i)
    return sorted(d)

for i in range(123456, 345679):
    # число, которое является квадратом другого числа, имеет нечетное количество делителей
    # Короче: если квадратный корень числа не имеет дробной части, то это число имеет нечетное количество делителей
    if i**0.5 == int(i**0.5):
        res = fn(i)
        if len(res) == 5:
            print(*res)


# https://stepik.org/lesson/559892/step/7?unit=553937
def fn(n):
    d = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            d.add(i)
            d.add(n // i)
    return d

for i in range(167000, 190001):
    if i**0.5 == int(i**0.5):
        res = sum(fn(i))
        if res > 250000:
            print(i, res)


# https://stepik.org/lesson/879914/step/4?unit=884462
def fn(n):
    if n == 1: return False
    for i in range (2, int(n**0.5) + 1):
        if not n % i:
            return False
    return True

cnt = 5
for i in range(100_000, 10_000_000):
    if all([fn(i), str(i)[0] + str(i)[-1] == '11']):
        print(i)
        cnt -= 1
    if not cnt:
        break


# https://stepik.org/lesson/879914/step/7?unit=884462
def simple(n):
    if n == 1: return False
    for i in range (2, int(n**0.5) + 1):
        if not n % i:
            return False
    return True

def dv(n):
    d = set()
    for i in range(2, int(n ** 0.5 + 1)):
        if not n % i:
            d.add(i)
            d.add(n // i)
    return d

cnt = 7
for i in range(650_000, 10_000_000):
    d = dv(i)
    if len([k for k in d if simple(k)]) == 5:
        print(i)
        cnt -= 1
    if not cnt:
        break


# https://stepik.org/lesson/879914/step/9?unit=884462
def simple(n):
    if n == 1: return False
    for i in range (2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True

def dv(n):
    d = set()
    for i in range(2, int(n ** 0.5 + 1)):
        if not n % i:
            d.add(i)
            d.add(n // i)
    return d

cnt = 6
for i in range(650_000, 10_000_000):
    d = dv(i)
    r = sum([k for k in d if simple(k)])
    if str(r)[-2:] == '15':
        print(i, r)
        cnt -= 1
    if not cnt:
        break


"""маски"""
# https://stepik.org/lesson/870004/step/2?unit=874178
s = '0123456789'
for i in s:
    for k in s:
        res = '1' + i +'34567' + k + '9'
        if not int(res) % 19:
            print(res, int(res) // 19)


# https://stepik.org/lesson/870004/step/7?unit=874178
# 123*567?
for n in range(0, 10 ** 9 + 1, 172):
    s = str(n)
    if all([s[:3] == '123', s[-4:-1] == '567']):
        print(s, int(s) // 172)


# https://stepik.org/lesson/870004/step/10?unit=874178
# ?5*5*?4
cnt = 5
for n in range(0, 1_000_000, 3 * 8):
    s = str(n)
    if len(s) >= 5:
        if all([s[1] == '5', '5' in s[2:-2], s[-1] == '4']):
            print(s)
            cnt -= 1
    if not cnt:
        break


# https://stepik.org/lesson/870004/step/10?unit=874178
# ?5*5*?4
# НОВОЕ РЕШЕНИЕ
from fnmatch import fnmatch
cnt = 5
for n in range(0, 1_000_000, 3 * 8):
    if fnmatch(str(n), '?5*5*?4'):
        print(n)
        cnt -= 1
        if not cnt:
            break

# ручной подход
cnt = 5
for n in range(0, 1_000_000, 3 * 8):
    s = str(n)
    if len(s) >= 5:
        if all([s[1] == '5', '5' in s[2:-2], s[-1] == '4']):
            print(s)
            cnt -= 1
    if not cnt:
        break


# https://stepik.org/lesson/870004/step/12?unit=874178
from fnmatch import fnmatch

for n in range(0, 10 ** 9, 172):
    if fnmatch(str(n), '123*567?'):
        print(n, n // 172)


# https://stepik.org/lesson/871176/step/2?unit=875447
from fnmatch import fnmatch

def nok(a, b):
    mult = a * b
    while b:
        a, b = b, a % b
    return mult // a

def dv(n):
    d = set()
    for i in range(1, int(n ** 0.5 + 1)):
        if not n % i:
            d.add(i)
            d.add(n // i)
    return sum(d)

step = nok(nok(6, 7), 8)  # 168
msk = '?8*8*?8'
cnt = 6

for n in range(0, 10 ** 6, step):
    if fnmatch(str(n), msk) and not n % step:
        print(n, dv(n))
        cnt-= 1
    if not cnt:
        break

# https://stepik.org/lesson/871176/step/5?unit=875447
from fnmatch import fnmatch

def nok(a, b):  # наименьшее общее кратное
    mult = a * b
    while b:
        a, b = b, a % b
    return mult // a

def dv(n):  # делители числа
    d = set()
    for i in range(1, int(n ** 0.5 + 1)):
        if not n % i:
            d.add(i)
            d.add(n // i)
    return sum(d)

num_div = nok(nok(4, 5), 6)  # 60
msk = '?1*2*?0'
cnt = 5
ls = []
n_start = 0
n_start = 10**8 // num_div * num_div  # 99999960  - ближайшее к 10**8 число делящееся на 60 без остатка

for n in range(n_start, 0, -60):
    if fnmatch(str(n), msk):
        ls.append((n, dv(n)))
        cnt -= 1
    if not cnt:
        break

ls.sort(key=lambda x: x[0])
[print(x[0], x[1]) for x in ls]



# https://stepik.org/lesson/871176/step/7?unit=875447
from fnmatch import fnmatch

def dv(n):
    d = set()
    for i in range(1, int(n ** 0.5 + 1)):
        if not n % i:
            d.add(i)
            d.add(n // i)
    return sum(i for i in d if not i % 2)

n_start = 10**7 // 223 * 223  # 9999989 - ближайшее к 10**7 число делящееся на 223 без остатка
cnt = 5
ls = []
msk = '23?4*'

for n in range(n_start, 0, -223):
    if fnmatch(str(n), msk):
        ls.append((n, dv(n)))
        cnt -= 1
    if not cnt:
        break

ls.sort(key=lambda x: x[0])
[print(x[0], x[1]) for x in ls]


# https://stepik.org/lesson/871176/step/11?unit=875447
from fnmatch import fnmatch

msk = '1[02468]2??[13579]?'
n_start = 10**6 // 2023 * 2023  # 999362
for n in range(n_start, 2_000_000, 2023):
    if fnmatch(str(n), msk):
        print(n, n // 2023)


# https://stepik.org/lesson/871176/step/14?unit=875447
alfa = '0123456789ABCDEF'
dv = int('AC', 16)
for i in alfa:
    for k in alfa:
        num = int(f'2{i}ABC{k}ABC', 16)
        if not num % dv:
            print(num, num // dv)

