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


# https://stepik.org/lesson/1224061/step/4?unit=1237558
from ipaddress import *
cnt = 0
net = ip_network('151.192.0.0/255.224.0.0', 0)
for i in net:
    b = f'{i:b}'
    cnt += b.count('0') == b.count('1')
print(cnt)  # 293930


# https://stepik.org/lesson/1224061/step/5?unit=1237558
from ipaddress import *
cnt = 0
net = ip_network('123.222.111.192/255.255.255.248', 0)
for i in net:
    b = f'{i:b}'
    cnt += b[-8:].count('1') % 3 != 0
print(cnt)  # 5


# https://stepik.org/lesson/1224061/step/6?unit=1237558
from ipaddress import *
def f(n):
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            return 0
    return 1

cnt = 0
net = ip_network('172.118.1.255/255.255.252.0', 0)
for i in net.hosts():
    b = f'{i:b}'.count('1')
    cnt += f(b)
print(cnt)  # 300


# https://stepik.org/lesson/1224061/step/7?unit=1237558
from ipaddress import *
cnt = 0
net = ip_network('49.26.38.163/255.255.255.224', 0)
for i in net.hosts():
    cnt += f'{i:b}'[-1] == '1'
print(cnt)  # 15


# https://stepik.org/lesson/1224061/step/8?unit=1237558
from ipaddress import *
cnt = 0
net = ip_network('235.86.56.0/255.255.248.0', 0)
for i in net:
    cnt += f'{i:b}'[-2:] == '11'
print(cnt)  # 512




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


""" 26.5 Закрепление (ч. 2) """
# Задачка для моего курса
# https://stepik.org/lesson/1229246/step/3?unit=1242787
from ipaddress import *
for n in range(32, 0, -1):
    net1 = ip_network(f'140.37.235.224/{n}', 0)
    net2 = ip_network(f'140.37.235.192/{n}', 0)
    if net1 == net2:
        if ip_address('140.37.235.224') in net1.hosts() and ip_address('140.37.235.192') in net2.hosts():
            print(net1.netmask)  # 255.255.255.128
            # print(str(net1.netmask).split('.')[-1])  # 128
            break


""" 27.5 Закрепление (ч. 2) """
# https://stepik.org/lesson/1229629/step/3?unit=1243181
# var 1
print(2**11 - 2)  # 2046

# var 2
from ipaddress import *
net = ip_network('1.2.3.4/255.255.248.0', 0)
print(len(list(net.hosts())))  # 2046


""" 28.5 Закрепление (ч. 2) """
# Задачка для моего курса
# https://stepik.org/lesson/1229674/step/3?unit=1243226
from ipaddress import *
for n in range(25, 33):
    net1 = ip_network(f'98.162.78.139/{n}', 0)
    net2 = ip_network(f'98.162.78.154/{n}', 0)
    if net1 != net2:
        print(n)  # 28
        break

