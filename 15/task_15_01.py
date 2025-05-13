""""
Task 15
Подготовка к ЕГЭ информатика
https://stepik.org/course/57248
"""


# https://stepik.org/lesson/454772/step/1?unit=445199
for a in range(1, 300):
    flag = True
    for x in range(1, 1001):
        # if not (not (x % a == 0) or (x % 14 == 0 and x % 21 == 0)):
        # if not (x % a or not (x % 14 or x % 21)):
        if  not(x % a) and (x % 14 or x % 21):
            flag = False
            break
    if flag:
        print(a)  # 42
        break


# https://stepik.org/lesson/454772/step/2?unit=445199
for a in range(1, 300):
    flag = True
    for x in range(1, 1001):
        # if not (not (not (x % 19 == 0) or not (x % 15) == 0) or not (x % a == 0)):
        # if (not (x % 19 == 0) or not (x % 15) == 0) and x % a == 0:
        # if not (not(x % 19) and not (x % 15)) and not (x % a):
        if (x % 19 or x % 15) and not (x % a):
            flag = False
            break
    if flag:
        print(a)  # 285
        break


# https://stepik.org/lesson/454772/step/3?unit=445199
for a in range(1, 300):
    flag = True
    for x in range(1, 1001):
        # if not (not (x % a == 0) or (not (x % a) == 0 or (x % 34 == 0 and x % 51 == 0))):
        # if (x % a == 0) and not (not (x % a) == 0 or (x % 34 == 0 and x % 51 == 0)):
        # if not (x % a) and not ((x % a) or not (x % 34 or x % 51)):
        if not (x % a) and (not (x % a) and (x % 34 or x % 51)):
            flag = False
            break
    if flag:
        print(a)  # 102
        break


# https://stepik.org/lesson/454772/step/4?unit=445199
for a in range(1, 300):
    flag = True
    for x in range(1, 1001):
        # if not(x % a) and not (x % 28 or not (x % 42)):
        if not(x % a) and not (x % 28) and x % 42:
            flag = False
            break
    if flag:
        print(a)  # 3
        break


# # https://stepik.org/lesson/454772/step/5?unit=445199
nm = 0
for a in range(1, 300):
    flag = True
    for x in range(1, 100_001):
        # f =  (x & a != 0) <= ((x & 44 == 0) <= (x & 76 != 0))
        f = not (x & a != 0) or (not (x & 44 == 0) or x & 76 != 0)
        if not f:
            flag = False
            break
    if flag:
        nm = max(a, nm)
print(nm)  # 108


# https://stepik.org/lesson/454772/step/6?unit=445199
for a in range(1, 100):
    for x in range(1, 10_001):
        flg = True
        # f = not (x % a == 0 and not (x % 36 == 0)) or not (x % 12 == 0)
        f = x % a or not x % 36 or x % 12
        if not f:
            flg = False
            break
    if flg:
        print(a)  # 9
        break


# https://stepik.org/lesson/454772/step/7?unit=445199
for a in range(1, 100):
    for x in range(1, 10_001):
        flg = True
        # f = not (x & 56 != 0) or (not (x & 48 == 0) or (x & a != 0))
        f = x & 56 == 0 or x & 48 != 0 or x & a != 0
        if not f:
            flg = False
            break
    if flg:
        print(a)  # 8
        break


# https://stepik.org/lesson/454772/step/8?unit=445199
for a in range(1, 100):
    for x in range(1, 10_001):
        flg = True
        # f = (x & 35 == 0) or ((x & 31 != 0) or x & a != 0)
        f = not (x & 35) or x & 31 or x & a
        if not f:
            flg = False
            break
    if flg:
        print(a)  # 32
        break


# https://stepik.org/lesson/454772/step/9?unit=445199
for a in range(1, 100):
    for x in range(1, 10_001):
        flg = True
        # f = not (x & 76 != 0) or (not (x & 10 == 0) or (x & a != 0))
        f = not x & 76 or x & 10 or x & a

        if not f:
            flg = False
            break
    if flg:
        print(a)  # 68
        break


# https://stepik.org/lesson/454772/step/10?unit=445199
nm = 0
for a in range(1, 100):
    for x in range(1, 10_001):
        flg = True
        # f = not (x % 40 == 0 or x % 64 == 0) or x % a == 0
        f = x % 40 and x % 64 or x % a == 0
        if not f:
            flg = False
            break
    if flg:
        nm = max(a, nm)
print(nm)  # 8


# https://stepik.org/lesson/454772/step/11?unit=445199
for a in range(1, 100):
    for x in range(1, 10_001):
        flg = True
        # f = not (x & 94 != 0) or (not (x & 21 == 0) or x & a != 0)
        f = not x & 94 or x & 21 or x & a
        if not f:
            flg = False
            break
    if flg:
        print(a)  # 74
        break


# https://stepik.org/lesson/454772/step/12?unit=445199
cnt = 0
for a in range(1, 100):
    for x in range(1, 10_001):
        flg = True
        # exp_1 = not (x & 17 != 0) or (not (x & a != 0) or (x & 58 != 0))
        # exp_2 = (x & 8 == 0) and (x & a != 0) and (x & 58 == 0)
        exp_1 = not x & 17 or not x & a or x & 58
        exp_2 = not x & 8 and x & a and not x & 58
        f = not exp_1 or exp_2
        if f:
            flg = False
            break
    if flg:
        cnt += 1
print(cnt)  # 15


# https://stepik.org/lesson/454772/step/13?unit=445199
res = set()
for x in range(1, 1000):
    exp_1 = not (x in set([2, 4, 8, 12, 16]))
    exp_2 = not (x in set([3, 6, 7, 15]))
    exp_3 = not (x in set([3, 6, 7, 15]))
    f = exp_1 and exp_2 or exp_3
    if not f:
        res.add(x)
print(res)  # {3, 15, 6, 7}
print(len(res))  # 4


# https://stepik.org/lesson/454772/step/14?unit=445199
# 15/course_57248/pic/pic_001
a = []
p = [i for i in range(10, 41)]
q = [i for i in range(20, 36)]
for x in range(1, 100):
    # f =  not (x in p and not (x in a)) or not x in q
    # f = not x in p or not x in q or x in a
    f = any([not x in p, not x in q, x in a])
    if not f:
        a.append(x)
print(a)  # [20, 21, 22, 23, ..., 32, 33, 34, 35]
print(len(a) - 1)  # 15


# https://stepik.org/lesson/454772/step/14?unit=445199
# 15/course_57248/pic/pic_002
a = []
p = [i for i in range(80, 104)]
q = [i for i in range(5, 16)]
r = [i for i in range(35, 51)]

for x in range(1, 200):
    exp1 = not x in p or x in q
    exp2 = x in r or x in a
    f = exp1 or exp2
    if not f:
        a.append(x)
print(a)  # [80, 81, 82, 83, 84, 85, ..., 100, 101, 102, 103]
print(len(a) - 1)  # 23


# https://stepik.org/lesson/454772/step/16?unit=445199
# 15/course_57248/pic/pic_003
# a = [i for i in range(80, 91)]
b = [i for i in range(30, 51)]
for n in range(11, 500):
    # c = [i for i in range(10, n)]
    cnt = 10  # уже дает отрезок "a"
    for x in range(30, 1000):
        # exp1 = x in a or x in b
        # exp2 = x in a or x in c
        # f = exp1 and exp2
        f = x in b
        if not f:
            break
        else:
            cnt += 1
        if cnt > 25:
            print(x)  # 45  в ответе 44 - я не согласен!!!
            #  https://www.cyberforum.ru/informatics/thread3063327.html
            # print(c)
            break


#  https://stepik.org/lesson/623846/step/1?unit=619531
# 15/course_57248/pic/pic_004
# p = set([i * 2 for i in range(1, 11)])
# q = set([i * 3 for i in range(1, 11)])
p = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
a = set()
for x in range(1, 1000):
    a.add(x)
    # exp1 = not x in a or not x in p
    # exp2 = not x in a or x in q
    # f = exp1 and exp2
    f = not x in a or (not x in p and x in q)
    if not f:
        a.remove(x)
print(a)  # {3, 9, 15, 21, 24, 27, 30}
print(len(a))  # 7


# https://stepik.org/lesson/623846/step/2?unit=619531
for r in range(10, 51):
    flag = True
    for a in range(1, 1000):
        for x in range(1, 1000):
            exp1 = x & 54 == 0 or x & 45 == 0
            exp2 = x & a == 0 or x & r == 0
            # if  not exp1 or exp2:
            if  exp1 and not exp2:
                flag = False
    if flag:
        print(r)  # 32


#  https://stepik.org/lesson/623846/step/3?unit=619531
# 15/course_57248/pic/pic_005
d = [*range(155, 178)]
b = [*range(111, 161)]
a_min = [*range(100, 200)]
def fn(ls: list):
    while ls:
        n = ls.pop()
        for x in range(1, 1000):
            # f = not x in d or (not (not x in b and not x in a) or not x in d)
            # f = not x in d or (( x in b or  x in a) or not x in d)
            # f =  x in b or x in a or not x in d
            f = any([x not in d, x in b, x in ls])
            if not f:
                ls.append(n)
                return ls
a_min = fn(a_min)
a_min.reverse()
a_min = fn(a_min)
print(a_min[::-1])  # [161, 162, 163, 164, ..., 175, 176, 177]
print(len(a_min))  # 17


#  https://stepik.org/lesson/623846/step/4?unit=619531
# 15/course_57248/pic/pic_006
a = [*range(60, 91)]
b = [*range(30, 51)]
cnt = 30  # 30 чисел дает отрезок A
for n in range(100):
    flag = True
    c = [*range(35, 35 + n)]
    for x in range(30, 51):
        # f = x in a or (x in b or x in c)
        f = x in b or x in c
        if not f:
            flag = False
            break
    if flag:
        cnt += 1
    if cnt == 35:
        print(35 + n)  # 39
        break


#  https://stepik.org/lesson/623846/step/5?unit=619531
# 15/course_57248/pic/pic_007

#  https://stepik.org/lesson/623846/step/6?unit=619531
# 15/course_57248/pic/pic_008

#  https://stepik.org/lesson/623846/step/7?unit=619531
# 15/course_57248/pic/pic_009


# https://stepik.org/lesson/623846/step/8?unit=619531
num = -100
for a in range(-20, 0):  # 'a'  положительным быть не может
    flag = True
    for k in range(100):
        for m in range(100):
            f = (k + m > 12) or ((k - 10 > a) and (m + 10 > a))
            if not f:
                flag = False
                break
    if flag:
        num = max(num, a)
print(num)  #  -11


# https://stepik.org/lesson/623846/step/9?unit=619531
# Решать нужно глазами
nm = 0
for a in range(6500, 6600):
    if  a < (81 ** 2 + 15):
        nm = max(nm, a)
print(nm)  # 6575


# https://stepik.org/lesson/623846/step/10?unit=619531
nm = -100
for a in range(-100, 100):
    flag = True
    for x in range(1, 500):
        for y in range(1, 500):
            f = (3 * y - x > a) or (2 * x + 3 * y < 30) or (2 * y - x < -31)
            if not f:
                flag = False
    if flag:
        nm = max(nm, a)
print(nm)  # -31


# https://stepik.org/lesson/623846/step/10?unit=619531
def fn(a):  # сокращаем лишние итерации вложенных циклов
    for x in range(1, 500):
        for y in range(1, 500):
            f = (3 * y - x > a) or (2 * x + 3 * y < 30) or (2 * y - x < -31)
            if not f:
                return False
    return True

nm = -100
for a in range(-100, 100):
    if fn(a):
        nm = max(nm, a)
print(nm)  # -31


# https://stepik.org/lesson/623846/step/11?unit=619531
for a in range(1, 2000):
    flag = True
    for x in range(1, 100000):
        # f = not (not (x % 84 == 0) or not (x % 90 == 0)) or not (x % a == 0)
        f = not x % 84 and not x % 90 or x % a
        if not f:
            flag = False
            break
    if flag:
        print(a)  # 1260
        break

# https://stepik.org/lesson/623846/step/12?unit=619531
for a in range(1, 1000):
    flag = True
    for x in range(1, 100000):
        # f = not ((x % a == 0) and (x % 36 == 0)) or (x % 324 == 0 and a > 100)
        f = x % a or x % 36 or (not x % 324 and a > 100)
        if not f:
            flag = False
            break
    if flag:
        print(a)  # 162
        break


#  https://stepik.org/lesson/667646/step/1?unit=668403
# 15/course_57248/pic/pic_010.jpg

#  https://stepik.org/lesson/667646/step/2?unit=668403
# 15/course_57248/pic/pic_011.jpg

#  https://stepik.org/lesson/667646/step/3?unit=668403
# 15/course_57248/pic/pic_012.jpg

#  https://stepik.org/lesson/667646/step/4?unit=668403
# 15/course_57248/pic/pic_013.jpg

#  https://stepik.org/lesson/667646/step/5?unit=668403
# 15/course_57248/pic/pic_014.jpg

#  https://stepik.org/lesson/667646/step/6?unit=668403
# 15/course_57248/pic/pic_015.jpg

#  https://stepik.org/lesson/667646/step/7?unit=668403
# 15/course_57248/pic/pic_016.jpg

#  https://stepik.org/lesson/667646/step/8?unit=668403
# 15/course_57248/pic/pic_017.jpg

#  https://stepik.org/lesson/667646/step/9?unit=668403
# 15/course_57248/pic/pic_018.jpg

#  https://stepik.org/lesson/667646/step/10?unit=668403
# 15/course_57248/pic/pic_019.jpg

#  https://stepik.org/lesson/667646/step/11?unit=668403
# 15/course_57248/pic/pic_020.jpg

#  https://stepik.org/lesson/667646/step/12?unit=668403
# 15/course_57248/pic/pic_021.jpg

#  https://stepik.org/lesson/667646/step/13?unit=668403
# 15/course_57248/pic/pic_022.jpg

#  https://stepik.org/lesson/667646/step/14?unit=668403
# 15/course_57248/pic/pic_023.jpg

#  https://stepik.org/lesson/667646/step/15?unit=668403
# 15/course_57248/pic/pic_024.jpg

#  https://stepik.org/lesson/667646/step/16?unit=668403
# 15/course_57248/pic/pic_025.jpg











