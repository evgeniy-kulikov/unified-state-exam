""""""
"""
Task 12
Подготовка к ЕГЭ информатика
https://stepik.org/course/57248
"""

# https://stepik.org/lesson/552237/step/12?unit=545965
for n in range(50, 1, -1):
    s = '6' * n
    while '66' in s:
        s = s.replace('66', '1', 1)
        s = s.replace('11', '2', 1)
        s = s.replace('22', '6', 1)
    if s == '21':
        print(n)  # 48
        break


# https://stepik.org/lesson/552237/step/13?unit=545965
for x in range(1, 10):
    for y in range(1, 50):
        for z in range(1, 50):
            st = '0' + '1' * x + '2' * y  + '3' * z
            s = st
            while '01' in s or '02' in s or '03' in s:
                s = s.replace('01', '30', 1)
                s = s.replace('02', '3103', 1)
                s = s.replace('03', '1201', 1)
            if s.count('1') == 59 and s.count('2') == 40 and s.count('3') == 66:
                print(st.count('1'))  # 7
                print(st)  # 011111112222222222222222222333333333333333333333
                # break


# https://stepik.org/lesson/552237/step/14?unit=545965
nm = 0
ns_in = ''
ns_out = ''
for y in range(1, 4):
    for x in range(150, 210):
        st = '1' * x + '3' * y
        s = st
        while '12' in s or '13' in s:
            s = s.replace('12', '21', 1)
            s = s.replace('31', '23', 1)
            s = s.replace('13', '23', 1)
        if s.count('1') == 0 and sum(map(int, s)) == 404:
            if len(st) > nm:
                nm = len(st)
                ns_in = st
                ns_out = s
print(nm)  # 201
print(ns_in)  # 11111111.........1133
print(ns_out)  #  22222222........2233
"""
Устное решение.
Длина исходной и конечной строки одинакова. Каждая единица меняется на двойку.
Получается, что конечная строка состоит из двоек, и минимально возможное кол-во троек (2 штуки).
Получаем: (404-6)/2 = 199 двоек + 2 тройки   -->   длина строки 201
"""
#  После устного анализа - короткое и быстрое решение (проверка)
s = '1' * 199 + '33'
while '12' in s or '13' in s:
    s = s.replace('12', '21', 1)
    s = s.replace('31', '23', 1)
    s = s.replace('13', '23', 1)
if s.count('1') == 0 and sum(map(int, s)) == 404:
    print(len(s)) # 201


# https://stepik.org/lesson/552237/step/15?unit=545965
st = '1007' + '0' * 67  #  1008
s = st
while '900' in s or '8000' in s or '70' in s:
    s = s.replace('70', '8', 1)
    s = s.replace('900', '70', 1)
    s = s.replace('8000', '900', 1)
print(s) #  1008


# https://stepik.org/lesson/449926/step/1?auth=login&unit=440312
s = '8' * 65
while '222' in s or '888' in s:
    if '222' in s:
        s = s.replace('222', '8', 1)
    else:
        s = s.replace('888', '2', 1)
print(s)


# https://stepik.org/lesson/449926/step/1?auth=login&unit=440312
cnt = set()
for n in range(1, 1000):  # s = '8' тоже нужна )))
    s = '8' * n
    while '555' in s or '888' in s:
            s = s.replace('555', '8', 1)
            s = s.replace('888', '55', 1)
    cnt.add(s)
print(len(cnt))  # 8
print(cnt)  # {'88', '55', '5588', '558', '8', '85', '8588', '858'}


