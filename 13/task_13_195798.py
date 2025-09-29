""""""
"""
Task 13
ЕГЭ информатика 2025. Полный курс
https://stepik.org/course/195798
"""

""" 18.2 Практика (ур. базовый) """
# https://stepik.org/lesson/1224001/step/1?unit=1237498
from ipaddress import *
cnt = 0
for n in range(17, 25):
    net = ip_network(f'203.75.227.102/{n}', 0)
    cnt += str(net).split('/')[0] == '203.75.224.0'
print(cnt)  # 4


# https://stepik.org/lesson/1224001/step/2?unit=1237498
from ipaddress import *
for n in range(32, 0, -1):
    net = ip_network(f'111.24.160.159/{n}', 0)
    if str(net.network_address) == '111.24.160.128':
    # if str(net).split('/')[0] == '111.24.160.128':
        print(n)  # 4
        break


# https://stepik.org/lesson/1224001/step/3?unit=1237498
from ipaddress import *
for n in range(1, 33):
    net = ip_network(f'192.75.64.98/{n}', 0)
    if str(net.network_address) == '192.75.64.0':
    # if str(net).split('/')[0] == '192.75.64.0':
        print(n)  # 18
        break


# https://stepik.org/lesson/1224001/step/4?unit=1237498
from ipaddress import *

net = ip_network(f'214.120.249.18/255.255.240.0', 0)
print(net)  # 214.120.240.0   ECFA


# https://stepik.org/lesson/1224001/step/6?unit=1237498
from ipaddress import *

for n in range(32, 0, -1):
    net = ip_network(f'111.91.200.28/{n}', 0)
    # if str(net).split('/')[0] == '111.91.192.0':
    if str(net.network_address) == '111.91.192.0':
        print(32 - n)  # 12
        break


# https://stepik.org/lesson/1224001/step/7?unit=1237498
from ipaddress import *
cnt = -1  # исключаем адрес сети
net = ip_network(f'156.128.0.227/255.255.255.248', 0)
for i in net:
    cnt += 1
    if str(i) == '156.128.0.227':
        print(cnt)  # 3
        break


# https://stepik.org/lesson/1224001/step/9?unit=1237498
from ipaddress import *
cnt = 0
for n in range(33):
    net = ip_network(f'133.57.64.130/{n}', 0)
    cnt += str(net.network_address) == '133.57.64.0'
print(cnt)  # 7


# https://stepik.org/lesson/1224001/step/10?unit=1237498
from ipaddress import *
cnt = 0
net = ip_network('10.48.96.0/255.255.240.0', 0)
for i in net:
    # cnt += f'{int(i):b}'.count('1') > 16
    cnt += f'{i:b}'.count('1') > 16  # так тоже работает !!!
print(cnt)  # 13



""" 18.3 Практика (ур. усложненный) """
# https://stepik.org/lesson/1224061/step/1?unit=1237558
from ipaddress import *
cnt = 0
net = ip_network('136.36.240.16/255.255.255.248', 0)
for i in net:
    cnt += not f'{i:b}'.count('101')
print(cnt)  # 4


# https://stepik.org/lesson/1224061/step/2?unit=1237558
from ipaddress import *
cnt = 0
net = ip_network('112.154.133.208/255.255.252.0', 0)
for i in net.hosts():
    l = f'{i:b}'[:16].count('1')
    r = f'{i:b}'[16:].count('0')
    cnt += (l <= r and r % 2)  # только среди тех вариантов, где нечётное кол-во нулей в  r
print(cnt)  # 502


# https://stepik.org/lesson/1224061/step/3?unit=1237558
from ipaddress import *
res = 32
net = ip_network('129.128.0.0/255.128.0.0', 0)
for i in net:
    res = min(res, f'{i:b}'.count('0'))
print(res)  # 6




""" 18.4 Закрепление """
# https://stepik.org/lesson/1224003/step/13?unit=1237500
from ipaddress import *
for n in range(32, 24, -1):
    net = ip_network(f'98.162.71.94/{n}', 0)
    if str(net.network_address) == '98.162.71.64':
        print(net.netmask)  # 255.255.255.224
        break

""" 21.4 Закрепление"""
# https://stepik.org/lesson/1227125/step/13?unit=1240643
from ipaddress import *
for n in range(32,0,-1):
    net = ip_network(f'111.81.200.27/{n}', 0)
    if str(net.network_address) == '111.81.192.0':
        print(net.netmask)  # 240
        break


""" 23.5 Закрепление (ч. 2) """
# https://stepik.org/lesson/1227732/step/3?unit=1241247
from ipaddress import *
c = 0
net = ip_network(f'112.154.133.208/255.255.248.0', 0)
for n in net.hosts():
    c += 1
    if str(n) == '112.154.133.208':
        print(c)  # 1488
        break

# variant 1
from ipaddress import *
net = ip_network(f'112.154.133.208/255.255.248.0', 0)
print(list(net.hosts()).index(ip_address('112.154.133.208')) + 1)  # 1488

# variant 2
from ipaddress import *
net = ip_network(f'112.154.133.208/255.255.248.0', 0)
print(list(net).index(ip_address('112.154.133.208')))  # 1488




