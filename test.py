"""
😉
🙂
🤔
👍
✅
❌
🌶
"""
""""""
# ЕГЭ Информатика 2026 | Полный Курс
# https://stepik.org/course/233165
# variant
""" Варианты """
# variant  (high speed)
# variant  (slow speed)
# best variant
""""""

# https://stepik.org/lesson/1038609/step/4?unit=1062783
# https://kompege.ru/task  № 1551
""""""
from math import log2

# № 24620 (Уровень: Сложный)
"""
1_SD = 300 - 1  = 299 шт.  (1200 / 4) + 1 on SD_5
3840 * 5160 * 24 * 300 * 100 / n = 4 * 2**33
"""
n = 1200
if n % 4:
    sd = n // 4 + 1
else:
    sd = n // 4
for i in range(100, 0, -1):
    if 3840 * 5160 * 24 * sd * ((100 - i) / 100) > 4 * 2**33:  # как только не умещается 300-е фото...
        print(i)  # 75
        break

















