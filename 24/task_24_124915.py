""""""
"""
course_124915
https://stepik.org/course/124915/syllabus
ЕГЭ по информатике 2027 :: Годовой курс
"""


# https://stepik.org/lesson/1015194/step/8?unit=1024864
# аналог задачи 27634 Апробация 04.03.26 (Уровень: Базовый)
f = open('24.txt').readline()
c = l = 0
res = 10**6
for r in range(len(f)):
    c += f[r]=='X'
    while c == 120:
        c -= f[l] =='X'
        res = min(res, r-l+1)  # пока 120 'X' ищем минимум
        l += 1
print(res)  # 1883

# чуть быстрее выполняется
f = open('24.txt').readline()
c = l = 0
res = 10**6
for r in range(len(f)):
    c += f[r]=='X'
    while c >= 120:
        if f[l]=='X':  # в начале и конце строки стоит 'X' и их ровно 120
            res = min(res, r-l+1)
            c -= 1
        l += 1
print(res)  # 1883



# https://stepik.org/lesson/1015194/step/11?unit=1024864
f = open('24.txt').readline()
l = m = k = 0
for r in range(len(f)):
    if f[r-1:r+1] ==  'DE':
        k += 1
    while k > 240:
        if f[l:l+2] == 'DE':
            k -= 1
        l += 1
    m = max(m , r-l+1)  # пока к <= 240
print(m)  # 1792

# variant (дольше)
f = open('24.txt').readline()
s = ''
m = k = 0
for r in range(len(f)):
    s += f[r]
    k += s[-2:]=='DE'
    while k > 240:
        k -= s[:2]=='DE'
        s = s[1:]
    m = max(m, len(s))
print(m)  # 1792



# https://stepik.org/lesson/1015194/step/12?unit=1024864
s = open('24.txt').read()
l = c = res = 0
for r in range(1, len(s)):
    c += s[r-1:r+1] == 'CD'
    while c > 160:
        c -= s[l:l+2] == 'CD'
        l += 1
    if c == 160:
        res = max(res, r-l+1)
print(res)

# variant
f = open('24.txt').readline().replace('CD', 'C D').split()
mx, t = 0, 160
for i in range(len(f) - t):
    mx = max(mx, len(''.join(f[i:i+t+1])))
print(mx)


# https://stepik.org/lesson/1015194/step/13?unit=1024864
from re import findall
f = open('24.txt').readline().strip()
n = r'[7-9]+\d*'
reg = rf'{n}(?:[*-]{n})+'
print(max(map(len, findall(reg, f))))  # 177



# https://stepik.org/lesson/1015194/step/14?unit=1024864
f = open('24.txt').readline()
c = l = 0
m = len(f)
for r in range(len(f)):
    c += f[r-1:r+1] == 'AF'
    while c==201:
        c -= f[l:l+2] == 'AF'
        m = min(m, r-l+1)
        l += 1
print(m)  # 9511

# variant
f = open('24.txt').readline().split('AF')
m, t = 10**6, 201
for i in range(1, len(f) - (t-1)):
    w = ''.join(f[i:i + t-1])
    m = min(m, len(w) + t*2)
print(m)  # 9511



# https://stepik.org/lesson/1015194/step/15?unit=1024864
# 5*0*7*95*0 + 0 + 8*0 + 0 + 0
from re import findall
s = open("24.txt").readline()
n = r'(?:0|[1-9]\d*)'  # 0 or 120
n_mul = rf'(?:{n}\*)*'  # 1*0*2*
mul_n = rf'(?:\*{n})*'  # *3*4*0
mult = rf'(?:{n_mul}0{mul_n})'  # 1*0*2 * 0 * 3*4*0
reg = rf'(?:{mult}(?:\+{mult})*)'  # 1*0*2*0*3*4*0 + 1*0*2*0*3*4*0
print(max(len(i) for i in findall(reg, s)))  # 104



# https://stepik.org/lesson/1015194/step/16?unit=1024864
from re import findall
s = open("24.txt").readline()
n = r'(?:0|[1-9]\d*)'  # 0 or 120
n_mul = rf'(?:{n}\*)*'  # 1*0*2*
mul_n = rf'(?:\*{n})*'  # *3*4*0
mult = rf'(?:{n_mul}0{mul_n})'  # 1*0*2 * 0 * 3*4*0
reg = rf'(?:{mult}(?:\+{mult})*)'  # 1*0*2*0*3*4*0 + 1*0*2*0*3*4*0
print(max(len(i) for i in findall(reg, s)))  # 197



# https://stepik.org/lesson/1579682/step/4?unit=1601041
from re import findall
reg = r'(?:[1-9A-D][0-9A-D]*[02468AC])'
s = open('24.txt').readline()
print(len(max(findall(reg, s), key=len)))  # 2598


