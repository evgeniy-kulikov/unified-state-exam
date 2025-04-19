""""""
"""
Task 08
Подготовка к ЕГЭ информатика
https://stepik.org/course/57248
"""



# https://stepik.org/lesson/552237/step/6?unit=545965
from itertools import product
import re
reg = r'[ЛД]{0,1}[АИ]+'
cnt = 0
for i in range(3, 6):
    for p in product('ЛИДА', repeat=i):
        p = ''.join(p)
        if re.fullmatch(reg, p) and p.count('И') < 3 and p.count('А') < 3:
            cnt += 1
print(cnt)  # 44


# https://stepik.org/lesson/552237/step/7?unit=545965
def fn(n):  # по сути эта функция лишняя
    s = ''
    while n:
        s = str(n % 5) + s
        n //= 5
    return all([len(s) == 6, s[0] == '3', not int(s, 5) % 2])

cnt = 0
for n in range(3 * 5 ** 5, 4 * 5 ** 5):
    # cnt += fn(n)  # по сути эта функция лишняя
    cnt += not n % 2
print(cnt)  # 1562


from itertools import product
import re
reg = r'[КСН]{0,1}[ЕИЯ]{2,}'
cnt = 0
for i in range(3, 8):
    for p in product('КСЕНИЯ', repeat=i):
        p = ''.join(p)
        if re.fullmatch(reg, p):
            cnt += all([p.count('Е') < 3, p.count('И') < 3, p.count('Я') < 3])
print(cnt)  # 1059



# https://stepik.org/lesson/552237/step/9?unit=545965
# http://lavinova8.ru/gotovimsja-k-egje/zadanie-8-kombinatorika.html
from itertools import permutations
ls = []
for p in permutations('МАРИ'):
    ls += [''.join(p)]
ls.sort()
# print(ls.index('МАРИ'))  # 13
# перед словом, начинающимся с МАРИ, возможны 13 вариантов начала слова

# Рассмотрим вторую половину слова
from itertools import product
cnt = 0
for p in product('ИНА',  repeat=4):
    cnt += 1
# print(cnt)  # 81
# 13 * 81 = 1053   различных слова до слова, начинающегося с МАРИ

cnt = 0
def fn(n):
    alfa = 'АИН'
    if n == 0:
        return 'АААА'
    s = ''
    while n:
        s = str(alfa[n % 3]) + s
        n //= 3
    return s.zfill(4).replace('0', 'А')

for i in range(100):
    cnt += 1
    if fn(i) == 'АННА':
        print(cnt)  # 25  АННА' стоит на 25 месте.
        break
# окончательный ответ: 1053 + 25 = 1078


# https://stepik.org/lesson/552237/step/10?unit=545965
# !!! ИНТЕРЕСНАЯ ЗАДАЧА !!!
s = '0123456789abcdef'
cnt = 0
for d12 in range(15, 10, -1):  # 'b' - меньшая возможная цифра из 'fedcba9876543210' для 12-ти символьного слова
    for d11 in range(d12 - 1, -1, -2):
        for d10 in range(d11 - 1, -1, -2):
            for d9 in range(d10 - 1, -1, -2):
                for d8 in range(d9 - 1, -1, -2):
                    for d7 in range(d8 - 1, -1, -2):
                        for d6 in range(d7 - 1, -1, -2):
                            for d5 in range(d6 - 1, -1, -2):
                                for d4 in range(d5 - 1, -1, -2):
                                    for d3 in range(d4 - 1, -1, -2):
                                        for d2 in range(d3 - 1, -1, -2):
                                            for d1 in range(d2 - 1, -1, -2):
                                                cnt += 1
                                                print(s[d12]+s[d11]+s[d10]+s[d9]+s[d8]+s[d7]+s[d6]+s[d5]+s[d4]+s[d3]+s[d2]+s[d1])
print(cnt)  # 104
# fedcba987654
# fedcba987652
# fedcba987650
# ...
# dc9876543210
# da9876543210
# cba987654321
# ba9876543210


# https://stepik.org/lesson/424708/step/1?auth=login&unit=414440
from itertools import product
cnt = 0
for p in product('катер', repeat=3):
    f = ''.join(p)
    if f.count('р') > 1:
        cnt += 1
print(cnt) # 13


# https://stepik.org/lesson/424708/step/2?auth=login&unit=414440
from itertools import product
cnt = 0
for p in product('катер', repeat=4):
    f = ''.join(p)
    if f.count('р') > 1:
        cnt += 1
print(cnt) # 113


# https://stepik.org/lesson/424708/step/3?auth=login&unit=414440
from itertools import product
cnt = 0
for p in product('муха', repeat=5):
    f = ''.join(p)
    if f.count('у') <= 3:
        cnt += 1
print(cnt) # 1008


# https://stepik.org/lesson/424708/step/4?auth=login&unit=414440
from itertools import product
cnt = 0
for p in product('жираф', repeat=6):
    f = ''.join(p)
    if 1 <= f.count('а') <= 4:
        cnt += 1
print(cnt) # 11504


# https://stepik.org/lesson/424708/step/5?auth=login&unit=414440
# http://dvbogdanov.ru/?page=var1701_task10
from itertools import permutations
cnt = 0
for p in permutations('123333'):
    cnt += '3333' in ''.join(p)
print(cnt) # 144

# Через факториал
from math import factorial as fc
print(fc(3) * fc(4)) # 144

# https://stepik.org/lesson/424708/step/6?auth=login&unit=414440
from itertools import product
cnt = 0
for p in product('абвгде', repeat=4):
    f = ''.join(p)
    if f.count('г') == 1:
        cnt += f[0] == 'г' or f[-1] == 'г'
print(cnt) # 250

# регулярка
from itertools import product
import re
cnt = 0
reg = r'[г][^г]{3}|[^г]{3}[г]'
for p in product('абвгде', repeat=4):
    f = ''.join(p)
    if re.findall(reg, f):
        cnt += 1
print(cnt) # 250
