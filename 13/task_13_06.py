""""""
"""
Task 13
ЕГЭ по информатике: варианты
https://stepik.org/course/228948
"""

""" 2.1 тест № 1 (егэ-2024, день 1) """
# https://stepik.org/lesson/1594698/step/14?unit=1616271
from ipaddress import *
cnt = 0
net = ip_network('172.16.128.0/255.255.192.0')
for n in net:
    cnt += not f'{int(n):b}'.count('1') % 2
print(cnt)  # 8192


""" 2.4 тест № 2 (пересдача ЕГЭ 2024) """
# https://stepik.org/lesson/1599363/step/14?unit=1621007
from ipaddress import *
cnt = 0
net = ip_network('115.192.0.0/255.192.0.0', 0)
for n in net:
    cnt += bool(f'{n:b}'.count('1') % 3)
print(cnt) # 2796202
