""""""
"""
Task 14
ЕГЭ Питоныч
https://stepik.org/course/100138
"""

# 9.1 Задание 14 КЕГЭ. Часть 1

# https://stepik.org/lesson/559861/step/4?unit=553906
print(f'{(2**10 - 2**2):b}'.count('1'))  # 8


# https://stepik.org/lesson/559861/step/9?unit=553906
n = 9**123 + 3**456 - 3**78 + 22
s = ''
while n:
    s += str(n % 3)
    n //= 3
print(s.count('2'))


# https://stepik.org/lesson/559861/step/12?unit=553906
n = 12 * 3**45 - 5**6 - 22
s = ''
while n:
    s += str(n % 7)
    n //= 7
print(sum(map(int, s)))  # 73



""" 9.2 Задание 14 КЕГЭ. Часть 2 """

# https://stepik.org/lesson/1030570/step/2?unit=1038941
a = '0123456789abcde'
for x in a:
    res = int(f'97968{x}13', 15) + int(f'7{x}213', 15)
    if not res % 14:
        print(res // 14)  # 116070624
        break


# https://stepik.org/lesson/1030570/step/4?unit=1038941
a = '0123456789abcde'
cnt = 0
for x in a:
    res = int(f'97968{x}13', 15) + int(f'7{x}213', 15)
    if not res % 14:
        cnt += 1
print(cnt)  # 3


# https://stepik.org/lesson/1030570/step/6?unit=1038941
a = '0123456789abcde'[::-1]
for i, x in enumerate(a):
    res = int(f'97968{x}15', 15) + int(f'7{x}233', 15)
    if not res % 14:
        print(res //14)
        break



""" 9.3 Задание 14 КЕГЭ через списки """

# https://stepik.org/lesson/894887/step/2?unit=899812
n = 49**7 + 7**21 - 7
s = ''
while n:
    s += str(n % 7)
    n //= 7
print(s.count('6'))  # 13


# https://stepik.org/lesson/894887/step/6?unit=899812
n = 4*25**2022 - 2*5**2000 + 125**1011 - 3*5**100 - 660
s = ''
while n:
    s += str(n % 5)
    n //= 5
print(s.count('4') - s.count('3'))  # 3025


# https://stepik.org/lesson/894887/step/9?unit=899812
a = '0123456789№#@$*'
s = ''
n = 100**2 + 625**25 + 5**100
while n:
    s += a[n % 15]
    n //= 15
print(s.count('@'))  # 3


# https://stepik.org/lesson/894887/step/14?unit=899812
for x in range(2030, 0, -1):
    n = 7**91 + 7**160 - x
    s = ''
    while n:
        s += str(n % 7)
        n //= 7
    if s.count('0') == 70:
        print(x)  # 2029
        break





""" 9.3 Задание 14 КЕГЭ через списки """

# https://stepik.org/lesson/894887/step/11?unit=899812
for x in range(1, 100):
    n = 81**20 - 9**x + 50
    s = ''
    while n:
        s += str(n % 9)
        n //= 9
    if sum(map(int, s)) == 138:
        print(x)  # 24
        break

