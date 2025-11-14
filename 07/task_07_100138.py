""""""
"""
Task 07
ЕГЭ Питоныч
https://stepik.org/course/100138
"""

"""  И37.1 Графика """

# https://stepik.org/lesson/768104/step/4?unit=770458
for i in range(2, 100):
    if 512 * 256 * i / 8 / 1024 > 160:
        print(2 ** (i - 1))  # 1024
        break