"""
Task 14
Подготовка к ЕГЭ информатика
https://stepik.org/course/57248?auth=login
"""

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

