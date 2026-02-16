""" https://kompege.ru/task """
"""
10578 10773
12245
17627 
23372
"""




# 10578 (Уровень: Базовый)
from ipaddress import *
for m in range(1, 33):
    net_1 = ip_network(f'10.96.180.231/{m}', False)
    net_2 = ip_network(f'10.96.140.118/{m}', False)
    if net_1 != net_2:
        print(32 - m)  # 13
        break

# 10773 (Уровень: Базовый)
from ipaddress import *
c = 0
for m in range(1, 33):
    net = ip_network(f'133.57.64.130/{m}', False)
    c += str(net) == f'133.57.64.0/{m}'
print(c)  # 7



# 12245 ЕГКР 16.12.23 (Уровень: Базовый)
from ipaddress import *
net = ip_network('192.168.32.48/255.255.255.240', False)
c = 0
for i in net:
    c += f'{i:b}'.count('1') % 2
print(c)  # 8


# 17627 Основная волна 19.06.24 (Уровень: Базовый)
from ipaddress import *
for n in range(32, 0, -1):
    net = ip_network(f'111.91.200.28/{n}', False)
    if str(net) == f'111.91.192.0/{n}':
    # if str(net.network_address) == '111.91.192.0':
    # if str(net).split('/')[0] == '111.91.192.0':
        print(32 - n)  # 12
        break


# 23372 Резервный день 19.06.25 (Уровень: Базовый)
from ipaddress import *
net = ip_network('73.148.145.65/255.224.0.0', False)
print(str(net[-2]).replace('.', ''))  # 73159255254


