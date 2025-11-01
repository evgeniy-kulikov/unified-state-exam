""""""
"""
Task 24
Подборка задач для подготовки к ЕГЭ по информатике 2026 | itpy
https://stepik.org/course/122969
"""

MX = 0
with open('add/course_122969/24_11.txt') as file:
    s = file.read().strip()
    for l in range(len(s) - 1):
        cnt = 1
        for r in range(l, len(s)):
            row = s[l:r + 2]
            if row[-2].isdigit() == row[-1].isalpha():
                cnt += 1
                MX = max(MX, cnt)
            else:
                break
print(MX)  # 22


""" 4.5 Домашка: 24 номер. """

# https://stepik.org/lesson/1038834/step/2?unit=1062779
# s = open('add/course_122969/24 4-5_01.txt').readline()
with open('add/course_122969/24_4_5_01.txt') as file:
    s = file.read().strip()
    res = 0
    cnt = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            cnt = 1
        else:
            cnt += 1
            res = max(res, cnt)
    print(res)


# https://stepik.org/lesson/1038834/step/3?unit=1062779
cnt = 0
with open('add/course_122969/24_4_5_02.txt') as file:
    s = file.read()
    for i in range(len(s)):
        cnt += s[i:i+5] == 'OKTOS'
print(cnt)  # 309

# short
with open('add/course_122969/24_4_5_02.txt') as file:
    s = file.read()
    print(s.count('OKTOS'))  # 309


# https://stepik.org/lesson/1038834/step/4?unit=1062779
res = 0
cnt = 0
with open('add/course_122969/24_4_5_03.txt') as file:
    s = file.read()
    for i in range(0, len(s), 2):
        if s[i] in 'CDF' and s[i + 1] in 'AU':
            cnt += 1
            res = max(res, cnt)
        else:
            cnt = 0
print(res)  # 173

# re
from re import *
reg = r'(?:[CDF][AU])+'
with open('add/course_122969/24_4_5_03.txt') as file:
    ls = findall(reg, file.read())
    res = max(ls, key=len)
print(len(res) // 2)  # 173


# https://stepik.org/lesson/1038834/step/5?unit=1062779
from re import *
a = r'[7-9]\d*'
b = r'[-*][7-9]\d*'
reg = f'{a}(?:{b})+'
with open('add/course_122969/24_4_5_04.txt') as file:
    ls = findall(reg, file.read())
    res = max(ls, key=len)
    print(len(res))  # 40


# https://stepik.org/lesson/1038834/step/7?unit=1062779
from re import *
reg = r'F.O'
cnt = 0
with open('add/course_122969/24_4_5_05.txt') as file:
    for fl in file:
        cnt += len(findall(reg, fl)) > 0
    print(cnt)  # 757

cnt = 0
with open('add/course_122969/24_4_5_05.txt') as file:
    for fl in file:
        for i in range(len(fl) - 2):
            if fl[i] + fl[i+2] == 'FO':
                cnt += 1
                break
    print(cnt)


# https://stepik.org/lesson/1038834/step/8?unit=1062779
# Искомые строки A***D  или  D***A  из A***D****A  >>>  A***D D****A
with open('add/course_122969/24_4_5_06.txt') as file:
    s = file.read()
    s = s.replace('A', 'A A').replace('D', 'D D')
    s = s.split()
    MX = 0
    for i in s:
        # if i.count('D') == 1 and i.count('A') == 1:
        if 'A' in i and 'D' in i:
            MX = max(MX, len(i))
    print(MX)


# https://stepik.org/lesson/1038834/step/9?unit=1062779
from re import *
reg = r'(?:[24][135])+'
with open('add/course_122969/24_4_5_07.txt') as file:
    s = file.read()
    ls = findall(reg, s)
    res = max(ls, key=len)
    print(len(res) // 2)  # 10

with open('add/course_122969/24_4_5_07.txt') as file:
    s = file.read()
    s = s.replace('3', '1').replace('5', '1').replace('4', '2')
    s = s.replace('21', '*').replace('2', ' ').replace('1', ' ')
    res = max(s.split(), key=len)
    print(len(res))  # 10



# https://stepik.org/lesson/1038834/step/10?unit=1062779
# О-Ч-Е-Н-Ь ДОЛГО ((((
with open('add/course_122969/24_4_5_08.txt') as file:
    s = file.read()
    m = 0
    for l in range(len(s)):
        for r in range(m, len(s) + 1):
            row = s[l:r]
            if row.count('CD') > 161:
                break
            if row.count('CD') == 160:
                m = max(m, len(row))
    print(m)  # 9712

# # var 1
# https://informatikaexpert.ru/sredi-kotoryx-para-simvolov-cd-v-ukazannom-poryadke-vstrechaetsya-rovno-160-raz/
with open('add/course_122969/24_4_5_08.txt') as file:
    s = file.read()
    l = k = 0
    m = 0
    for r in range(1, len(s)):
        if s[r - 1] + s[r] == 'CD':
            k += 1
        while k > 160:
            if s[l] + s[l + 1] == 'CD':
                k -= 1
            l += 1
        if k == 160:
            m = max(m, r - l + 1)
    print(m)  # 9712

# var 2  (быстрый)
# https://informatikaexpert.ru/sredi-kotoryx-para-simvolov-cd-v-ukazannom-poryadke-vstrechaetsya-rovno-160-raz/
with open('add/course_122969/24_4_5_08.txt') as file:
    s = file.read()
    ls = s.replace('CD', 'C D').split()
    m = 0
    for i in range(len(ls) - 161):
        st = ''.join(ls[i:i + 161])
        m = max(m, len(st))
print(m)  # 9712


# https://stepik.org/lesson/1038834/step/12?unit=1062779
with open('add/course_122969/24_4_5_09.txt') as file:
    MX = 0
    s = file.read()
    ls = s.replace('DD', 'D D').split()
    for i in ls:
        if 'FE' in i:
            MX = max(MX, len(i))
    print(MX)  # 2486


# https://stepik.org/lesson/1038834/step/13?unit=1062779
with open('add/course_122969/24_4_5_10.txt') as file:
    cnt = 0
    s = file.read()
    for i in range(len(s) - 3):
        cnt += s[i:i+4] == 'XXXX'
    print(cnt)  # 12263


# https://stepik.org/lesson/1038834/step/14?unit=1062779
with open('add/course_122969/24_4_5_11.txt') as file:
    cnt = 0
    s = file.read()
    s = s.replace('A', ' ').replace('B', ' ').replace('C', ' ').split()
    res = max(len(i) for i in s)
    print(res)  # 20


# https://stepik.org/lesson/1038834/step/15?unit=1062779
with open('add/course_122969/24_4_5_12.txt') as file:
    MX = 0
    cnt = 3
    s = file.read()
    for i in range(len(s) - 3):
        if s[i:i+4] in 'KLMNKLM':
            cnt += 1
            MX = max(MX, cnt)
        else:
            cnt = 3
    print(MX)  # 182

# long code
with open('add/course_122969/24_4_5_12.txt') as file:
    MX = 0
    cnt = 0
    s = file.read()
    s = '123' + s.replace('KLMN', '*') + '123'
    for i in range(len(s)):
        if s[i] == '*':
            cnt += 4
            if s[i-1] == 'N':
                cnt += sum([s[i-2] == 'M', s[i-3:i-1] == 'LM']) + 1
            if s[i+1] == 'K':
                cnt += sum([s[i+2] == 'L', s[i+2:i+4] == 'LM']) + 1
            MX = max(MX, cnt)
        else:
            cnt = 0
    print(MX)  # 182



""" 4.6 Практика: 24 номер. """
# https://stepik.org/lesson/1228676/step/2?unit=1242209
with open('add/course_122969/24_4_6_01.txt') as file:
    MX = 0
    cnt = 4
    s = file.read()
    for i in range(len(s) - 4):
        if s[i:i+5] in 'VWXYZVWXY':
            cnt += 1
            MX = max(MX, cnt)
        else:
            cnt = 4
    print(MX)  # 40


# https://stepik.org/lesson/1228676/step/3?unit=1242209
with open('add/course_122969/24_4_6_02.txt') as file:
    MX = 0
    cnt = 0
    l = 0
    s = file.read()
    for r in range(1, len(s)):
        if s[r-1:r+1] == 'AB':
            cnt += 1
        while cnt > 100:
            if s[l:l+2] == 'AB':
                cnt -= 1
            l += 1
        if cnt == 100:
            MX = max(MX, r-l+1)
    print(MX)  # 750


# https://stepik.org/lesson/1228676/step/4?unit=1242209
with open('add/course_122969/24_4_6_03.txt') as file:
    MX = 0
    cnt = 2
    s = file.read()
    for i in range(len(s) - 2):
        if s[i: i+3] in 'RSQRS':
            cnt += 1
            MX = max(MX, cnt)
        else:
            cnt = 2
    print(MX)  # 54


# https://stepik.org/lesson/1228676/step/5?unit=1242209
with open('add/course_122969/24_4_6_04.txt') as file:
    s = file.read().split('Y')
    ls = [i for i in s if i.count('X') >= 500]  # отсекаем лишнее

    MX = 10**6
    for row in ls:
        l = cnt = 0
        for r in range(len(row)):
            if row[r] == 'X':
                cnt += 1
            while cnt >= 500:
                MX = min(MX, r - l + 1)
                if row[l] == 'X':
                    cnt -= 1
                l += 1
    print(MX)  # 68500


# https://stepik.org/lesson/1228676/step/6?unit=1242209
with open('add/course_122969/24_4_6_05.txt') as file:
    s = file.read().strip()
    s = s.replace('*', '-')
    while '--' in s:
        s = s.replace('--', '  ')
    s = s.replace('6', '9').replace('7', '9').replace('8', '9')
    m = 0
    for row in s.split():
        if len(row) > m:
            for l in range(len(row)):
                for r in range(l + 1, len(row)):
                    st = row[l:r + m].strip('-')
                    if all(['-' in st, '-00' not in st, '-09' not in st, st[:2] not in '009']):
                        m = max(m, len(st))
    print(m)


# https://stepik.org/lesson/1228676/step/7?unit=1242209
with open('add/course_122969/24_4_6_06.txt') as file:
    s = file.read().rstrip()
    MX = 0
    # D и C остаются на концах элементов списка
    s = s.replace('C', 'C ').replace('D', 'D ').split()
    for i in range(len(s) - 4):
        # Только в 5-ти элементах списка (5-й без последней буквы (D или C)) может быть условие *
        row = ''.join(s[i:i + 5])[:-1]
        if row.count('D') <= 2 and row.count('C') <= 2:  # условие *
            MX = max(MX, len(row))
    print(MX)  # 253



# https://stepik.org/lesson/1228676/step/8?unit=1242209
with open('add/course_122969/24_4_6_07.txt') as file:
    MX = 0
    s = file.read().rstrip()
    s = s.replace('*', ' ').replace('++', ' ').split()
    for r in s:
        r = r.strip('+')
        if '+' in r:
            MX = max(MX, eval(r))
print(MX)  # 9988877898985

from re import *
reg = r'(?:\d+(\+\d+)+)'
MX = 0
with open('add/course_122969/24_4_6_07.txt') as file:
    s = file.read()
    res = finditer(reg, s)
    for i in res:
        dig = i.group()
        if dig:
            MX = max(MX, eval(dig))
    print(MX)  # 9988877898985


# https://stepik.org/lesson/1228676/step/9?unit=1242209
from re import *
reg = '[1-9A-F][0-9A-F]*'
with open('add/course_122969/24_4_6_08.txt') as file:
    MX = 0
    s = file.read()
    res = finditer(reg, s)
    for i in res:
        MX = max(MX, len(i.group()))
    print(MX)  # 21


# https://stepik.org/lesson/1228676/step/9?unit=1242209
with open('add/course_122969/24_4_6_08.txt') as file:
    s = file.read().strip()
    bad = set(s) - set('0123456789ABCDEF')
    for i in bad:
        s = s.replace(i, ' ')
    MX = max(len(i) for i in s.split() if i[0] != '0')
    print(MX)  # 21


# https://stepik.org/lesson/1228676/step/10?unit=1242209
with open('add/course_122969/24_4_6_09.txt') as file:
    MX = 0
    s = file.read().strip()
    s = s.replace('T', 'T ').split()
    for i in range(len(s) - 101):
        r = ''.join(s[i:i+101])[:-1]
        if len(r) > MX:
            MX = max(MX, len(r))
    print(MX)  # 133

with open('add/course_122969/24_4_6_09.txt') as file:
    MX = 0
    cnt = l = 0
    s = file.read().strip()
    for r in range(len(s)):
        cnt += s[r] == 'T'
        while cnt > 100:
            if s[l] == 'T':
                cnt -= 1
            l += 1
        if cnt == 100:
            MX = max(MX, r - l + 1)
    print(MX)  # 133


# https://stepik.org/lesson/1228676/step/11?unit=1242209
with open('add/course_122969/24_4_6_10.txt') as file:
    MX = 0
    cnt = 1
    s = file.read().strip()
    s = s.replace('B', 'A').replace('C', 'A').replace('8', '9')
    for i in range(1, len(s)):
        if s[i-1] != s[i]:
            cnt += 1
            MX = max(MX, cnt)
        else:
            cnt = 1
    print(MX)  # 18



# https://stepik.org/lesson/1228676/step/12?unit=1242209
with open('add/course_122969/24_4_6_11.txt') as file:
    MX = 0
    s = file.read().strip().replace('Y', 'Y ').split()
    for i in range(len(s) - 151):
        r = ''.join(s[i:i+151])[:-1]
        if len(r) > MX:
            MX = max(MX, len(r))
    print(MX)  # 244


# Тоже самое, но быстрее
# https://stepik.org/lesson/1228676/step/12?unit=1242209
with open('add/course_122969/24_4_6_12.txt') as file:
    MX = 0
    s = file.read().strip()
    t = [i for i, v in enumerate(s) if v == 'Y']
    for i in range(len(t) - 151):
        cnt = t[i + 151] - t[i] - 1
        if cnt > MX:
            MX = cnt
    print(MX)  # 244



with open('add/course_122969/24_4_6_12.txt') as file:
    MX = 0
    s = '+' + file.read().strip().replace('*', '+')  # '+' +  если строка начнется с нулей
    while '++' in s or '+0' in s:
        s = s.replace('++', '+ +')
        s = s.replace('+0', ' +')  # удаление незначащих нулей
    for el in s.split():
        el = el.strip('+')  # удаление краевых '+'
        if '+' in el:
            MX = max(MX, el.count('+') + 1)
    print(MX)  # 44


from re import *
reg = r'[1-9]\d*(?:\+[1-9]\d*)+'
with open('add/course_122969/24_4_6_12.txt') as file:
    MX = 0
    s = file.read().replace('*', '+')
    res = finditer(reg, s)
    for el in res:
        MX = max(MX, el.group().count('+') + 1)
    print(MX)  # 44


# # https://stepik.org/lesson/1228676/step/14?unit=1242209
from re import *
reg = r'\d[A-Z]+\d'
odd = '13579'
with open('add/course_122969/24_4_6_13.txt') as file:
    MX = 0
    s = file.read()
    res = finditer(reg, s)
    for el in res:
        r = el.group()
        if sum([r[0] in odd, r[-1] in odd]) == 1:
            MX = max(MX, len(r))
    print(MX)  # 49


with open('add/course_122969/24_4_6_13.txt') as file:
    s = file.read()
    for i in '0468':
        s = s.replace(i, '2')
    for i in '3579':
        s = s.replace(i, '1')
    s = s.replace('1', '1 1').replace('2', '2 2')
    print(max(len(x) for x in s.split() if '1' in x and '2' in x))  # 49


# # https://stepik.org/lesson/1228676/step/15?unit=1242209
with open('add/course_122969/24_4_6_14.txt') as file:
    s = file.read()
    s = s.replace('O', 'A').replace('D', 'C').replace('F', 'C')
    s = s.replace('CAAC', 'CAA AAC').split()  # CAAC
    res = max(len(i) for i in s)
    print(res)  # 599


# # https://stepik.org/lesson/1228676/step/16?unit=1242209
with open('add/course_122969/24_4_6_15.txt') as file:
    s = file.read()
    cnt = 0
    s = s.replace('A', 'A A').split()
    for i in s[1:-1]:
        cnt += 'B' not in i and len(i) >= 17
    print(cnt)  # 597


""" 4.7 Проверочная: Работа с файлами, номера: 9, 17, 24 """
# https://stepik.org/lesson/1231755/step/8?unit=1245338
from re import *
reg = r'(?:\d{2}[DR])+'
with open('add/course_122969/24_4_7_01.txt') as file:
    s = file.read()
    res = max(len(i) for i in findall(reg, s))
    print(res // 3)  # 67

with open('add/course_122969/24_4_7_01.txt') as file:
    s = file.read()
    s = s.replace('8', '1').replace('R', 'D').replace('11D', '*')
    s = s.replace('1', ' ').replace('D', ' ').split()
    res = max(len(i) for i in s)
    print(res)  # 67


# https://stepik.org/lesson/1231755/step/9?unit=1245338
with open('add/course_122969/24_4_7_02.txt') as file:
    MX = 0
    s = file.read().strip()
    for i in 'AEIOUY':
        s = s.replace(i, f'{i} {i}')
    s = s.split()
    for i in range(len(s) - 1):
        r = s[i][1:-1] + s[i+1][:-1]
        cnt = 1
        for i in range(len(r) - 1):
            if r[i] < r[i+1]:
                cnt += 1
                MX = max(MX, cnt)
            else:
                cnt = 1
    print(MX)


# https://stepik.org/lesson/1231755/step10?unit=1245338
with open('add/course_122969/24_4_7_03.txt') as file:
    MX = 0
    s = file.read().strip()
    for l in range(len(s) - 1):
        for r in range(l + 1, len(s)):
            if s[r] == s[l]:
                MX = max(MX, r - l + 1)
                break
    print(MX)  # 9747




