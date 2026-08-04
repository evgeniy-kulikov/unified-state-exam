""""""
"""
task 17
https://stepik.org/course/72713/syllabus
Подготовка к ЕГЭ по информатике
"""

# https://stepik.org/lesson/603962/step/5?unit=599239
f = [*map(int, open('17.txt'))]
c = mx = 0
for a, b in zip(f, f[1:]):
    if any([not a%7 and not b%17, not b%7 and a%17]):
        c += 1
        mx = max(mx, a+b)
print(c, mx)  # 2510 19632


# https://stepik.org/lesson/603962/step/6?unit=599239
f = [*map(int, open('17.txt'))]
c = mn = 0
for a, b in zip(f, f[1:]):
    if any([str(a)[-1]=='6' and not a%3, str(b)[-1]=='6' and not b%3]):
        c += 1
        mn = min(mn, a, b)
print(c, abs(mn))  # 587 9996


# https://stepik.org/lesson/603962/step/11?unit=599239 🌶️🌶️🌶️
f = [*map(int, open('17.txt'))] + ['*']  # '*' для обработки в конце списка убывающей последовательности
l = 1
d = dict()
for a, b in zip(f, f[1:]):
    if b != '*' and a > b:
        l += 1
    else:
        d.setdefault(l, 0)
        d[l] += 1
        l = 1
d = sorted(d.items())
print(d[-1])  #  72


# https://stepik.org/lesson/408053/step/2?unit=397335
c = M = 0
for n in range(1014, 9639, 3):
    if all(n % i for i in (11,13,17,19)):
        c += 1
        M = max(M, n)
print(c, M)  # 2151 9630


# https://stepik.org/lesson/408053/step/3?unit=397335
c, M = 0, 5321
for n in range(980, 5321):
    if any(not n%i for i in (4,5)) and all(n%i for i in (11,17,19,23)):
        c += 1
        M = min(M, n)
print(c, M)  # 1353 980


# https://stepik.org/lesson/408053/step/6?unit=397335
c, M = 0, 8433
for n in range(3712, 8433):
    if any(not n%i for i in (13, 14, 15)) and n%4 == n%2:
        c += 1
        M = min(M, n)
print(c, M)  # 471 3720


# https://stepik.org/lesson/408053/step/8?unit=397335
r = []
for n in range(2807, 8559):
    if f'{n:b}'[-2:] == '11' and n%9 == 5:
        r.append(n)
print(max(r), sum(r))  # 8555 910880


# https://stepik.org/lesson/545757/step/1?unit=539329
r = []
for n in range(2248, 6483):
    if all(not i%2 for i in map(int, str(n))):
        r.append(n)
print(len(r), sum(r), sep='') # 283 1227630


# https://stepik.org/lesson/545757/step/5?unit=539329
def f(n):
    r = set()
    for i in range(1, int(n**0.5)+1):
        if not n % i:
            r |= {i, n//i}
    return len(r) > 17

r = [i for i in range(10_001, 50_001) if f(i)]
print(len(r), min(r), sep='')  # 6585 10008

