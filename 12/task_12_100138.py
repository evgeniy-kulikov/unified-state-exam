""""""
"""
Task 12
ЕГЭ Питоныч
https://stepik.org/course/100138
"""

""" 41.1 Задачи с циклом и условием внутри """

# https://stepik.org/lesson/769415/step/4?unit=771844
s = '2' * 10
while '111' in s or '222' in s:
    if '111' in s:
        s = s.replace('111', '2', 1)
    else:
        s = s.replace('222', '1', 1)
print(s)


""" 41.2 Задачи с циклом без условия внутри """

# https://stepik.org/lesson/769416/step/2?unit=771845
s = '7' * 8
while '7777' in s:
    s = s.replace('7777', '55', 1)
    s = s.replace('555', '7', 1)
print(s)  # 75


""" 41.3 Задачи с неизвестной начальной строкой """

# https://stepik.org/lesson/769416/step/2?unit=771845
# s = '>' + '1' * 10 + '2' * 10 + '3' * 10
s = '>' + '123' * 10
while '>1' in s or '>2' in s or '>3' in s:
    s = s.replace('>1', '22>', 1)
    s = s.replace('>2', '2>', 1)
    s = s.replace('>3', '1>', 1)
# print(s)  # 2221222122212221222122212221222122212221>
print(sum(map(int, s[:-1])))  # 70


# https://stepik.org/lesson/769416/step/3?unit=771845
s = '>' + '123' * 20
while any(['>1' in s, '>2' in s, '>3' in s]):
    s = s.replace('>1', '22>', 1)
    s = s.replace('>2', '2>', 1)
    s = s.replace('>3', '>', 1)
# print(s)  # 222222222222222222222222222222222222222222222222222222222222>
print(sum(map(int, s[:-1])))  # 120


""" 41.3 Задачи с неизвестной начальной строкой """

# https://stepik.org/lesson/769417/step/11?unit=771846
for i in range(3, 100):
    s = '1' * i
    while '111' in s:
        s = s.replace('111', '2', 1)
        s = s.replace('222', '1', 1)
    if s == '21':
        print(i)  # 4
        break

