""" https://kompege.ru/task """
"""
10105
26551 27069 27634
"""

# 10105 Демоверсия 2024 (Уровень: Средний)
st = open('24_10105.txt').readline()
res = c = l = 0
for r in range(len(st)):
    if st[r] == 'T':
        c += 1
    while c > 100:
        if st[l] == 'T':
            c -= 1
        l += 1
    if c == 100:
        res = max(res, r - l + 1)
print(res)  # 133




# 26551 (Уровень: Базовый)
from re import *
s = open('add/24/24_26551.txt').read()
reg = r'[1-9A-D][0-9A-D]*[0248AC]'  # четное
res = findall(reg, s)
print(len(max(res, key=len)))  # 2598


# 27069 (Уровень: Средний)
from re import *
s = open('add/24/24_27069.txt').read()
w1 = r'(?:[A-Z][a-z]*)'
w2 = r'(?:\s[A-Za-z][a-z]*)*'
reg = rf'{w1}{w2}\.'
res = findall(reg, s)
ans = max(res, key=len)
print(ans)  # You are a genius.
print(len(ans.split()))  # 4


# 27634 Апробация 04.03.26 (Уровень: Базовый) ✔️
"""поиск минимальной длины строки"""
res = 10**10
l = c = 0
s = open('add/KIM_25163454/24_27634.txt').readline().strip()
for r in range(len(s)):
    if s[r] == 'Z':
        c += 1
    while c > 269:  # 270 - 1
        if s[l] == 'Z':  # в начале и конце строки стоит 'Z' и их ровно 270
            res = min(res, r - l + 1)
            c -= 1
        l += 1
print(res)  # 1058


