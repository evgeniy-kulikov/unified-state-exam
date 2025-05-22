"""
Task 24
ЕГЭ Питоныч
https://stepik.org/course/100138
Задание 24 КЕГЭ. Часть 1  --> task24_01
Задание 24 КЕГЭ. Часть 2
"""

""" 22.1 Поиск C-подцепочек """

# https://stepik.org/lesson/784665/step/4?unit=787262
# В этом разделе все решения без проверки на пустую строку !!!
from re import findall
st = input()
reg = r'[C]+'
ls = max(findall(reg, st), key=len)
print(len(ls))

# Вариант
st = input()
st = st.replace('A', ' ').replace('B', ' ')
ls = max(st.split(), key=len)
print(len(ls))


# https://stepik.org/lesson/784665/step/5?unit=787262
from re import findall
st = input()
reg = r'[A]+'
ls = max(findall(reg, st), key=len)
print(len(ls))

# Вариант
st = input()
st = st.replace('B', ' ').replace('C', ' ')
ls = max(st.split(), key=len)
print(len(ls))


# https://stepik.org/lesson/784665/step/6?unit=787262
from re import findall
ls = findall(r'[BC]+', input())  # в цепочке есть или только 'В' или только 'С' или оба символа вместе
ls = findall(r'B+C+|C+B+', input())  # в цепочке есть обязятельно оба символа 'В' и 'С'
print(len(max(ls, key=len)))

# Вариант
st = input()
st = st.replace('A', ' ')
ls = max(st.split(), key=len)
print(len(ls))


# https://stepik.org/lesson/784665/step/7?unit=787262
from re import findall
ls = findall(r'[AC]+', input())  # в цепочке есть или только 'A' или только 'С' или оба символа вместе
print(len(max(ls, key=len)))

# Вариант
st = input()
st = st.replace('B', ' ')
ls = max(st.split(), key=len)
print(len(ls))


# https://stepik.org/lesson/784665/step/8?unit=787262
from re import findall
ls = findall(r'[BCD]+', input())
print(len(max(ls, key=len)))

# Вариант
st = input()
st = st.replace('A', ' ').replace('E', ' ').replace('F', ' ')
ls = max(st.split(), key=len)
print(len(ls))


# https://stepik.org/lesson/784665/step/10?unit=787262
from re import findall
ls = findall(r'[^E]+', input())
print(len(max(ls, key=len)))

# Вариант
st = input()
st = st.replace('E', ' ')
ls = max(st.split(), key=len)
print(len(ls))


# https://stepik.org/lesson/784665/step/11?unit=787262
from re import findall
ls = findall(r'[^FA]+', input())
print(len(max(ls, key=len)))

# Вариант
st = input()
st = st.replace('F', ' ').replace('A', ' ')
ls = max(st.split(), key=len)
print(len(ls))


# https://stepik.org/lesson/784665/step/12?unit=787262
from re import findall
ls = findall(r'[^AEIOUY]+', input())  # AEIOUY - гласные буквы
print(len(max(ls, key=len)))


# https://stepik.org/lesson/784665/step/13?unit=787262
from re import findall
ls = findall(r'[ABCD]+', input())  # AEIOUY - гласные буквы
print(len(max(ls, key=len)))



""" 22.2 Поиск произвольных подцепочек """

# https://stepik.org/lesson/784660/step/2?unit=787257
st = input()
res = st[0]
for i in range(1, len(st)):
    if st[i - 1] != st[i]:
        res += st[i]
    else:
        res += ' ' + st[i]
print(max(map(len, res.split())))

# Вариант
st = input()
cnt = res = 1
for i in range(1, len(st)):
    if st[i - 1] != st[i]:
        cnt += 1
    else:
        res = max(cnt, res)
        cnt = 1
print(res)


# https://stepik.org/lesson/784660/step/3?unit=787257
st = input()
res = st[0]
for i in range(1, len(st)):
    if st[i - 1] == st[i]:
        res += st[i]
    else:
        res += ' ' + st[i]
print(max(map(len, res.split())))

# Вариант
st = input()
cnt = res = 1
for i in range(1, len(st)):
    if st[i - 1] == st[i]:
        cnt += 1
    else:
        res = max(cnt, res)
        cnt = 1
print(res)


# https://stepik.org/lesson/784660/step/4?unit=787257
st = input()
res = st[0]
for i in range(1, len(st)):
    if st[i - 1] < st[i]:
        res += st[i]
    else:
        res += ' ' + st[i]
print(max(map(len, res.split())))

# Вариант
st = input()
cnt = res = 1
for i in range(1, len(st)):
    if st[i - 1] < st[i]:
        cnt += 1
    else:
        res = max(cnt, res)
        cnt = 1
print(res)


# https://stepik.org/lesson/784660/step/9?unit=787257
from re import *
res = 0
reg = r'(DE|DF)+'
for i in finditer(reg, input()):
    res = max(res, len(i.group()) // 2)
print(res)

# Вариант
st = st.replace('DF', '*').replace('DE', '*')
st = st.replace('D', ' ').replace('E', ' ').replace('F', ' ')
res = max(st.split(), key=len)
print(len(res))



""" 22.3 Исключение подцепочек """
# FAQ  https://stepik.org/lesson/784661/step/1?unit=787258

# https://stepik.org/lesson/784661/step/2?unit=787258
s = input()
s = s.replace('12', '1 2')
res = max(s.split(), key=len)
print(len(res))  # 34


# https://stepik.org/lesson/784661/step/4?unit=787258
s = input()
s = s.replace('AB', 'A B').replace('CD', 'C D')
res = max(s.split(), key=len)
print(len(res))  # 16


# https://stepik.org/lesson/784661/step/6?unit=787258
s = input()
s = s.replace('123', '12 23')
res = max(s.split(), key=len)
print(len(res))  # 35


# https://stepik.org/lesson/784661/step/8?unit=787258
s = input()
s = s.replace('1234', '123 234')
res = max(s.split(), key=len)
print(len(res))  # 46


# https://stepik.org/lesson/784661/step/9?unit=787258
s = input()
s = s.replace('1234', '123 234').replace('ABC', 'AB BC')
res = max(s.split(), key=len)
print(len(res))  # 29


# https://stepik.org/lesson/784661/step/13?unit=787258
"""
FAQ:  https://stepik.org/lesson/784661/step/13?unit=787258
Если запрещенная подстрока начинается и заканчивается одним и тем же символом, 
замены в программе выполнять через цикл while
"""

s = input()
while '111' in s:
    s = s.replace('111', '11 11', 1)
res = max(s.split(), key=len)
print(len(res))  # 36


# https://stepik.org/lesson/784661/step/16?unit=787258
s = input()
while '12321' in s:
    s = s.replace('12321', '1232 2321', 1)
res = max(s.split(), key=len)
print(len(res))  # 21



""" 22.4 Тройки символов """

# https://stepik.org/lesson/867224/step/2?unit=871325
from re import *
s = input()
reg = r'(\w\d{2})+'
w = findall(reg, s)
res = max(len(i.group(0)) for i in finditer(reg, s))
print(res // 3)  # 9


# https://stepik.org/lesson/867224/step/3?unit=871325
from re import *
s = input()
reg = r'(\w\d[!?])+'
w = findall(reg, s)
res = max(len(i.group(0)) for i in finditer(reg, s))
print(res // 3)  # 8



""" 22.4 Тройки символов """
# FAQ:  https://stepik.org/lesson/867224/step/5?unit=871325

# https://stepik.org/lesson/867224/step/6?unit=871325
s = input().split('.')  # список
res = 0
for i in range(len(s) - 3):
    cur = len(s[i] + s[i + 1] + s[i + 2] + s[i + 3]) + 3
    res = max(res, cur)
print(res)


# https://stepik.org/lesson/867224/step/8?unit=871325
s = input().split('.')  # список
res = 0
for i in range(len(s) - 8):
    # cur = len(s[i] + s[i+1] + s[i+2] + s[i+3] + s[i+4] + s[i+5] + s[i+6] + s[i+7] + s[i+8]) + 8
    cur = len(''.join(s[i:i + 9])) + 8
    res = max(res, cur)
print(res)



""" 22.5 Цифры в строке """
# FAQ:  https://stepik.org/lesson/867294/step/1?unit=871451

# https://stepik.org/lesson/867294/step/2?unit=871451
from string import ascii_uppercase
s = input()
for i in ascii_uppercase:
    s = s.replace(i, ' ')
s = s.split()
res = max(int(i) for i in s if i[-1] in '02468')
print(res)

# option
from re import *
res = 0
reg = r'\d*[02468](?=\D|$)'
for n in finditer(reg, input()):
    res = max(res, int(n.group()))
print(res)


# https://stepik.org/lesson/867294/step/4?unit=871451
from sys import maxsize
from re import *
res = maxsize
reg = r'\d*[02468](?=\D|$)'
for n in finditer(reg, input()):
    res = min(res, int(n.group()))
print(res)


# https://stepik.org/lesson/867294/step/5?unit=871451
from re import *
cnt = 0
reg = r'\d*[02468](?=\D|$)'
print(len(findall(reg, input())))


# https://stepik.org/lesson/867294/step/7?unit=871451
from string import ascii_uppercase
s = input()
for i in ascii_uppercase:
    s = s.replace(i, ' ')
s = s.split()
res = [i for i in s if i == i[::-1]]
print(len(res))

# option
from re import *
cnt = 0
reg = r'\d+(?=\D|$)'
ls = findall(reg, input())
res = [i for i in ls if i == i[::-1]]
print(len(res))


# https://stepik.org/lesson/867294/step/9?unit=871451
from re import *
with open('add/course_100138/24_17563.txt') as fl:
    f = fl.read()
reg = r'[7-9]\d*([-*][7-9]\d*)+'
ls = [len(i.group()) for i in finditer(reg, f)]
print(max(ls))  # 40

# option
with open('24_17563.txt') as fl:
    f = fl.read().strip()
f = f.replace('-','*')
while '**' in f: f= f.replace('**','* *')
while '*0' in f: f= f.replace('*0','* 0')
mx = 0
for c in f.split():
    while len(c) > 0 and c[0] in '0*': c = c[1:]
    while len(c) > 0 and c[-1] == '*': c = c[:-1]
    if '*' in c:
        mx = max(mx, len(c))
        if len(c) > 35:
            print(c)
print(mx)



# https://stepik.org/lesson/867294/step/10?unit=871451
# !!!  НЕ СХОДИТСЯ С ОТВЕТОМ  142   !!!
from re import *
with open('add/course_100138/24_17641.txt') as fl:
    f = fl.read()
reg = r'(0|([1-9]\d*))([+*](0|([1-9]\d*)))+'
# без вычисления выражения
mx = 0
for i in finditer(reg, f):
    mx = max(mx, len(i.group()))
    # if len(i.group()) > 185:
    #     print(i.group())
print(mx)  # 189

# с вычислением выражения
mx = 0
for i in finditer(reg, f):
    if not eval(i.group()):
        mx = max(mx, len(i.group()))
        # if len(i.group()) > 128:
        #     print(i.group())
print(mx)  # 130



""" 22.6 Регулярные выражения """
# FAQ:  https://stepik.org/lesson/1683491/step/11?unit=1706669

# https://stepik.org/lesson/1683491/step/4?unit=1706669
from re import *
reg = r'(D[EF])+'
res = 0
for i in finditer(reg, input()):
    res = max(res, len(i.group()) // 2)
print(res)


# https://stepik.org/lesson/1683491/step/6?unit=1706669
from re import *
reg = r'(\w\d{2})+'
res = 0
for i in finditer(reg, input()):
    res = max(res, len(i.group()) // 3)
print(res)


# https://stepik.org/lesson/1683491/step/7?unit=1706669
from re import *
reg = r'(\w\d\W)+'
res = 0
for i in finditer(reg, input()):
    res = max(res, len(i.group()) // 3)
print(res)


# https://stepik.org/lesson/1683491/step/9?unit=1706669
from re import *
reg = r'[1-9]\d*'
res = 0
for i in finditer(reg, input()):
    n = int(i.group())
    if not n % 2:
        res = max(res, n)
print(res)


# https://stepik.org/lesson/1683491/step/10?unit=1706669
from re import *
reg = r'[1-9]\d*'
cnt = 0
for i in finditer(reg, input()):
    cnt += int(i.group()) % 2 != 0
print(cnt)



""" 22.7 Арифметические выражения и "регулярки" """
# FAQ:  https://stepik.org/lesson/1688395/step/1?unit=1711683
# FAQ:  https://stepik.org/lesson/1688395/step/5?unit=1711683


# https://stepik.org/lesson/1688395/step/2?unit=1711683
from re import *
with open('add/course_100138/24-304.txt') as fl:
    f = fl.read()
num = '[1-9]\d*'
reg = rf'A{num}([+*]{num})+'
res = 0
for i in finditer(reg, f):
    res = max(res, len(i.group()))
print(res)  # 145


# https://stepik.org/lesson/1688395/step/3?unit=1711683
from re import *
with open('add/course_100138/24-304.txt') as fl:
    f = fl.read()
num = '([1-9]\d*|0)'  # допускается только единственный "0" (после него других "0" нет)
reg = rf'A{num}([+*]{num})+'
res = 0
for i in finditer(reg, f):
    res = max(res, len(i.group()))
print(res)  # 147


# https://stepik.org/lesson/1688395/step/4?unit=1711683
from re import *
with open('add/course_100138/24-310.txt') as fl:
    f = fl.read()
# num = '[1-9A-F][0-9A-F]*'
# reg = rf'{num}([*+](0(?!0)|{num}))+'  # 0(?!0)   допускается только единственный "0" (после него других "0" нет)
num = '([1-9A-F][0-9A-F]*|0)'  # допускается только единственный "0" (после него других "0" нет)
reg = rf'{num}([*+]{num})+'
res = 0
for i in finditer(reg, f):
    res = max(res, len(i.group()))
print(res)  # 502


# https://stepik.org/lesson/1688395/step/6?unit=1711683
# FAQ:  https://stepik.org/lesson/1688395/step/5?unit=1711683
from re import *
with open('add/course_100138/24-300.txt') as fl:
    f = fl.read()

num = '([1-9]\d*|0)'  # НЕотрицательное число (ноль или положительное)
mul = f'(({num}\*)*0(\*{num})*)'  # Произведение чисел, среди которых ОБЯЗАТЕЛЬНО есть ноль
reg = rf'{mul}(\+{mul})*'  # сумма из произведений, равных нулю (либо только произведение равное нулю)

res = 0
for i in finditer(reg, f):
    res = max(res, len(i.group()))
print(res)  # 126


