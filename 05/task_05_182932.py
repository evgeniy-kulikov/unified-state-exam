""""""
"""
Task 05
Информатика Подготовка к ЕГЭ 2025
https://stepik.org/course/182932/syllabus
"""

# https://stepik.org/lesson/1135848/step/1?unit=1147478
def convert(num):
    sm = sum(map(int, num))
    return num + str(sm % 2)

for n in range(10_000):
    # b = bin(n)[2:]
    b = f'{n:b}'
    num = convert(convert(b))
    if int(num, 2) > 80:
        print(int(num, 2))  # 86
        break


# https://stepik.org/lesson/1135848/step/2?unit=1147478
for n in range(2, 10_000):
    n_bin = bin(n)[2:]
    n_bin = n_bin + n_bin[-1]
    n_bin = n_bin + ['1', '0'][not n_bin.count('1') % 2]
    n_bin = n_bin + ['1', '0'][not n_bin.count('1') % 2]

    if int(n_bin, 2) > 130:
        print(bin(n)[2:])  # 10001
        print(n_bin)  # '10001110'
        print(n)  # 17
        break


# https://stepik.org/lesson/1135848/step/6?unit=1147478
for n in range(100, 0, -1):
    b = f'{n:b}'
    b = b[::-1].lstrip('0')
    if int(b, 2) == 13:
        print(n)  # 88
        break


# https://stepik.org/lesson/1135848/step/4?unit=1147478
def conv(n):
    res = ''
    while n:
        res = str(n % 3) + res
        n //= 3
    return res

for n in range(3, 100):
    num = conv(n)
    num += str(n % 3)
    if int(num, 3) > 99:
        print(int(num, 3))  # 103
        break

# https://stepik.org/lesson/1135848/step/6?unit=1147478
cnt = 0
for n in range(1, 1000):
    b = f'{n:b}'
    b += str(sum(map(int, b)) % 2)
    b += str(b.count('1') % 2)
    if int(b, 2) < 80:
        cnt += 1
print(cnt)


# https://stepik.org/lesson/1135848/step/7?unit=1147478
for n in range(100, 0, -1):
    b = f'{n:b}'
    if not b.count('1') % 2:
        b += '0'
        b = '10' + b[2:]
    else:
        b += '1'
        b = '11' + b[2:]
    if int(b, 2) < 35:
        print(n)  # 24
        break


# https://stepik.org/lesson/1135848/step/8?unit=1147478
def conv(n):
    t = ''
    while n:
        t = str(n % 3) + t
        n //= 3
    return t

for n in range(1000, 0, -1):
    t = conv(n)
    if not n % 3:
        t = '1' + t + '02'
    else:
        t += conv((n % 3) * 4)
    if int(t, 3) < 199:
        print(n)  # 20
        break


# https://stepik.org/lesson/1135848/step/9?unit=1147478
def conv(n):
    s = ''
    while n:
        s = str(n % 6) + s
        n //= 6
    return s

for n in range(1, 1000):
    sx = conv(n)
    if not n % 3:
        sx = sx + sx[:2]
    else:
        sx += conv((n % 3) * 10)
    if int(sx, 6) > 680:
        print(int(sx, 6))  # 694
        break


# https://stepik.org/lesson/1135848/step/9?unit=1147478
def conv(n):
    s = ''
    while n:
        s = str(n % 6) + s
        n //= 6
    return s

for n in range(1, 1000):
    sx = conv(n)
    if not n % 3:
        sx += sx[:2]
    else:
        sx += conv((n % 3) * 10)
    if int(sx, 6) > 680:
        print(int(sx, 6))  # 694
        break


# https://stepik.org/lesson/1135848/step/10?unit=1147478
def conv(n):
    s = ''
    while n:
        s = str(n % 3) + s
        n //= 3
    return s

for n in range(1000, 0, -1):
    tr = conv(n)
    if not n % 4:
        tr += tr[-3:]
    else:
        tr += conv((n % 4) * 4)
    if int(tr, 3) < 127:
        print(int(tr, 3))  # 121
        break


# https://stepik.org/lesson/1135848/step/11?unit=1147478
for n in range(1, 1000):
    b = f'{n:b}'
    if not n % 3:
        b += b[-3:]
    else:
        b += f'{(n % 3) * 3:b}'
    if int(b, 2) > 151:
        print(int(b, 2))  # 166
        break

