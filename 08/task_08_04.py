""""""
"""
Task 08
ЕГЭ по информатике: варианты
https://stepik.org/course/228948
"""


""" егэ-2024, день 1 """
# https://stepik.org/lesson/1594698/step/9?unit=1616271
from re import fullmatch

reg = r'[0246][0-7]*[^26]'
cnt = 0
for n in range(int('10000', 8), int('77777', 8) + 1):
    b = oct(n)[2:]
    if fullmatch(reg, b) and b.count('7') <= 2:
        cnt += 1
print(cnt)


""" 2.4 тест № 2 (пересдача ЕГЭ 2024) """
# https://stepik.org/lesson/1599363/step/9?unit=1621007
def b4(n):
    a = 'ailm'
    r = ''
    while n:
        r += a[n % 4]
        n //= 4
    return r[::-1].rjust(5, 'a')

for n in range(int('33333', 4), 0, -1):
    s = b4(n)
    if all([not 'l' in s, not 'm' in s,  not 'ii' in s]):
        print(n + 1)  # 274 iaiai
        break

# Вариант
from itertools import product
cnt = mx = 0
for p in product('ailm', repeat=5):
    cnt += 1
    s = ''.join(p)
    if all([not 'l' in s, not 'm' in s, not 'ii' in s]):
        mx = max(cnt, mx)
print(mx)  # 274


""" тест № 3 (егэ 2023) """
# https://stepik.org/lesson/1609595/step/9?unit=1631351
from itertools import product
cnt = 0
for p in product('ЕКМОПРТЬЮ', repeat=5):
    cnt += 1
    if all([not cnt % 2, p[0] != 'Ь', p.count('К') == 2]):
        print(cnt, p)

