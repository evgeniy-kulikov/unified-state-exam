""" https://kompege.ru/task """
"""
10578 10715 10773 10786 10788 10789 11662 11779 11780 11787 11794 11835
12088 12245 12947 17627 17632
23372 23559
"""


# 10578 (Уровень: Базовый)
from ipaddress import *
for m in range(1, 33):
    net_1 = ip_network(f'10.96.180.231/{m}', False)
    net_2 = ip_network(f'10.96.140.118/{m}', False)
    if net_1 != net_2:
        print(32 - m)  # 13
        break


# 10715 (Уровень: Средний)
from ipaddress import *
c = 0
net = ip_network('192.168.32.160/255.255.255.240')
for i in net:
    c += f'{i:b}'.count('0') > 21
print(c)  # 11


# 10773 (Уровень: Базовый)
from ipaddress import *
c = 0
for m in range(1, 33):
    net = ip_network(f'133.57.64.130/{m}', False)
    c += str(net) == f'133.57.64.0/{m}'
print(c)  # 7


# 10786 (Уровень: Средний)
from ipaddress import *
for m in range(1, 33):
    net1 = ip_network(f'151.172.115.121/{m}', 0)
    net2 = ip_network(f'151.172.115.156/{m}', 0)
    if net1 != net2:
        print(m)  # 25
        break


# 10788 (Уровень: Базовый)
from ipaddress import *
c = 0
for m in range(1, 33):
    net1 = ip_network(f'201.44.240.33/{m}', 0)
    net2 = ip_network(f'201.44.240.107/{m}', 0)
    if net1 == net2:
        c += f'{net1.network_address:b}'.count('1') >= 5
print(c)  # 15


# 10789 (Уровень: Базовый)
from ipaddress import *
c = 0
for m in range(1, 33):
    net = ip_network(f'203.75.227.102/{m}', 0)
    if str(net.network_address) == '203.75.224.0':
        c += 1
print(c)  # 4


# 11662 (Уровень: Базовый)
from ipaddress import *
c = 0
net = ip_network('123.222.111.192/255.255.255.248', 0)
for i in net:
    c += f'{i:b}'[24:].count('1') % 3 != 0
print(c)  # 5


# 11779 (Уровень: Базовый)
from ipaddress import *
c = 0
net = ip_network('151.192.0.0/255.224.0.0', 0)
for i in net:
    c += f'{i:b}'.count('1') == 16
print(c)  # 293930


# 11780 (Уровень: Базовый)
from ipaddress import *
res = 0
net = ip_network('185.8.0.0/255.255.128.0')
for i in net:
    res = max(res, f'{i:b}'.count('1'))
print(res)  # 11


# 11787 (Уровень: Базовый)
from ipaddress import *
c = 0
net = ip_network('101.157.240.0/255.255.252.0', 0)
for i in net:
    c += f'{i:b}'[:16].count('1') > f'{i:b}'[16:].count('1')
print(c)  # 386


# 11794 (Уровень: Базовый)
from ipaddress import *
for n in range(255, -1, -1):
    net = ip_network(f'223.167.{n}.167/255.255.255.192', 0)
    if all(f'{i:b}'[:16].count('0') <= f'{i:b}'[16:].count('0') for i in net):
        print(n)  # 248
        break


# 11835 (Уровень: Средний)
from ipaddress import *
def f(i):
    a = f'{i:b}'[:16].count('0')
    b = f'{i:b}'[16:].count('0')
    return a > b
c = 0
for n in range(256):
    net = ip_network(f'207.0.{n}.167/255.255.255.192', False)
    c += all(f(i) for i in net)
print(c)  # 37




# 12088 (Уровень: Средний)
from ipaddress import *
c = 0
net = ip_network('112.154.132.0/255.255.252.0')
for i in net.hosts():  #  узлов (устройств)
    a = f'{i:b}'[:16].count('1')
    b = f'{i:b}'[16:].count('0')
    if b % 2:
        c += a <= b
print(c)  # 502


# 12245 ЕГКР 16.12.23 (Уровень: Базовый)
from ipaddress import *
net = ip_network('192.168.32.48/255.255.255.240', False)
c = 0
for i in net:
    c += f'{i:b}'.count('1') % 2
print(c)  # 8


# 12947 (Уровень: Базовый)
from ipaddress import *
c = 0
net = ip_network('203.111.195.0/255.255.240.0', 0)
for i in net:
    b = f'{i:b}'
    c += not b.count('0') % 3 and '111' in b and '000' in b
print(c)  # 1043


# 17627 Основная волна 19.06.24 (Уровень: Базовый)
from ipaddress import *
for n in range(32, 0, -1):
    net = ip_network(f'111.91.200.28/{n}', False)
    if str(net) == f'111.91.192.0/{n}':
    # if str(net.network_address) == '111.91.192.0':
    # if str(net).split('/')[0] == '111.91.192.0':
        print(32 - n)  # 12
        break


# 17632 Основная волна 19.06.24 (Уровень: Базовый)
from ipaddress import *
c = 0
net = ip_network('112.160.0.0/255.240.0.0', 0)
for i in net:
    c += not f'{i:b}'.count('1') % 5
print(c)  # 215766




# 23372 Резервный день 19.06.25 (Уровень: Базовый)
from ipaddress import *
net = ip_network('73.148.145.65/255.224.0.0', False)
print(str(net[-2]).replace('.', ''))  # 73159255254


# 23559 Пересдача 03.07.25 (Уровень: Базовый)
from ipaddress import *
net = ip_network('102.162.200.51/255.255.255.0', 0)
r = str(net[-2])
print(sum(map(int, r.split('.'))))  # 718


