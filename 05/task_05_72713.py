""""""
"""
course_72713
task_**_72713
task **
https://stepik.org/course/72713/syllabus
Подготовка к ЕГЭ по информатике
"""

# https://stepik.org/lesson/707568/step/5?unit=708074
for n in range(9999, 1001, -1):
    a,b,c,d = map(int, str(n))
    d = sorted([a+b, b+c, c+d])
    if int(str(d[1]) + str(d[0])) == 127:
        print(n)  # 9934
        break


# https://stepik.org/lesson/707568/step/11?unit=708074
from itertools import product
cnt = 0
for p in product('13579', repeat=4):
    a,b,c,d = map(int, p)
    n = sorted([a+b, c+d])
    # cnt += int(str(n[0]) + str(n[1])) == 414
    cnt += n == [4, 14]
print(cnt)  # 12


# https://stepik.org/lesson/707568/step/7?unit=708074
for n in range(999, 99, -1):
    a,b,c = map(int, str(n))
    ls = sorted([a**2 + b**2, b**2 + c**2])
    if str(ls[1]) + str(ls[0]) == '9752':
        print(n)  # 946
        break


# https://stepik.org/lesson/1207854/step/3?unit=1221088
for n in range(1, 1000):
    b = f'{n:b}'
    if n % 3:
        b += f'{n%3 * 3:b}'
    else:
        b += b[-3:]
    if int(b, 2) >= 76:
        print(n)  # 11
        break


# https://stepik.org/lesson/1340034/step/5?unit=1356035
res = 0
for i in range(11, 1000, 2):
    n = i
    b = ''
    while n:
        b = str(n % 4) + b
        n //= 4
    if i % 3:
        b += str(i % 3)
    else:
        b = b[-1] + b[1:-1] + b[0] + '1'
    if int(b, 4) <= 340:
        res = max(res, int(b, 4))
print(res)  # 334


