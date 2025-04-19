""""""
"""
ЕГЭ Информатика
https://stepik.org/course/100056
"""

"""
№ 13 IP-адреса и маски
"""

# # связь между '1' в двоичном числе и четностью  (не совпадает)
# cnt = 0
# for i in range(256):
#     # if bin(i).count('1') % 2 == 0:
#     if bin(i).count('1') % 2 == 0 and bin(i)[-1] == '0':
#         cnt += 1
# # print(cnt)  # 128
# print(cnt)  # 64


# https://stepik.org/lesson/1074876/step/6?unit=1095106
from ipaddress import ip_network
net = ip_network('192.168.32.128/255.255.255.192')
cnt = 0
for ip in net:
    if bin(int(ip)).count('1') % 2 == 0:
        cnt += 1
print(cnt)  # 32


# https://stepik.org/lesson/1074876/step/7?unit=1095106
# Сеть задана IP-адресом 122.159.136.144 и маской сети 255.255.255.248
# Сколько в этой сети IP-адресов, для которых количество единиц в двоичной записи IP-адреса не кратно 4?
from ipaddress import ip_network
cnt = 0
for adr in ip_network('122.159.136.144/255.255.255.248'):
    if bin(int(adr)).count('1') % 4 != 0:
        cnt += 1
print(cnt)  # 5


# https://stepik.org/lesson/1074876/step/7?unit=1095106
# Сеть задана IP-адресом 112.160.0.0 и сетевой маской 255.240.0.0
# Сколько в этой сети IP-адресов, для которых количество единиц в двоичной записи IP-адреса кратно 5?
from ipaddress import ip_network
cnt = 0
for adr in ip_network('112.160.0.0/255.240.0.0'):
    if bin(int(adr)).count('1') % 5 == 0:
        cnt += 1
print(cnt)  # 215766


# https://stepik.org/lesson/1074876/step/11?unit=1095106
# Сеть задана IP-адресом 115.192.0.0 и сетевой маской 255.192.0.0
# Сколько в этой сети IP-адресов, для которых количество единиц в двоичной записи IP-адреса не кратно 3?
from ipaddress import ip_network
cnt = 0
for adr in ip_network('115.192.0.0/255.192.0.0'):
    if bin(int(adr)).count('1') % 3 != 0:
        cnt += 1
print(cnt)  # 2796202


# https://stepik.org/lesson/1074876/step/12?unit=1095106
# Сеть задана IP-адресом 192.168.32.160 и маской сети 255.255.255.240
# Сколько в этой сети IP-адресов, для которых количество нулей в двоичной записи IP-адреса больше 21 ?
from ipaddress import ip_network
cnt = 0
for adr in ip_network('192.168.32.160/255.255.255.240'):
    if f'{adr:b}'.count('0') > 21:
    # if bin(int(adr))[2:].count('0') > 21:
        cnt += 1
print(cnt)  # 11


# https://stepik.org/lesson/1074876/step/13?unit=1095106
# Сеть задана IP-адресом 192.168.248.176 и маской сети 255.255.255.240
# Сколько в этой сети IP-адресов, для которых количество единиц и нулей в двоичной записи IP-адреса одинаково ?
from ipaddress import ip_network
cnt = 0
for adr in ip_network('192.168.248.176/255.255.255.240'):
    if f'{adr:b}'.count('1') == 16:
    # if bin(int(adr))[2:].count('0') == 16:
        cnt += 1
print(cnt)  # 4


# https://stepik.org/lesson/1074876/step/14?unit=1095106
# Сеть задана IP-адресом 202.75.38.152 и маской сети 255.255.255.248
# Сколько в этой сети IP-адресов, у которых в двоичной записи IP-адреса имеется сочетание трех подряд идущих единиц ?
from ipaddress import ip_network
cnt = 0
for adr in ip_network('202.75.38.152/255.255.255.248'):
    if '111' in f'{adr:b}':
    # if bin(int(adr))[2:].count('0') == 16:
        cnt += 1
print(cnt)  # 4

# вариант
cnt = 0
for p1 in '01':
    for p2 in '01':
        for p3 in '01':
            s = '11001010.01001011.00100110.10011' + p1 + p2 + p3
            if '111' in s:
                cnt += 1
print(cnt)


# https://stepik.org/lesson/1074877/step/2?thread=solutions&unit=1095107
# Для узла с IP-адресом 111.81.27.224 адрес сети равен 111.81.27.192.
# Чему равен последний (самый правый) байт маски ?
from ipaddress import *

for i in range(1, 33):
    try:
        net = ip_network(f'111.81.27.192/{i}')
        if ip_address('111.81.27.224') in net:
            # print(str(net.netmask).split('.')[3])
            print(str(net.netmask))  # 192
    except:
        pass



# https://stepik.org/lesson/1074877/step/4?thread=solutions&unit=1095107
# Для узла с IP-адресом 111.81.208.27 адрес сети равен 111.81.192.0
# Чему равно наименьшее возможное значение третьего слева байта маски ?
from ipaddress import *

for i in range(1, 33):
    try:
        net = ip_network(f'111.81.192.0/{i}')
        if ip_address('111.81.208.27') in net:
            print(str(net.netmask))  # 192
    except:
        pass
# 255.255.192.0
# 255.255.224.0


#  https://stepik.org/lesson/1074878/step/2?thread=solutions&unit=1095109
# Сеть задана IP-адресом 192.168.32.160 и маской сети 255.255.255.224
# Сколько в этой сети IP-адресов, у которых в двоичной записи IP-адреса количество нулей
# хотя бы в два раза превосходит количество единиц ?
from ipaddress import ip_network
cnt = 0
for i in ip_network('192.168.32.160/27'):
    adr = f'{i:b}'
    cnt += adr.count('0') >= adr.count('1') * 2
print(cnt)  # 16


#  https://stepik.org/lesson/1074878/step/3?unit=1095109
# Сеть задана IP-адресом 192.168.248.176 и маской сети 255.255.255.240
# Сколько в этой сети IP-адресов, для которых количество единиц в двоичной записи IP-адреса больше,
# чем количество нулей?
from ipaddress import ip_network
cnt = 0
for i in ip_network('192.168.248.176/28'):
    adr = f'{i:b}'
    cnt += adr.count('1') > adr.count('0')
print(cnt)  # 1


#  https://stepik.org/lesson/1074878/step/4?unit=1095109
# Сеть задана IP-адресом 211.48.136.64 и маской сети 255.255.255.224
# Сколько в этой сети IP-адресов, которые в двоичной записи IP-адреса оканчиваются двумя единицами?
from ipaddress import ip_network
cnt = 0
for i in ip_network('211.48.136.64/27'):
    # adr = f'{i:b}'
    cnt += f'{i:b}'[-2:] == '11'
print(cnt)  # 8


#  https://stepik.org/lesson/1074878/step/5?unit=1095109
# Сеть задана IP-адресом 112.208.0.0 и сетевой маской 255.255.128.0
# Сколько в этой сети ІР-адресов, для которых количество единиц в двоичной записи IP-адреса кратно 11?
from ipaddress import ip_network
cnt = 0
for i in ip_network('112.208.0.0/17'):
    # cnt += not f'{i:b}'.count('1') % 11
    cnt += f'{i:b}'.count('1') % 11 == 0
print(cnt)  # 3003


#  https://stepik.org/lesson/1074878/step/6?unit=1095109
# Сеть задана IP-адресом 112.160.0.0 и сетевой маской 255.240.0.0
# Сколько в этой сети IP-адресов, для которых количество единиц в двоичной записи IP-адреса не кратно 3 ?
from ipaddress import ip_network
cnt = 0
for i in ip_network('112.160.0.0/12'):
    cnt += not f'{i:b}'.count('1') % 3 == 0
print(cnt)  # 699050







