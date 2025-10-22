""""""
"""
Task 05
Подборка задач для подготовки к ЕГЭ по информатике 2026 | itpy
https://stepik.org/course/122969
"""


""" 2.1 Домашка: 5 номер. """
#  https://stepik.org/lesson/1038432/step/2?unit=1060804
def f(b: str):
    if not b.count('1') % 2:
        return '11' + b[2:] + '00'
    return '10' + b[2:] + '11'

res = set()
for n in range(100):
    b = f(f'{n:b}')
    b = f(b)
    res |= {int(b, 2)}
print(max(res))  # 1584


# https://stepik.org/lesson/1038432/step/3?unit=1060804
for n in range(1, 100):
    b = f'{n:b}'
    if not b.count('1') % 2:
        b = '101' + b[3:] + '0'
    else:
        b = '10' + b[2:] + '11'
    if int(b, 2) > 68:
        print(n)  # 19
        break


# https://stepik.org/lesson/1038432/step/4?unit=1060804
for n in range(1, 100):
    b = f'{n:b}'
    b = b.replace('0', '*').replace('1', '0').replace('*', '1')
    b = '1' + b
    b += ('0', '1')[b.count('1') % 2]
    if int(b, 2) > 180:
        print(n)  # 32
        break


# https://stepik.org/lesson/1038432/step/5?unit=1060804
res = set()
for n in range(1, 1000):
    b = f'{n:b}'
    for _ in range(2):
        b += str(b.count('1') % 2)
    r = int(b, 2)
    if r > 75:
        res |= {r}
print(min(res))  # 78


# https://stepik.org/lesson/1038432/step/5?unit=1060804
for n in range(1, 100):
    b = f'{n:b}'
    if not b.count('1') % 2:
        b = '10' + b[2:] + '1'
    else:
        b = '1' + b[2:] + '11'
    if int(b, 2) >= 100:
        print(n)  # 41
        break


# https://stepik.org/lesson/1038432/step/8?unit=1060804
res = set()
for n in range(100, 1001):
    b = f'{n:b}'.replace('0', '')
    res |= {int(b, 2)}
print(len(res))  # 9


# https://stepik.org/lesson/1038432/step/9?unit=1060804
res = set()
for n in range(1, 1000):
    b = f'{n:b}'
    if not n % 2:
        b = '1' + b + '00'
    else:
        b += f'{b.count("1"):b}'
    r = int(b, 2)
    if r > 190:
        res |= {(r, n)}
print(min(res)[1])  # 16


# https://stepik.org/lesson/1038432/step/12?unit=1060804
MX = 0
for n in range(1, 100):
    b = f'{n:b}'
    for _ in '12':
        if not b.count('1') % 2:
        # if not sum(map(int, b)) % 2:
            b = '11' + b[2:] + '00'
        else:
            b = '10' + b[2:] + '11'
    MX = max(MX, int(b, 2))
print(MX)  # 1584


# https://stepik.org/lesson/1038432/step/14?unit=1060804
for n in range(1001, 10**5):
    b = f'{n:b}'[::-1]
    if int(b, 2) == 29:
        print(n)  # 1472
        break







""" 2.2 Практика: 5 номер """

# https://stepik.org/lesson/1228668/step/4?unit=1242201
def conv(n, b):
    r = ''
    while n:
        r = str(n % b) + r
        n //= b
    return r

for n in range(1000, 1, -1):
    r = conv(n, 4)
    if not len(r) % 2:
        i = len(r) // 2
        r = r[:i] + '0' + r[i:]
    if int(r, 4) <= 180:
        print(n)  # 63
        break

