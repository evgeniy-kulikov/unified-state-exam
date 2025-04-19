# Информатика Подготовка к ЕГЭ 2025
# https://stepik.org/course/182932
""""""

# https://stepik.org/lesson/1084603/step/1?unit=1094965
from itertools import product
alfa = 'КРЕСЛО'
cnt = 0
for p in product(alfa, repeat=4):
    if p[0] in 'КРСЛ' and p[-1] in 'ЕО':
        cnt += 1
print(cnt)  # 288

# короче
cnt = 0
for p in product('КРЕСЛО', repeat=4):
    cnt += all([p[0] in 'КРСЛ', p[-1] in 'ЕО'])
print(cnt)  # 288

# вариант
cnt = 0
for _ in product('КРСЛ', 'КРЕСЛО', 'КРЕСЛО', 'ЕО'):
    cnt += 1
print(cnt)  # 288


# https://stepik.org/lesson/1084603/step/2?unit=1094965
from itertools import product
cnt = 0
for p in product('WXYZ', 'ABC', 'ABC', 'ABC', 'ABC', 'WXYZ'):
    cnt += 1
print(cnt)  # 1296


# https://stepik.org/lesson/1084603/step/3?unit=1094965
from itertools import product
cnt = 0
for p in product('ПУЛЯ', repeat=6):
    cnt += p.count('У') == 2
print(cnt)  # 1296


# https://stepik.org/lesson/1084603/step/4?unit=1094965
from itertools import product
cnt = 0
for p in product('ЛОДКА', repeat=4):
    cnt += p.count('О') > 1
print(cnt)  # 113


# https://stepik.org/lesson/1084603/step/5?unit=1094965
from itertools import product
cnt = 0
for p in product('САЛО', repeat=6):
    cnt += 0 < p.count('О') < 4
print(cnt)  # 3213


# https://stepik.org/lesson/1084603/step/6?unit=1094965
# лучший вариант
from itertools import permutations
cnt = 0
for p in permutations('ИГРОК',5):
    cnt += all([not p[0] == 'К', 'РОК' not in ''.join(p)])
print(cnt)  # 90

# вариант хуже
from itertools import product
cnt = 0
for p in product('ИГРОК', repeat=5):
    cnt += all([len(set(p)) == 5, not p[0] == 'К', 'РОК' not in ''.join(p)])
print(cnt)  # 90


# https://stepik.org/lesson/1084603/step/7?unit=1094965
from itertools import permutations
from re import findall
r = r'[БКЛН]{2}|[АИОУ]{2}'
cnt = 0
for p in permutations('АБИКЛОУН',8):
    cnt += not findall(r, ''.join(p))
print(cnt)  # 1152

# вариант хуже
from itertools import permutations
cnt = 0
for p in permutations('АБИКЛОУН',8):
    s = ''.join(p)
    s = s.replace('А', '0').replace('И', '0').replace('О', '0').replace('У', '0')
    s = s.replace('Б', '1').replace('К', '1').replace('Л', '1').replace('Н', '1')
    cnt += not any(['00' in s, '11' in s])
print(cnt)  # 1152


# https://stepik.org/lesson/1084603/step/8?unit=1094965
from itertools import product
cnt = 0
for p in product('AB123', repeat=8):
    s = ''.join(p)
    s = s.replace('B', 'A')
    cnt += s.count('A') == 2
print(cnt)  # 81648


# https://stepik.org/lesson/1084603/step/9?unit=1094965
from itertools import product
cnt = 0
for p in product('ВИШНЯ', repeat=6):
    cnt += all([p.count('В') < 2, p[0] !='Ш', p[-1] not in 'ИЯ'])
print(cnt)  # 4352


# https://stepik.org/lesson/1084603/step/10?unit=1094965
from itertools import product
cnt = 0
for p in product('ABCD', repeat=4):
    cnt += list(p) == sorted(p)
print(cnt)  # 35


# https://stepik.org/lesson/1084603/step/11?unit=1094965
from itertools import product
cnt = 0
for p in product('ГЕПАРД', repeat=5):
    cnt += all([p.count('Г') == 1, p[0] != 'А', p[-1] != 'Е'])
print(cnt)  # 2200


# https://stepik.org/lesson/1084603/step/12?unit=1094965
from itertools import permutations
cnt = 0
for p in permutations('ДЕЙКСТРА', 6):
    cnt += p[:-1].count('Й') == 1 and p[p.index('Й') + 1] in 'ДКСТР'
print(cnt)  # 9000


# https://stepik.org/lesson/1084603/step/13?unit=1094965
from itertools import permutations
from re import findall
cnt = 0
r = r'ВФ|ФВ'
for p in permutations('ВАЙФУ', 4):
    cnt += all([p[0] != 'Й', not findall(r, ''.join(p))])
print(cnt)  # 68


# https://stepik.org/lesson/1084604/step/1?unit=1094966
print(int('1000', 5) + 1)  # 126


# https://stepik.org/lesson/1084604/step/4?thread=solutions&unit=109496
alfa = 'АИМРЯ'
n = 210
s = ''
while n:
    s = alfa[n % 5] + s
    n //= 5
print(s)  # ИРМА  (1320)


# https://stepik.org/lesson/1107346/step/1?unit=1118584
# print(int('200000', 5))  # 6250
# print(int('444444', 5))  # 15624
cnt = 0
for n in range(int('200000', 5), int('444444', 5) + 1):
    s = ''
    while n:
        s = str(n % 5) + s
        n //= 5
    cnt += not s[-1] in '34'
print(cnt)  # 5625


# https://stepik.org/lesson/1107346/step/2?unit=1118584
from re import findall
r = '[0246]{2}|[1357]{2}'
cnt = 0
for n in range(int('20000', 8), int('77777', 8) + 1):
    s = ''
    while n:
        s = str(n % 8) + s
        n //= 8
    cnt += all([not '1' in s, len(set(s)) == 5, not findall(r, s)])
print(cnt)  # 180

# вариант без модуля re
def valid(num):
    odd = '0246'
    ls = [i in odd for i in num]
    for i, n in enumerate(ls[:-1]):
        if n == ls[i + 1]:
            return False
    return True

cnt = 0
for n in range(int('20000', 8), int('77777', 8) + 1):
    s = ''
    while n:
        s = str(n % 8) + s
        n //= 8
    cnt += all([not '1' in s, len(set(s)) == 5, valid(s)])
print(cnt)  # 180



# https://stepik.org/lesson/1107346/step/3?unit=1118584
cnt = 0
for i in range(100, 1000):
    n = str(i)
    if list(n) == sorted(n):
        cnt += 1
print(cnt)  # 165

# короче
print(sum(list(str(i)) == sorted(str(i)) for i in range(100, 1000)))  # 165


# https://stepik.org/lesson/1107346/step/4?unit=1118584
cnt = 0
for n in range(int('10000', 7), int('66666', 7) + 1):
    s = ''
    while n:
        s = str(n % 7) + s
        n //= 7
    if s.count('6') == 1:
        cnt += sum(int(i) for i in s if i in '0246') < sum(int(k) for k in s if k in '135')
print(cnt)  # 1390


# https://stepik.org/lesson/1107346/step/5?unit=1118584
from re import findall
r = r'[^1357]\d{5}[^02468]'
cnt = 0
for n in range(int('2000001', 9), int('8888888', 9)):
    s = ''
    while n:
        s = str(n % 9) + s
        n //= 9
    cnt += all([s.count('8') == 1, findall(r, s)])
print(cnt)  # 376832


# https://stepik.org/lesson/1107347/step/1?unit=1118585
from re import findall
r = r'[1357]{2}|[02468]{2}'
cnt = 0
# for n in range(int('10000', 8), int('77777', 8) + 1):
for n in range(int('23054', 8), int('76544', 8)):
    s = ''
    while n:
        s = str(n % 8) + s
        n //= 8
    d = s
    cnt += all([not s.count('1'), not findall(r, s), len(set(s)) == 5])
print(cnt)  # 180


# https://stepik.org/lesson/1107347/step/1?unit=1118585
from re import findall
r = r'[1357]{2}|[02468]{2}'
cnt = 0
# for n in range(int('10000', 8), int('77777', 8) + 1):
for n in range(int('23054', 8), int('76544', 8)):
    s = ''
    while n:
        s = str(n % 8) + s
        n //= 8
    d = s
    cnt += all([not s.count('1'), not findall(r, s), len(set(s)) == 5])
print(cnt)  # 180


# https://stepik.org/lesson/1107347/step/2?unit=1118585
from re import findall
reg = r'[02468ace]{2}|[13579bdf]{2}'
cnt = 0
for n in range(200, 4500):
    i = hex(n)[2:]
    cnt += all([len(i) == 3, len(set(i)) == 3, not findall(reg, i)])
print(cnt)  # 840


#  https://stepik.org/lesson/1107347/step/4?unit=1118585
cnt = 0
even = '135'
for n in range(int('10000', 7), int('66666', 7) + 1):
    s = ''
    while n:
        s = str(n % 7) + s
        n //= 7
    if len(s) == 5 and s.count('5') == 1:
        i = s.index('5')
        s = '1' + s + '1'
        cnt += s[i] in even and s[i + 2] in even
print(cnt)  # 1176




