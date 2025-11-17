""""""
"""
Task 12
ЕГЭ Информатика 2026 | Полный Курс
https://stepik.org/course/233165
"""


""" 12.1 Задание 12 | Урок 1 """
# https://stepik.org/lesson/1695399/step/3?unit=1718750
#  https://kompege.ru/task  № 24174 (Уровень: Базовый)
# пусть n0 = кол-ву нулей, а n2 = кол-ву двоек => n1 = 2 * n2 (кол-ву единиц)
for n0 in range(1000):
    for n2 in range(1000):
        str1 = '0' * n0 + '1' * 2 * n2 + '2' * n2  # формируем нашу строку
        if len(str1) == 1000:  # проверяем, что строка имеет именно 1000 символов
            sum1 = sum(map(int, str1))
            str2 = str1.replace('1', '+')  # защита от наложения замен друг на друга
            str2 = str2.replace('2', '1').replace('0', '2').replace('+', '0')
            sum2 = sum(map(int, str2))
            if sum2 == sum1 + 1640:
                print(str1.count('0'))  # 880

# variant
for n2 in range(1, 1001):
    n1 = 2 * n2
    n0 = 1000 - n1 - n2
    sum1 = n1 + 2 * n2
    sum2 = 2 * n0 + n2
    if sum1 == sum2 - 1640:
        print(n0)