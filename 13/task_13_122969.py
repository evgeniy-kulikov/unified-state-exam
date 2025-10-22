""""""
"""
Task 13
Подборка задач для подготовки к ЕГЭ по информатике 2026 | itpy
https://stepik.org/course/122969
"""

""" 2.9 Домашка: 13 номер. """
# https://stepik.org/lesson/1038700/step/3?unit=1062785
from ipaddress import *
for n in range(32, 0, -1):
    net = ip_network(f'163.232.136.60/{n}', 0)
    # if str(net.network_address) == '163.232.136.0':
    if f'{net.network_address}' == '163.232.136.0':
        print(n)  # 26
        break


# https://stepik.org/lesson/1038700/step/4?unit=1062785
from ipaddress import *
cnt = 0
net = ip_network(f'136.36.240.16/255.255.255.248', 0)
for i in net:
    cnt += '101' not in f'{i:b}'
print(cnt)  # 4


# https://stepik.org/lesson/1038700/step/5?unit=1062785
# short
from ipaddress import *
for n in range(32, 1, -1):
    net = ip_network(f'165.112.200.70/{n}', 0)
    if ip_address('165.112.175.80') in net:
        print(n)
        break

# long
from ipaddress import *
for n in range(32, 1, -1):
    net1 = ip_network(f'165.112.200.70/{n}', 0)
    net2 = ip_network(f'165.112.175.80/{n}', 0)
    if net1 == net2:
        print(n)  # 17
        break



