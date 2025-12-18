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


# https://stepik.org/lesson/1695808/step/8?unit=1719160
# https://kompege.ru/task   № 10574 (Уровень: Базовый)
from ipaddress import *
cnt = 0
for n in range(1, 33):
    net = ip_network(f'158.116.11.146/{n}', 0)
    cnt += str(net.network_address) == '158.116.0.0'
print(cnt)  # 7


# https://stepik.org/lesson/1695808/step/9?unit=1719160
#  https://kompege.ru/task  № 10573 (Уровень: Базовый)
from ipaddress import *
for n in range(32, 0, -1):
    net = ip_network(f'191.173.145.240/{n}', False)
    if str(net.network_address) == '191.173.144.0':
        print(2 ** (32 - n))  # 512
        # print(len([*net]))  # 512
        break


# https://stepik.org/lesson/1695808/step/10?unit=1719160
# https://kompege.ru/task   № 10576 (Уровень: Базовый)
from ipaddress import *
net = ip_network(f"0.0.0.0/255.255.240.0", 0)
print(len([*net.hosts()]))  # 4094

# без всякой мудрости 😉
print((256 - 240) * 256 - 2)  # 4094




# https://stepik.org/lesson/1695808/step/12?unit=1719160
#  https://kompege.ru/task  № 10578 (Уровень: Базовый)
from ipaddress import *
for n in range(1, 33):
    net1 = ip_network(f'10.96.180.231/{n}', False)
    net2 = ip_network(f'10.96.140.118/{n}', False)
    if net1 != net2:
        print(32 - n)  # 13
        break


# https://stepik.org/lesson/1695808/step/11?unit=1719160
# https://kompege.ru/task   № 10577 (Уровень: Базовый)
from ipaddress import *
for n in range(32, 0, -1):
    net1 = ip_network(f'165.112.200.70/{n}', 0)
    net2 = ip_network(f'165.112.175.80/{n}', 0)
    if net1 == net2:
        print(n)  # 17
        break




""" 13.2 Задание 13 | Задачи прошлых лет """
# https://stepik.org/lesson/1695809/step/1?unit=1719161
# https://kompege.ru/task   № 10095 Демоверсия 2024 (Уровень: Средний)
from ipaddress import *
cnt = 0
net = ip_network(f'192.168.32.160/255.255.255.240', 0)
for i in net:
    cnt += not f'{i:b}'.count('1') % 2
print(cnt)  # 8


# https://stepik.org/lesson/1695809/step/2?unit=1719161
#  https://kompege.ru/task  № 15326 Досрочная волна 2024 (Уровень: Базовый)
from ipaddress import *
cnt = 0
net = ip_network(f'105.224.200.224/255.255.255.224', False)
for i in net:
    if not f'{i:b}'.count('1') % 4:
        cnt += 1
print(cnt)  # 10


# https://stepik.org/lesson/1695809/step/3?unit=1719161
# https://kompege.ru/task   № 17526 Основная волна 07.06.24 (Уровень: Базовый)
from ipaddress import *
cnt = 0
net = ip_network(f'172.16.128.0/255.255.192.0', 0)
for i in net:
    cnt += f'{i:b}'.count('1') % 8192
print(cnt)  # 8


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




""" Варианты """
# 28.1 Вариант 1 | Часть 1
# https://stepik.org/lesson/1729565/step/1?unit=1753394
#  https://kompege.ru/task  № 17867 Демоверсия 2025 (Уровень: Базовый)
from ipaddress import *
cnt = 0
net = ip_network('172.16.168.0/255.255.248.0', 0)
for i in net:
    cnt += f'{i:b}'.count('1') % 5 != 0
print(cnt)  # 1663


# 29.1 Вариант 2 | Часть 2
# https://stepik.org/lesson/1729899/step/1?unit=1753726
# https://kompege.ru/task  № 19245 ЕГКР 21.12.24 (Уровень: Базовый)
from ipaddress import *
net = ip_network('218.194.82.148/255.255.255.192', 0)
print(str(net[-2]).replace('.', ''))  # 21819482190


# 30.1 Вариант 3 | Часть 1
# https://stepik.org/lesson/1730528/step/1?unit=1754357
# https://kompege.ru/task  № 20807 Апробация 05.03.25 (Уровень: Базовый)
from ipaddress import *
c = 0
net = ip_network('172.16.192.0/255.255.192.0', False)
for i in net:
    c += f'{i:b}'.count('1') % 5 != 0
print(c)  # 13003


# 31.2 Вариант 4 | Часть 2
# https://stepik.org/lesson/1736670/step/1?unit=1760676
# https://kompege.ru/task  № 21412 Досрочная волна 2025 (Уровень: Базовый)
from ipaddress import *
net = ip_network('143.168.72.213/255.255.255.240', False)
print(str(net[-2]).replace('.', ''))  # 14316872222


