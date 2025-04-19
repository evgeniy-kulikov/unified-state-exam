""""""
"""
Task 05
Подготовка к ЕГЭ информатика
https://stepik.org/course/57248
"""

#  https://stepik.org/lesson/552237/step/1?unit=545965
# Короче
def g(n, d):
    if n % d == 0:
        return n // d
    return n - 1

def f(n):
    n = g(n, 3)
    n = g(n, 5)
    n = g(n, 11)
    return n

cnt = 0
for n in range(1, 1_000_000):
    if f(n) == 8:
        cnt += 1
print(cnt)  # 4


# https://stepik.org/lesson/552237/step/2?unit=545965
def get_bin(b):
    one = b.count('1')
    zero = b.count('0')
    if one == zero:
        b += b[-1]
    else:
        b += ['0', '1'][zero > one]
    return b

for n in range(500, 0, -1):
    b = bin(n)[2:]
    for _ in range(3):
        b = get_bin(b)
    i = int(b, 2)
    if not i % 4 and i % 8:
        print(n)  # 225
        break


# https://stepik.org/lesson/552237/step/3?unit=545965
def get_num(n: str):
    one = n.count('1')
    zero = n.count('0')
    if one == zero:
        return n + n[-1]
    return n + ['0', '1'][zero > one]

for i in range(750, 0, -1):
    b = bin(i)[2:]
    for _ in range(3):
        b = get_num(b)
    n = int(b, 2)
    if not n % 2 and n % 4:
        print(i)  # 480
        break


# https://stepik.org/lesson/552237/step/4?unit=545965
ls = list(range(150, 201))
cnt = 0
for i in range(2, 1000):
    b = bin(i)[2:]
    b += b[1]
    b += b[-2]
    if int(b, 2) in ls:
        cnt += 1
print(cnt) # 12


# https://stepik.org/lesson/552237/step/5?unit=545965
def fn(n: int):
    one = n.bit_count()
    zero = n.bit_length() - one
    if one > zero:
        # return int(bin(n)[2:] + '0', 2)
        return n * 2
    return int('11' + bin(n)[2:], 2)

for i in range(1, 1000):
    n = i
    n = fn(fn(n))
    if n > 500:
        print(i)  # 32
        break

# https://stepik.org/lesson/421051/step/1?auth=login&unit=410661
for n in range(131, 256):
    b = bin(n)[2:].zfill(8)
    b = b[:2] + b[6:]
    if int(b, 2) == 10:
        print(n)  # 134
        break

# https://stepik.org/lesson/421051/step/2?auth=login&unit=410661
for n in range(100, -1,-1):
    b = bin(n)[2:].zfill(8)[:-1][::-1]
    if int(b, 2) == n:
        print(n)  # 90
        break

# https://stepik.org/lesson/421051/step/3?auth=login&unit=410661
res = set()
for n in range(10, 2501):
    b = bin(n)[2:]
    b = b.replace('0', '')
    res.add(int(b, 2))
print(len(res))  # 11


# https://stepik.org/lesson/421051/step/4?auth=login&unit=410661
res = set()
for n in range(20, 601):
    b = bin(n)[2:][:-2]
    res.add(int(b, 2))
print(len(res))  # 146


# https://stepik.org/lesson/421051/step/5?auth=login&unit=410661
n = 95
s = ''
b = bin(n)[2:].zfill(8)
for i in range(len(b)):
    s += ['0', '1'][b[i] == '0']  # Инвертируются разряды воичного числа (0 на 1, 1 на 0)
print(int(s, 2) + 1)  # 161


# https://stepik.org/lesson/421051/step/6?auth=login&unit=410661
for n in range(255, -1, -1):
    s = ''
    b = bin(n)[2:].zfill(8)
    for i in range(7):
        s += ['0', '1'][b[i] == '0']  # Инвертируются разряды воичного числа (0 на 1, 1 на 0)
    s = s + b[-1]
    if int(s, 2) == 171:
        print(n)  # 85
        break


# https://stepik.org/lesson/421051/step/6?auth=login&unit=410661
for n in range(1, 1000):
    b = bin(n)[2:]
    b = b + ['0', '1'][not b.count('1') % 2]
    b = b + str(b.count('1') % 2)
    r = int(b, 2)
    if r > 31:
        print(r)  # 33
        break




