""""""
"""
Task 12
ЕГЭ по информатике: варианты
https://stepik.org/course/228948
"""

""" 2.4 тест № 2 (пересдача ЕГЭ 2024) """
# https://stepik.org/lesson/1599363/step/13?unit=1621007
s = '9' * 134
while '22222' in s or '9999' in s:
    if '22222' in s:
        s = s.replace('22222', '99', 1)
    else:
        s = s.replace('9999', '2', 1)
print(s)