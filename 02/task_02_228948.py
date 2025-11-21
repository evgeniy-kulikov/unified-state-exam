""""""
"""
Task 02
ЕГЭ по информатике: варианты
https://stepik.org/course/228948
"""


""" 2.4 тест № 2 (пересдача ЕГЭ 2024) """
# https://stepik.org/lesson/1599363/step/3?unit=1621007
from itertools import product
print(*'z,y,x,w')
for z,y,x,w in product((0,1), repeat=4):
    # f = (z <= (not(y <= x))) or w
    f = any([not z, y and not x, w])
    if not f:
        print(z,y,x,w)
# z y x w
# 1 1 1 0
# 1 0 1 0
# 1 0 0 0