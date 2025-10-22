""""""
"""
Task 14
Подборка задач для подготовки к ЕГЭ по информатике 2026 | itpy
https://stepik.org/course/122969
"""

""" 2.3 Домашка: 14 номер """
# https://stepik.org/lesson/1038703/step/2?unit=1062210
res = set()
n = 11*15 ** 65 + 18*15**38 - 14*15**17 + 19*15**11 + 18338
while n:
    res |= {n % 15}
    n //= 15
print(len(res))  # 10

# long way
def conv(n, b):
    alf = '0123456789abcdef'
    r = ''
    while n:
        r = str(alf[n % b]) + r
        n //= b
    return r

n = 11*15 ** 65 + 18*15**38 - 14*15**17 + 19*15**11 + 18338
r = conv(n, 15)
print(len(set(r)))  # 10


# https://stepik.org/lesson/1038703/step/3?unit=1062210
for x in '0123456789abcde'[::-1]:
    n = int(f'1{x}51', 15) - int(f'3{x}2', 15)
    if not n % 4:
        print(n // 4)  # 1376
        break


# https://stepik.org/lesson/1038703/step/4?unit=1062210
res = []
for x in '0123456':
    for y in '0123456':
        n = int(f'{y}{x}320', 7) + int(f'1{x}3{y}3', 9)
        if not n % 181:
            res.append(n // 181)
print(min(res))  # 148


# https://stepik.org/lesson/1038703/step/5?unit=1062210
for x in range(1, 2031):
    n = 6**260 + 6**160 + 6**60 - x
    cnt = 0
    while n:
        cnt += not n % 6
        n //= 6
    if cnt == 202:
        print(x)  # 216
        break


# https://stepik.org/lesson/1038703/step/7?unit=1062210
n = 766**66 + 15**13 - 22
cnt = 0
while n:
    cnt += n % 13 == 12
    n //= 13
print(cnt)  # 10


# https://stepik.org/lesson/1038703/step/8?unit=1062210
for x in '0123456789abcde':
    n = int(f'97531{x}19', 15) + int(f'3{x}519', 15)
    if not n % 11:
        print(n // 11)  # 147416793
        break




