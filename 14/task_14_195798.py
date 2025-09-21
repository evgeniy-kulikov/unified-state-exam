""""""
"""
Task 14
ЕГЭ информатика 2025. Полный курс
https://stepik.org/course/195798
"""



""" 19.2 Практика (ур. базовый) """
# https://stepik.org/lesson/1225426/step/1?unit=1238917
def f(n):
    alf = '0123456789' + '*' * 15
    s = ''
    while n:
        s = alf[n % 25] + s
        n //= 25
    return s

n = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2024
print(f(n).count('0'))  # 9

# short solution
n = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2024
cnt = 0
while n:
    cnt += not n % 25
    n //= 25
print(cnt)  # 9


# https://stepik.org/lesson/1225426/step/2?unit=1238917
from string import ascii_lowercase, digits
alf = digits + ascii_lowercase[:9]
for x in alf[::-1]:
    n = int(f'98897{x}21' , 19) + int(f'2{x}923', 19)
    if not n % 18:
        print(n // 18)  # 469034148
        break


# https://stepik.org/lesson/1225426/step/4?unit=1238917
def f(n):
    s = ''
    while n:
        s = str(n % 5) + s
        n //= 5
    return s

n = 7 * 5**123 + 6 * 5**111 - 5 * 25**50 + 4 * 125**30 - 3 * 5**10
print(f(n).count('4'))


# https://stepik.org/lesson/1225426/step/5?unit=1238917
for n in range(6, 36):
    if not (7**500 - int('53', n)) % 6:
        print(n)  # 8
        break


# https://stepik.org/lesson/1225426/step/6?unit=1238917
from string import hexdigits
for x in hexdigits[::-1]:
    n = int(f'1F3B{x}75', 16) + int(f'5D{x}3B', 16)
    if not n % 11:
        print(n // 11)  # 3012112
        break


# https://stepik.org/lesson/1225426/step/7?unit=1238917
def f(num, n):
    s = ''
    while num:
        s = str(num % n) + s
        num //= n
    return s

num = 343**515 - 6 * 49**520 + 5 * 49**510 - 3 * 7**530 - 550
print(f(num, 7).count('6'))  # 1519


# https://stepik.org/lesson/1225426/step/9?unit=1238917
from string import  hexdigits
def f(num, n):
    alf = hexdigits
    s = ''
    while num:
        s = hexdigits[num % n] + s
        num //= n
    return s

num = 673**7 + 67**6 + 3**3
res = f(num, 12)
# print(int('a', 12) * res.count('a') - int('8', 12) * res.count('8'))  #
print(10 * res.count('a') - 8 * res.count('8'))  # 2

# short solution
num = 673**7 + 67**6 + 3**3
res = ''
while num:
    if num % 12 == 10:
        res += 'a'
    elif num % 12 == 8:
        res += '8'
    num //= 12
print(10 * res.count('a') - 8 * res.count('8'))  # 2


# https://stepik.org/lesson/1225426/step/10?unit=1238917
num =  2197**50 - 169**35 - 26
res = ''
while num:
    if num % 13 == 12:
        res += 'c'
    num //= 13
print(res.count('c'))  # 147


# https://stepik.org/lesson/1225426/step/11?unit=1238917
num = 3 * 3125**9 + 2 * 625**8 - 4 * 625**7 + 3 * 125**6 - 2 * 25**5 - 2024
cnt = 0
while num:
    cnt += not num % 25
    num //= 25
print(cnt)  # 9


# https://stepik.org/lesson/1225426/step/12?unit=1238917
from string import ascii_lowercase, digits
for x in digits + ascii_lowercase[:9]:
    res = (int(f'78{x}79643', 19) + int(f'25{x}43', 19) + int(f'63{x}5', 19))
    if not res % 18:
        print(res // 18)  # 368599039
        break


# https://stepik.org/lesson/1225426/step/13?unit=1238917
num = 2*729**333 + 2*243**334 - 81**335 + 2*27**336 - 2*9**337 - 338
cnt = 0
while num:
    cnt += bool(num % 9)
    num //= 9
# while num:
#     if num % 9:
#         cnt += 1
#     num //= 9
print(cnt)  # 9


# https://stepik.org/lesson/1225426/step/14?unit=1238917
from string import ascii_lowercase, digits
for x in digits + ascii_lowercase[:22]:
    res = (int(f'931{x}964', 32) + int(f'4{x}51{x}1', 32) + int(f'2861{x}637', 32))
    if not res % 31:
        print(res // 31)  # 2820159444
        break



""" 19.3 Практика (ур. усложненный) """
# https://stepik.org/lesson/1225427/step/1?unit=1238918
def f(num, n):
    s = ''
    while num:
        s = str(num % n) + s
        num //= n
    return s

for x in range(99, -1, -1):
    a = 7*100**6 + 10*100**5 + x*100**4 + 0 + 100**2 + 2*100 + 3
    b = 100**5 + 11*100**4 + 10*100**3 + 6*100**2 + 4*100 + x
    c = x*100**6 + 9*100**5 + 8*100**4 + 0 + 100**2 + 2*100 + 12
    if not (a - b + c) % 21:
        print(f(x, 6))  # 224
        break


# https://stepik.org/lesson/1225427/step/2?unit=1238918
from string import ascii_lowercase, digits
alf = digits + ascii_lowercase
for i in range(5, 37):
    for x in alf[:i]:
        for y in alf[:i]:
            a = int('32', i) * int('14', i)
            b = int(f'{x}{y}2', i)
            if a == b:
                print(int(f'{y}{x}', i))  # 23
                break

# short solution
for p in range(5, 10):
    for x in range(p):
        for y in range(p):
            if (3 * p + 2) * (1 * p + 4) == (x * p**2 + y * p + 2):
                print(y * p + x)  # 23
                break


# https://stepik.org/lesson/1225427/step/3?unit=1238918
def f(num, n):
    s = ''
    while num:
        s = str(num % n) + s
        num //= n
    return s

for x in range(15, -1, -1):
    a = 11 * 16**4 + 7 * 16**3 + 10 * 16**2 + x*16 + 9
    b = 5 * 16**4 + 4 * 16**3 + x * 16**2 + 14*16 + 13
    if sum(map(int, f(a + b, 6)))  == 25:
        print(a + b)  # 1099430
        break

# variant
for x in '0123456789abcdef'[::-1]:
    a = int(f'b7a{x}9', 16)
    b = int(f'54{x}ed', 16)
    if sum(map(int, f(a + b, 6)))  == 25:
        print(a + b)  # 1099430
        break


# https://stepik.org/lesson/1225427/step/4?unit=1238918
for x in range(67, -1, -1):
    a = 68**4 + 2 * 68**3 + 3 * 68**2 + x*68 + 5
    b = 68**4 + x * 68**3 + 2 * 68**2 + 3*68 + 3
    if not (a + b) % 12:
        print((a + b) // 12)  # 5321454
        break


# https://stepik.org/lesson/1225427/step/5?unit=1238918
from string import digits, ascii_lowercase
alf = digits + ascii_lowercase
res = 0

def f(num, n):
    s = ''
    while num:
        s = str(num % n) + s
        num //= n
    return s

for x in alf[:20]:
    a = int(f'{x}1{x}2{x}3{x}4', 20)
    for y in alf[:5]:
        b = int(f'1{y}2{y}3{y}4{y}', 5)
        r = sum(map(int, f(a-b, 7)))
        res = max(res, r)
print(res)  # 56




""" 20.4 Закрепление """
# https://stepik.org/lesson/1226263/step/14?unit=1239750
for x in '0123456789ab':
    r = (int(f'982{x}8', 11) + int(f'194{x}7', 11))
    if not r % 58:
        print(r // 58)  # 2931
        break

