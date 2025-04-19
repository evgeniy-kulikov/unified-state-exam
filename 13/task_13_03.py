""""""
"""
Task 13
Информатика Подготовка к ЕГЭ 2025
https://stepik.org/course/182932/syllabus
"""

# https://stepik.org/lesson/1247108/step/1?unit=1260931
from ipaddress import *
net = ip_network('10.8.248.131/255.255.224.0', 0)
print(str(net)) # 10.8.224.0/19
# FADE

from ipaddress import *
for m in range(33):
    net = ip_network(f'118.193.30.139/{m}', 0)
    if str(net.network_address) == '118.193.24.0':
        print(net.netmask)  # 255.255.248.0
        # 248

# https://stepik.org/lesson/1247108/step/3?unit=1260931
from ipaddress import *
for m in range(33):
    net = ip_network(f'154.201.208.17/{m}', 0)
    if str(net.network_address) == '154.201.192.0':
        print(net.netmask) # 224
# 255.255.192.0
# 255.255.224.0


# https://stepik.org/lesson/1247108/step/4?unit=1260931
from ipaddress import *
for m in range(33):
    net = ip_network(f'122.21.49.91/{m}', 0)
    # if str(net.network_address) == '122.21.48.0':
    if f'{net.network_address}' == '122.21.48.0':
        print(f'{net.netmask:b}'.count('1'))
# 20
# 21
# 22
# 23


# https://stepik.org/lesson/1247108/step/5?unit=1260931
from ipaddress import *
for m in range(33):
    net = ip_network(f'173.103.25.118/{m}', 0)
    if f'{net.network_address}' == '173.103.24.0':
        print(f'{net.netmask:b}'.count('0'))
# 11
# 10
# 9


# https://stepik.org/lesson/1247108/step/6?unit=1260931
from ipaddress import *

cnt = 0
for m in range(33):
    net = ip_network(f'158.116.11.146/{m}', 0)
    if f'{net.network_address}' == '158.116.0.0':
        cnt += 1
        # print(f'{net.netmask}')
print(cnt) # 7


# https://stepik.org/lesson/1247108/step/7?unit=1260931
from ipaddress import *
for m in range(32, 15, -1):
    net = ip_network(f'191.173.145.240/{m}', 0)
    if f'{net.network_address}' == '191.173.144.0':
        print(len(list(net.hosts())) + 2)  # 512
        break

