""""""
"""
Task 13
ЕГЭ Питоныч
https://stepik.org/course/100138
"""

""" 25.1 Основы IP-адресации """

# https://stepik.org/lesson/1190361/step/3?unit=1203331
b = '11000000.10101000.00000101.00010011'
d = [str(int(i, 2)) for i in b.split('.')]
print('.'.join(d))  # 192.168.5.19


# https://stepik.org/lesson/1190361/step/12?unit=1203331
from ipaddress import ip_network
print(ip_network('208.128.193.64/255.255.224.0', 0))
# 208.128.192.0/19



""" 25.2 Решение задач. Часть 1 """

# https://stepik.org/lesson/1190362/step/2?unit=1203332
from ipaddress import ip_network

cnt = 0
net = ip_network('156.128.0.227/255.255.255.248', 0)  # 156.128.0.224
for i in net.hosts():
    cnt += 1
    if str(i) == '156.128.0.227':
        print(cnt, i)  # 3  156.128.0.227

# https://stepik.org/lesson/1190362/step/7?unit=1203332
from ipaddress import *
for m in range(17, 33):
    net = ip_network(f'148.228.120.242/{m}', 0)
    if str(net.network_address) == '148.228.112.0':
        m_3 = ('1' * m).ljust(32, '0')[16:24]
        print(m_3)  # 11110000
        print(int(m_3, 2))  # 240

# конвертирование десятичного IP адреса в двоичный
def bin_ip(s: str):
    return '.'.join(f'{int(i):b}'.zfill(8) for i in s.split('.'))
host = '148.228.120.242'
net = '148.228.112.0'
print(bin_ip(host))
print(bin_ip(net))
"""
10010100.11100100.01111000.11110010       # host
11111111.11111111.11110000.00000000       # 11110000 --> 240
10010100.11100100.01110000.00000000       # net
"""


# https://stepik.org/lesson/1190362/step/8?unit=1203332
from ipaddress import *
for m in range(17, 33):
    net = ip_network(f'153.209.31.240/{m}', 0)
    if str(net.network_address) == '153.209.28.0':
        m_3 = ('1' * m).ljust(32, '0')[16:24]
        print(m_3)  # 11111100
        print(int(m_3, 2))  # 252


# https://stepik.org/lesson/1190362/step/12?unit=1203332
from ipaddress import *
net = ip_network('64.128.194.208/255.255.240.0', 0)
print(net)  # 64.128.192.0/20


""" 25.3 Решение задач. Часть 2 """

# https://stepik.org/lesson/1190363/step/2?unit=1203333
from ipaddress import *
for m in range(33):
    net = ip_network(f'148.228.120.242/{m}', 0)
    if str(net.network_address) == '148.228.112.0':
        # print(net.netmask)  # 255.255.240.0
        print(str(net.netmask).split('.')[2])  # 240
        break


# https://stepik.org/lesson/1190363/step/7?unit=1203333
from ipaddress import *
for m in range(33):
    net = ip_network(f'68.112.69.138/{m}', 0)
    if str(net.network_address) == '68.112.64.0':
        print(m)
# 21


# https://stepik.org/lesson/1190363/step/10?unit=1203333
from ipaddress import *
for m in range(33):
    net = ip_network(f'15.51.208.15/{m}', 0)
    if str(net.network_address) == '15.51.192.0':
        msk = ('1' * m).ljust(32, '0')
        print(int(msk[16:24], 2))
# 224


""" 25.4 Решение задач. Часть 3 """

# https://stepik.org/lesson/1192962/step/2?unit=1205951
from ipaddress import *
for m in range(33):
    net_1 = ip_network(f'112.117.107.70/{m}', 0)
    net_2 = ip_network(f'112.117.121.80/{m}', 0)
    if net_1 == net_2:
        # print(net_1.netmask)
        print(str(net_1.netmask).split('.')[2])
# 224


# https://stepik.org/lesson/1192962/step/6?unit=1205951
from ipaddress import *
for m in range(33):
    net_1 = ip_network(f'151.172.115.121/{m}', 0)
    net_2 = ip_network(f'151.172.115.156/{m}', 0)
    if net_1 != net_2:
        print(m)  # 25
        break


# https://stepik.org/lesson/1192962/step/11?unit=1205951
from ipaddress import *
net = ip_network('1.2.3.0/255.255.255.0', 0)
print(net.num_addresses - 2)  # 254
# 256 - 2 = 254


""" 25.5 Решение задач. Часть 4 """

# https://stepik.org/lesson/1192963/step/2?unit=1205952
from ipaddress import *
cnt = 0
net = ip_network('172.16.128.0/255.255.192.0', 0)
for n in net:
    cnt += f'{n:b}'.count('1') % 2
print(cnt)  # 8192


# https://stepik.org/lesson/1192963/step/7?unit=1205952
from ipaddress import *
cnt = 0
net = ip_network('192.168.248.176/255.255.255.240', 0)
for n in net:
    cnt += f'{n:b}'.count('1') > 16
print(cnt)  # 1


# https://stepik.org/lesson/1192963/step/8?unit=1205952
from ipaddress import *
cnt = 0
net = ip_network('211.48.136.64/255.255.255.224', 0)
for n in net:
    cnt += f'{n:b}'[-2:] == '11'
print(cnt)  # 8


# https://stepik.org/lesson/1192963/step/11?unit=1205952
from ipaddress import *
cnt = 0
net = ip_network('140.19.96.0/255.255.248.0', 0)
for n in net:
    ls = [f'{n:b}'[i:i + 8].count('1') for i in range(0, 32, 8)]
    cnt += len(set(ls)) == 1
print(cnt)  # 168
