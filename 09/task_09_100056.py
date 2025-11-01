""""""
"""
Task 09
https://stepik.org/course/100056
ЕГЭ Информатика
"""

""" 15.1 Решаем вариантик """
# https://stepik.org/lesson/766574/step/7?unit=768992
for f in open('add/course_100056/9.txt'):
    d = list(map(int, f.split()))
    d_2 = [i for i in d if d.count(i) == 2]
    d_1 = [i for i in d if d.count(i) == 1]
    if len(d_2) == 4 and len(d_1) == 3 and max(d) not in d_2:
        print(sum(d))  # 261
        break

