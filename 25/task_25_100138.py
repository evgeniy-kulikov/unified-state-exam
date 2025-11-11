"""
Task 25
ЕГЭ Питоныч
https://stepik.org/course/100138
"""

""" 23.1 Поиск простых чисел """
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


""" 23.2 Поиск делителей чисел """
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


""" 23.3 Решение задач. Часть 1 """
# https://stepik.org/lesson/877936/step/2?unit=882403
def fn(n):
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return abs(i - n // i)
cnt = 4
for n in range(600_000, 600_500):
    res = fn(n)
    if res and res % 10 == 6:
        print(n, res)
        cnt -= 1
    if not cnt:
        break

# https://stepik.org/lesson/877936/step/3?unit=882403
def fn(n):
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return i + n // i  # сразу находим минимальный и максимальный делитель числа
cnt = 0
for n in range(900_000, 900_500):
    res = fn(n)
    if res and res % 10 == 5:
        print(n, res)
        cnt += 1
    if cnt == 6:
        break


# https://stepik.org/lesson/877936/step/4?unit=882403
def fn(num):
    for i in range(2, int(num**0.5 + 1)):
        if not num % i:
            return i**2 + (num // i)**2
cnt = 0
for n in range(750_000, 800_000):
    res = fn(n)
    if res and res % 10 == 2:
        cnt += 1
        print(n, res)
    if cnt == 5: break


# https://stepik.org/lesson/877936/step/5?unit=882403
def fn(n):
    d = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            d.add(i)
            d.add(n // i)
    if d: return sum(d) // len(d)

cnt = 5
for i in range(1_200_000, 1_200_200):
    res = fn(i)
    if res and res % 10 == 3:
        cnt -= 1
        print(i, res)
    if not cnt: break


# https://stepik.org/lesson/877936/step/6?unit=882403
def fn(n):
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            return i + n // i

cnt = 5
for i in range(800_000, 800_200):
    res = fn(i)
    if res and res % 10 == 4:
        cnt -= 1
        print(i, res)
    if not cnt: break


# https://stepik.org/lesson/877936/step/9?unit=882403
def fn(n):
    d = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            d.add(i)
            d.add(n // i)
    if len(d) >= 3:
        m = sorted(d)[:3]
        return m[0] * m[1] * m[2], m[2]

cnt = 5
for i in range(400_000_000, 400_005_000):
    if fn(i):
        m, mx = fn(i)
        if m % 100 == 15 and m <= i:
            cnt -= 1
            print(i, m, mx)
    if not cnt: break


# https://stepik.org/lesson/877936/step/10?unit=882403
from math import prod
def fn(n):
    d = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            d.add(i)
            d.add(n // i)
    if len(d) >= 4:
        m = sorted(d)[:4]
        return prod(m), m[-1]

cnt = 6
for i in range(300_000_000, 300_010_000):
    if fn(i):
        m, mx = fn(i)
        if m % 100 == 19 and m <= i:
            cnt -= 1
            print(m, mx)
    if not cnt: break


# https://stepik.org/lesson/877936/step/12?unit=882403
def fn(n):
    d = set()
    for i in range(1, int(n**0.5 + 1)):
        if not n % i:
            d.add(i)
            d.add(n // i)
    ls = [i for i in d if not i % 2]
    if len(ls) == 4:
        return sorted(ls)[-2:]
# У нечетного числа не может быть четных делителей.
for i in range(150000, 150101, 2):
    m = fn(i)
    if m:
        print(*m)



""" 23.4 Решение задач. Часть 2 """
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


# https://stepik.org/lesson/1401988/step/3?unit=1418958
def fn(n):
    d = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            d.add(i)
            d.add(n // i)
    ls = [i for i in d if i % 100 == 25 and i != 25]
    if len(ls): return max(ls)

cnt = 6
for i in range(700_001, 700_500):
    m = fn(i)
    if m:
        print(i, m)
        cnt -= 1
    if not cnt:
        break


# https://stepik.org/lesson/1401988/step/4?unit=1418958
def fn(n):
    d = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            d.add(i)
            d.add(n // i)
    ls = [i for i in d if i % 10 == 9 and i != 9]
    if len(ls): return min(ls)

cnt = 5
for i in range(800_001, 800_100):
    m = fn(i)
    if m:
        print(i, m)
        cnt -= 1
    if not cnt:
        break



""" 23.5 Поиск чисел с нечетным количеством делителей """
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



""" 23.6 Простые числа. Часть 2 """
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


# https://stepik.org/lesson/879914/step/11?unit=884462
from math import prod
def n_div(n):
    d = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            d.add(i)
            d.add(n // i)
    return d

def pr(n):
    for i in range(2, int(n ** 0.5 + 1)):
        if not n % i: return 0
    return 1

ls = []
for i in range(123_456, 234_568):
    sp = [i for i in n_div(i) if pr(i)]
    if len(sp) == 5 and prod(sp) == i:
            ls.append(i)
print(len(ls), min(ls))  # 1685 123510


# https://stepik.org/lesson/879914/step/14?unit=884462
def n_div(n):
    d = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            d.add(i)
            d.add(n // i)
    return d

def pr(n):
    for i in range(2, int(n ** 0.5 + 1)):
        if not n % i: return 0
    return 1

cnt = 5
for i in range(650_001, 650_100):
    d = n_div(i)
    if d and pr(max(d)):
        print(i, max(d))
        cnt -= 1
    if not cnt:
        break



""" 23.7 Маски """
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


# https://stepik.org/lesson/870004/step/8?unit=874178
for n in range(10 ** 9 - (10 ** 9 % 2023), 123456, -2023):
    s = str(n)
    if all([s[:3] == '123', s[-1] == '6', '45' in s]):
        print(n, n // 2023)
        
# Вариант
from fnmatch import fnmatch
start = '123'
for k in range(10**5, 0, -1):
    n = start + str(k) + '6'
    if fnmatch(n, '123*45*6') and int(n) % 2023 == 0:
        print(n, int(n) // 2023)


# https://stepik.org/lesson/870004/step/9?unit=874178
for n in range(0, 10**9 - (10**9 % 1968) + 1, 1968):
    s = str(n)
    if all([s[0] == '1', s[-1] == '8', '3' in s]):
        pass
        if all(s[i] <= s[i + 1] for i in range(len(s) - 1)):
            print(n, n // 1968)

# Вариант (работает дольше)
from fnmatch import fnmatch
for k in range(10**7):
    n = '1' + str(k) + '8'
    if fnmatch(n, '1*3*8') and int(n) % 1968 == 0 and \
            all(n[i] <= n[i + 1] for i in range(len(n) - 1)):
        print(n, int(n) // 1968)


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


# https://stepik.org/lesson/870004/step/15?unit=874178
# ?5*5*?4
cnt = 6
for n in range(24, 100_000, 24):
    s = str(n)
    if all([s[1] == '5', s[-1] == '4', '5' in s[2:-2]]):
        print(n)
        cnt -= 1
        if not cnt: break

from fnmatch import fnmatch
cnt = 6
for k in range(100_000):
    n = str(k)
    if fnmatch(n, '?5*5*?4') and not int(n) % 24:
        print(n)
        cnt -= 1
        if not cnt: break



""" 23.8 Маски. Решение задач """
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

# https://stepik.org/lesson/871176/step/4?unit=875447
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


# https://stepik.org/lesson/871176/step/5?unit=875447
from fnmatch import fnmatch
def fn(n):
    d = set()
    for i in range(1, int(n**0.5 + 1)):
        if not n % i:
            d.add(i)
            d.add(n // i)
    return len(d)

msk = '?1*2*?0'
cnt = 5
for n in range(200_000):
    if fnmatch(str(n), msk) and not n % (3*5*7):
        print(n, fn(n))
        cnt -= 1
    if not cnt: break


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


# https://stepik.org/lesson/871176/step/8?unit=875447
from fnmatch import fnmatch
def fn(n):
    d = set()
    for i in range(1, int(n**0.5 + 1)):
        if not n % i:
            d.add(i)
            d.add(n // i)
    return len([i for i in d if i % 2])

msk = '123?4*'
cnt = 5
for n in range(123, 10**7, 123):
    if fnmatch(str(n), msk):
        print(n, fn(n))
        cnt -= 1
    if not cnt: break


# https://stepik.org/lesson/871176/step/9?unit=875447
from fnmatch import fnmatch
def fn(n):
    d = set()
    for i in range(1, int(n**0.5 + 1)):
        if not n % i:
            d.add(i)
            d.add(n // i)
    return len([i for i in d if i % 2]), sum(i for i in d if not i % 2)

msk = '12*3?4'
cnt = 6
for n in range(2022, 10**8, 2022):
    if fnmatch(str(n), msk):
        print(n, *fn(n))
        cnt -= 1
    if not cnt: break


# https://stepik.org/lesson/871176/step/11?unit=875447
from fnmatch import fnmatch

msk = '1[02468]2??[13579]?'
n_start = 10**6 // 2023 * 2023  # 999362
for n in range(n_start, 2_000_000, 2023):
    if fnmatch(str(n), msk):
        print(n, n // 2023)


# https://stepik.org/lesson/871176/step/12?unit=875447
from fnmatch import fnmatch

ev = '[02468]'
od = '[13579]'
msk = f'?{ev}{od}?{ev}{od}?'
cnt = 5
for n in range(172, 10**7, 172):
    if fnmatch(str(n), msk):
        print(n, sum(int(i) for i in str(n)))
        cnt -= 1
    if not cnt: break


# https://stepik.org/lesson/871176/step/14?unit=875447
alfa = '0123456789ABCDEF'
dv = int('AC', 16)
for i in alfa:
    for k in alfa:
        num = int(f'2{i}ABC{k}ABC', 16)
        if not num % dv:
            print(num, num // dv)


# https://stepik.org/lesson/871176/step/15?unit=875447
alf = '0123456789ABCDEF'
for i in alf:
    for k in alf:
        n = int(f'3{k}ABC{i}FDE', 16)
        if not n % int('3F', 16):
            print(n, n // int('3F', 16))


# https://stepik.org/lesson/871176/step/16?unit=875447
alf = '01234567'
for i in alf:
    for k in alf:
        n = int(f'1{i}234{k}567', 8)
        if not n % int('33', 8):
            print(n, n // int('33', 8))


