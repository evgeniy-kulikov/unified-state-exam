""""""
"""
Task 13
ЕГЭ Информатика 2026 | Полный Курс
https://stepik.org/course/233165

all from https://kompege.ru/task
"""


""" 13.1 Задание 13 | Урок 1 """
# https://stepik.org/lesson/1695808/step/3?unit=1719160
# https://kompege.ru/task   № 10569 (Уровень: Базовый)
from ipaddress import *
net = ip_network('10.8.248.131/255.255.224.0', 0)
print(net.network_address)  # 10.8.224.0
# FADE


# https://stepik.org/lesson/1695808/step/4?unit=1719160
#  https://kompege.ru/task  № 10575 (Уровень: Базовый)
from ipaddress import *
for n in range(1,33):
    net = ip_network(f'118.193.30.139/{n}', False)
    if str(net.network_address) == '118.193.24.0':
        print(net.netmask)  # 255.255.248.0


# https://stepik.org/lesson/1695808/step/5?unit=1719160
# https://kompege.ru/task   № 10570 (Уровень: Базовый)
from ipaddress import *
for n in range(32, 0, -1):
    net = ip_network(f'154.201.208.17/{n}', 0)
    if str(net.network_address) == '154.201.192.0':
        msk = str(net.netmask).split('.')
        print(msk[2])  # 224
        break


# https://stepik.org/lesson/1695808/step/6?unit=1719160
#  https://kompege.ru/task  № 10571 (Уровень: Базовый)
from ipaddress import *
for n in range(1,33):
    net = ip_network(f'122.21.49.91/{n}', False)
    if str(net.network_address) == '122.21.48.0':
        print(n)  # 20
        break


# https://stepik.org/lesson/1695808/step/7?unit=1719160
#  https://kompege.ru/task  № 10572 (Уровень: Базовый)
from ipaddress import *
for n in range(1,33):
    net = ip_network(f'173.103.25.118/{n}', False)
    if str(net.network_address) == '173.103.24.0':
        print(32 - n)  # 11
        break


# https://stepik.org/lesson/1695808/step/9?unit=1719160
#  https://kompege.ru/task  № 10573 (Уровень: Базовый)
from ipaddress import *
for n in range(32, 0, -1):
    net = ip_network(f'191.173.145.240/{n}', False)
    if str(net.network_address) == '191.173.144.0':
        print(2 ** (32 - n))  # 512
        # print(len([*net]))  # 512
        break


# https://stepik.org/lesson/1695808/step/12?unit=1719160
#  https://kompege.ru/task  № 10578 (Уровень: Базовый)
from ipaddress import *
for n in range(1, 33):
    net1 = ip_network(f'10.96.180.231/{n}', False)
    net2 = ip_network(f'10.96.140.118/{n}', False)
    if net1 != net2:
        print(32 - n)  # 13
        break



""" 13.2 Задание 13 | Задачи прошлых лет """
# https://stepik.org/lesson/1695809/step/2?unit=1719161
#  https://kompege.ru/task  № 15326 Досрочная волна 2024 (Уровень: Базовый)
from ipaddress import *
cnt = 0
net = ip_network(f'105.224.200.224/255.255.255.224', False)
for i in net:
    if not f'{i:b}'.count('1') % 4:
        cnt += 1
print(cnt)  # 10


# https://stepik.org/lesson/1695809/step/4?unit=1719161
#  https://kompege.ru/task  № 17554 Основная волна 08.06.24 (Уровень: Базовый)
from ipaddress import *
net = ip_network(f'112.160.0.0/255.240.0.0', False)
print(sum(1 for n in net if f'{n:b}'.count('1') % 3))  # 699050


# https://stepik.org/lesson/1695809/step/7?unit=1719161
#  https://kompege.ru/task  № 23197 Основная волна 10.06.25 (Уровень: Базовый)
from ipaddress import *
net = ip_network(f'45.172.106.203/255.255.252.0', False)
print(str(net[-2]).replace('.', ''))  # 45172107254


