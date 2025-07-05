""""""
"""
Task 12
Информатика Подготовка к ЕГЭ 2025
https://stepik.org/course/182932/syllabus
"""

# https://stepik.org/lesson/1341300/step/3?unit=1356964
sm_max = 0
s_max = ''
for i in range(4, 10_000):
    s = '1' + '9' * i
    while '19' in s or '49' in s or '999' in s:
        if '19' in s:
            s = s.replace('19', '9', 1)
        if '49' in s:
            s = s.replace('49', '91', 1)
        if '999' in s:
            s = s.replace('999', '4', 1)
    sm_i = sum(map(int, s))
    # sm_max = max(sm_max, sm_i)
    if sm_i > sm_max:
        sm_max = sm_i
        s_max = s
print(sm_max)  # 23
print(s_max)  # 9914


# https://stepik.org/lesson/1341300/step/4?unit=1356964
for i in range(4, 10_000):
    s = '1' + '8' * i
    while '18' in s or '388' in s or '888' in s:
        if '18' in s:
            s = s.replace('18', '8', 1)
        if '388' in s:
            s = s.replace('388', '81', 1)
        if '888' in s:
            s = s.replace('888', '3', 1)
    if s.count('1') == 3:
        print(i)  # 33
        print(s)  # 811381
        break



# https://stepik.org/lesson/1112640/step/1?unit=1124026
s = '8' * 70
while any(['2222' in s, '8888' in s]):
    s = s.replace('2222', '88')
    s = s.replace('8888', '22')
print(s)  # 22


# https://stepik.org/lesson/1112640/step/2?unit=1124026
s = '2' + '5' * 81
while any(['25' in s, '355' in s, '4555' in s]):
    s = s.replace('25', '4')
    s = s.replace('355', '2')
    s = s.replace('4555', '3')
print(s)  # 455


# https://stepik.org/lesson/1112640/step/3?unit=1124026
s = '1' + '0' * 33
while any(['1' in s, '100' in s]):
    if '100' in s:
        s = s.replace('100', '0001')
    else:
        s = s.replace('1', '00')
print(s)  # 000000000000000000000000000000000000000000000000000
print(len(s))  # 51


# # https://stepik.org/lesson/1112640/step/4?unit=1124026
s = '1' * 46 + '2' * 31
while '1111' in s:
    s = s.replace('1111', '2')
    s = s.replace('222', '1')
print(s)  # 21


# https://stepik.org/lesson/1112640/step/5?unit=1124026
for n in range(50, 1, -1):
    s = '6' * n
    while '66' in s:
        s = s.replace('66', '1')
        s = s.replace('11', '2')
        s = s.replace('22', '6')
    if s == '21':
        print(n)
        break  # 48


# https://stepik.org/lesson/1112640/step/6?unit=1124026
s = '>' + '3' * 30 + '1' * 11 + '2' * 12
while any(['>1' in s, '>2' in s, '>3' in s]):
    s = s.replace('>1', '22>')
    s = s.replace('>2', '2>')
    s = s.replace('>3', '1>')
# print(s)
print(sum(map(int, s[:-1])))  # 98



# https://stepik.org/lesson/1112640/step/7?unit=1124026
def get_one():
    for a in range(1,100):
        for b in range(1, 100):
            for c in range(1, 100):
                s = '0' + '1' * a + '2' * b + '3' * c
                while any(['01' in s, '02' in s, '03' in s]) and len(s) < 110:
                    s = s.replace('01', '302', 1)
                    s = s.replace('02', '3103', 1)
                    s = s.replace('03', '20', 1)
                if all([s.count('1') == 28, s.count('2') == 34, s.count('3') == 45]):
                    return a
print(get_one())  # 17


# https://stepik.org/lesson/1112640/step/10?unit=1124026
res = set()
for n in range(1, 1000):
    s = '5' * n
    while any(['555' in s, '888' in s]):
        s = s.replace('555' , '8', 1)
        s = s.replace('888' , '5', 1)
    res.add(s)
print(len(res))  # 8
print(*sorted(res))  # 5 8 55 85 88 855 885 8855


