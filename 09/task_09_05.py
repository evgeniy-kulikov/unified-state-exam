""""""
"""
Task 09
ЕГЭ по информатике: варианты
https://stepik.org/course/228948
"""

""" 2.1 тест № 1 (егэ-2024, день 1) """
# https://stepik.org/lesson/1594698/step/10?unit=1616271
cnt = 0
with open('test.txt') as fl:  # копируем таблицу в файл
    for n in fl:
        ls = sorted(map(int, n.split()))
        if sum(ls[:3]) > ls[-1] and len(set(ls)) == 3:
            cnt += 1
print(cnt)



""" 2.4 тест № 2 (пересдача ЕГЭ 2024) """
# https://stepik.org/lesson/1599363/step/10?unit=1621007
with open('9_alles.txt') as fl:
    cnt = 0
    for s in fl:
        n = sorted(map(int, s.split()))
        cnt += n[0] + n[-1] < sum(n[1:-1])
print(cnt)  # 9997


""" егэ 2023 """
# https://stepik.org/lesson/1609595/step/10?unit=1631351
with open('9_alles.txt') as fl:
    cnt = 0
    for f in fl:
        cnt += 1
        d = list(map(int, f.split()))
        one = [i for i in d if d.count(i) == 1]
        two = [i for i in d if d.count(i) == 2]
        if len(one) == 4 and len(two) == 2 and two[0] >= sum(one) / 4:
            print(cnt, d)  # 34 [62, 21, 70, 82, 47, 82]
            break
