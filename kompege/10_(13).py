""" https://kompege.ru/task """
"""
10157 10158  10160 10161 10163 10164 10165 10166 10167 10169 10171 10172 
10570 10578 10715 10773 10776 10781 10785 10786 10788 10789 
11662 11779 11780 11787 11794 11835
12088 12245 12451 12922 12947 14648 14649 17632 18487 19748
22466 22467 23372 23559 23857 24971 25141 27768 29966 31221
"""


# 10157 (Уровень: Базовый)
from ipaddress import *
for m in range(32, 0, -1):
    net = ip_network(f'241.185.253.57/{m}', False)
    if str(net.network_address) == '241.185.252.0':
        print(32 - m)  # 9
        break


# 10158 (Уровень: Базовый)
from ipaddress import *
for m in range(33):
    net = ip_network(f'204.108.112.142/{m}', False)
    if str(net.network_address) == '204.108.64.0':
        print(32 - m)  # 14
        break


""" Взято на мой курс """
# 10160 (Уровень: Базовый)
from ipaddress import *
c = 0
for i in range(1, 33):
    net = ip_network(f'76.155.48.2/{i}', False)
    c += str(net.network_address) == '76.155.48.0'
print(c)  # 11
# variant
from ipaddress import *
cnt = 0
for m in range(1, 33):
    net = ip_network(f'76.155.48.2/{m}', False)
    cnt += str(net) == f'76.155.48.0/{m}'
print(cnt)  # 11


# 10161 (Уровень: Средний)
from ipaddress import *
res = 0
for i in range(1, 33):
    net1 = ip_network(f'211.115.61.154/{i}', False)
    net2 = ip_network(f'211.115.59.137/{i}', False)
    if net1 == net2:
        m = str(net1.netmask).split('.')[2]
        res = max(res, int(m))
print(res)  # 248

# variant
from ipaddress import *
for i in range(32, 0, -1):
    net1 = ip_network(f'211.115.61.154/{i}', False)
    net2 = ip_network(f'211.115.59.137/{i}', False)
    if net1 == net2:
        m = str(net1.netmask).split('.')[2]
        print(m)  # 248
        break


# 10163 (Уровень: Средний)
from ipaddress import *
net = list(ip_network(f'192.168.156.235/255.255.255.240', False))
print(net.index(ip_address('192.168.156.235')))  # 11  (индекс 0 ушел на адрес сети)


""" Взято на мой курс """
# 10164 (Уровень: Средний)
from ipaddress import *
n = 0
net = ip_network('156.132.15.138/255.255.252.0', False)
for i in net.hosts():
    n += 1
    # if i == ip_address('156.132.15.138'):
    if str(i) == '156.132.15.138':
        print(n)  # 906
        break

# variant
from ipaddress import *
n = 0
net = ip_network('156.132.15.138/255.255.252.0', False)
n = [*net.hosts()]
print(n.index(ip_address('156.132.15.138')) + 1)  # 906


# 10165 (Уровень: Базовый)
from ipaddress import *
net = ip_network(f'0.0.0.0/255.255.255.128', False)
print(net.num_addresses - 2)  # 126  (индекс 0 ушел на адрес сети)
# 128 -> 1000 0000 -> 2**7 = 128 - 2 = 126


# 10166 (Уровень: Базовый)
from ipaddress import *
n = 0
net = ip_network('0.0.0.0/255.255.254.0', False)
n = [*net.hosts()]
print(len(n))  # 510

# variant
# .254.0 >>  .11111110.00000000
print(2**9 - 2)  # 510


""" Взято на мой курс """
# 10167 (Уровень: Базовый)
from ipaddress import *
res = 0
for m in range(1, 33):
    net = ip_network(f'108.133.75.91/{m}', False)
    if str(net.network_address) == '108.133.75.64':
        res = max(res, net.num_addresses)
print(res)  # 64

# Каждый нуль в маске - это два варианта адреса в сети. В данной задаче маска содержит шесть "0"  -> 2**6 = 64
from ipaddress import *
for m in range(1, 33):
    net = ip_network(f'108.133.75.91/{m}', False)
    if str(net.network_address) == '108.133.75.64':
        print(2**(32 - m))  # 64
        break


""" Взято на мой курс """
# 10169 (Уровень: Средний)
from ipaddress import *
def ip_ok(ip, net): # проверка узла на корректность
    return ip not in (str(net[0]), str(net[-1]))

for m in range(1, 33):
    net1 = ip_network(f'157.127.182.76/{m}', False)
    net2 = ip_network(f'157.127.190.80/{m}', False)
    if net1 != net2 and ip_ok('157.127.182.76', net1) and ip_ok('157.127.190.80', net2):
        print(m)  # 21
        break

# возможна ошибка, если узел окажется сетью или шириком !!!
for m in range(33):
    net1 =  ip_network(f'157.127.182.76/{m}', False)
    net2 =  ip_network(f'157.127.190.80/{m}', False)
    if net1 != net2:
        print(m)  # 21
        break



# 10171 (Уровень: Средний)
c = 0
for m in range(1, 33):
    net = ip_network(f'115.53.128.88/{m}', False)
    if net.network_address == ip_address('115.53.128.0'):
        if net.num_addresses - 2 >= 1000:
            c += 1
print(c)  # 6


# 10172 (Уровень: Средний)
for m in range(32, 0, -1):
    net = ip_network(f'175.122.80.13/{m}', False)
    if net.network_address == ip_address('175.122.80.0'):
        if net.num_addresses - 2 >= 60:
            print(33 - m)  # 7
            break

# variant
from ipaddress import *
cnt = 0
for m in range(1, 33):
    net = ip_network(f'175.122.80.13/{m}', False)
    if str(net.network_address) == '175.122.80.0':
        if '175.122.80.13' not in str(net[-1]):  # доп. проверка на broadcast (сам узел точно не сетевой адрес)
            cnt += 2**(32 - m) - 2 >= 60
            # cnt += net.num_addresses - 2 >= 60
print(cnt)  # 7


""" Взято на мой курс """
# 10570 (Уровень: Базовый)
from ipaddress import *
for n in range(32, 0, -1):
    net = ip_network(f'154.201.208.17/{n}', False)
    if str(net.network_address) == '154.201.192.0':
        msk = str(net.netmask).split('.')
        print(msk[2])  # 224
        break


""" Взято на мой курс """
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


""" Взято на мой курс """
# 10773 (Уровень: Базовый)
from ipaddress import *
c = 0
for m in range(1, 33):
    net = ip_network(f'133.57.64.130/{m}', False)
    c += str(net) == f'133.57.64.0/{m}'
print(c)  # 7



""" Взято на мой курс """
# 10781 (Уровень: Средний)
from ipaddress import *
for m in range(32, 0, -1):
    net1 = ip_network(f'112.117.107.70/{m}', False)
    net2 = ip_network(f'112.117.121.80/{m}', False)
    if net1 == net2:
        print(net1.num_addresses)  # 8192
        print(2**(32 - m))  # 8192
        break


# 10785 (Уровень: Базовый)
from ipaddress import *
for m in range(1, 33):
    net = ip_network(f'192.75.64.98/{m}', False)
    if str(net.network_address) == '192.75.64.0':
        print(m) # 18
        break


# 10786 (Уровень: Средний)
from ipaddress import *
for m in range(1, 33):
    net1 = ip_network(f'151.172.115.121/{m}', False)
    net2 = ip_network(f'151.172.115.156/{m}', False)
    if net1 != net2:
        print(m)  # 25
        break


# 10788 (Уровень: Базовый)
from ipaddress import *
c = 0
for m in range(1, 33):
    net1 = ip_network(f'201.44.240.33/{m}', False)
    net2 = ip_network(f'201.44.240.107/{m}', False)
    if net1 == net2:
        c += f'{net1.network_address:b}'.count('1') >= 5
print(c)  # 15


# 10789 (Уровень: Базовый)
from ipaddress import *
c = 0
for m in range(1, 33):
    net = ip_network(f'203.75.227.102/{m}', False)
    if str(net.network_address) == '203.75.224.0':
        c += 1
print(c)  # 4


# 11662 (Уровень: Базовый)
from ipaddress import *
c = 0
net = ip_network('123.222.111.192/255.255.255.248', False)
for i in net:
    c += f'{i:b}'[24:].count('1') % 3 != 0
print(c)  # 5



""" Взято на мой курс """
# 11779 (Уровень: Базовый)
from ipaddress import *
c = 0
net = ip_network('151.192.0.0/255.224.0.0', False)
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
net = ip_network('101.157.240.0/255.255.252.0', False)
for i in net:
    c += f'{i:b}'[:16].count('1') > f'{i:b}'[16:].count('1')
print(c)  # 386


# 11794 (Уровень: Базовый)
from ipaddress import *
for n in range(255, -1, -1):
    net = ip_network(f'223.167.{n}.167/255.255.255.192', False)
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



""" Взято на мой курс """
# 12245 ЕГКР 16.12.13_(23) (Уровень: Базовый)
from ipaddress import *
net = ip_network('192.168.32.48/255.255.255.240', False)
c = 0
for i in net:
    c += f'{i:b}'.count('1') % 2
print(c)  # 8


""" Взято на мой курс """
# 12451 (Уровень: Средний) 🌶️🌶️🌶️
# Ловушка: адрес IP может оказаться как network/broadcast в формируемой сети из этого адреса IP ✅
from ipaddress import *
c = 0
for x in range(256):
    IP = f'246.81.65.{x}'
    net = ip_network(f'{IP}/255.255.255.224', False)
    if ip_address(IP) not in (net[0], net[-1]):  # Проверяем, что IP не network/broadcast ✅
        c += all(f'{i:b}'[16:24].count('0') > f'{i:b}'[24:].count('0') for i in net.hosts())
print(c)  # 120


# 12922 PRO100 ЕГЭ 26.01.24(Уровень: Базовый)
from ipaddress import *
cnt = 0
net = ip_network('136.36.240.16/255.255.255.248', False)
for i in net:
    cnt += '101' not in f'{i:b}'
print(cnt)  # 4


""" Взято на мой курс """
# 12947 (Уровень: Базовый)
from ipaddress import *
cnt = 0
net = ip_network('203.111.195.0/255.255.240.0', False)
for i in net:
    b = f'{i:b}'
    cnt += not b.count('0') % 3 and '111' in b and '000' in b
print(cnt)  # 1043


""" Взято на мой курс """
# 10776 (Уровень: Базовый)
from ipaddress import *
for n in range(32, 0, -1):
    net = ip_network(f'111.91.200.28/{n}', False)
    if str(net) == f'111.91.192.0/{n}':
    # if str(net.network_address) == '111.91.192.0':
    # if str(net).split('/')[0] == '111.91.192.0':
        print(32 - n)  # 12
        break


""" Взято на мой курс """
# 14648 Открытый курс "Слово пацана"(Уровень: Базовый)
from ipaddress import *
cnt = 0
for m in range(1, 33):
    net = ip_network(f'125.28.160.73/{m}', False)
    if net.network_address == ip_address('125.28.160.0'):
        cnt += net.num_addresses - 2 >= 500
print(cnt)  # 5


""" Взято на мой курс """
# 14649 Открытый курс "Слово пацана" (Уровень: Средний)
from ipaddress import *
for a in range(255, -1, -1):
    net = ip_network(f'116.242.{a}.26/255.255.255.224', False)
    if all(f'{i:b}'[:16].count('1') >= f'{i:b}'[16:].count('1') for i in net):
        print(a)  # 240
        break


# 17632 Основная волна 19.06.24 (Уровень: Базовый)
from ipaddress import *
c = 0
net = ip_network('112.160.0.0/255.240.0.0', False)
for i in net:
    c += not f'{i:b}'.count('1') % 5
print(c)  # 215766


# 18487 (Уровень: Средний)
from ipaddress import *
for x in range(256):
    net = ip_network(f'192.214.{x}.184/255.255.255.224', False)
    if all(f'{i:b}'.count('1') > 15 for i in net) :
        print(x)  # 127
        break


""" Взято на мой курс """
# 19748 (Уровень: Средний)
from ipaddress import *
for m in range(32, 12, -1):
    c = 0
    net1 = ip_network(f'157.220.185.237/{m}', False)
    net2 = ip_network(f'157.220.184.230/{m}', False)
    if net1 == net2:
        c += sum(f'{i:b}'.count('1') == 15 for i in net1)
    if c:
        print(c)  # 9
        break


""" Взято на мой курс """
# 22466 (Уровень: Базовый)
from ipaddress import *
net = ip_network('98.71.254.171/255.248.0.0', False)
for i in net.hosts():
    res = f'{i:b}'.count('1')
    if res and not res % 7:
        print(str(i).replace('.', ''))  # 986407
        break


# 22467 (Уровень: Средний) 🌶️🌶️
from ipaddress import *
def ip_ok(ip: str, net):
    return ip not in (str(net[0]), str(net[-1]))

cnt = 0
for m in range(1, 33):
    net = ip_network(f'192.214.116.184/{m}', False)
    res = f'{net.network_address:b}'.count('1')
    if res and not res % 5 and ip_ok('192.214.116.184', net):
        cnt += 1
print(cnt)  # 4


# 23372 Резервный день 19.06.25 (Уровень: Базовый)
from ipaddress import *
net = ip_network('73.148.145.65/255.224.0.0', False)
print(str(net[-2]).replace('.', ''))  # 73159255254


# 23559 Пересдача 03.07.25 (Уровень: Базовый)
from ipaddress import *
net = ip_network('102.162.200.51/255.255.255.0', False)
r = str(net[-2])
print(sum(map(int, r.split('.'))))  # 718



""" Взято на мой курс """
# 23857 (Уровень: Базовый)
from ipaddress import *
cnt = 0
net = ip_network('192.168.12.207/255.192.0.0', False)
for i in [*net][::-1]:
    if f'{i:b}'.count('1') == 16:
        print(str(i).replace('.', ''))  # 1921912540
        break


""" Взято на мой курс """
# 24971 (Уровень: Средний)
from ipaddress import *
net = ip_network('111.222.0.124/255.255.224.0', False)
for i in [*net][::-1]:
    one = f'{i:b}'.count('1')
    zero = 32 - one
    if one * zero % 2:
        print(sum(map(int, str(i).split('.'))))  # 619
        break


""" Взято на мой курс """
# 25141 (Уровень: Средний)
from ipaddress import *
net = ip_network('46.29.170.214/255.255.128.0', False)
for i in list(net.hosts())[::-1]:
    n = sorted(map(int, str(i).split('.')))
    if n[-1] == sum(n[:-1]):
        print(str(i).replace('.', ''))  # 4629255180
        break


""" Взято на мой курс """
# 27768 Апробация 04.03.26(Уровень: Базовый)
from ipaddress import *
cnt = 0
net = ip_network('172.16.160.0/255.255.240.0', False)
for i in net:
    cnt += not f'{i:b}'.count('1') % 2
print(cnt)  # 2048


# 29966 Апробация 14.05.26(Уровень: Базовый)
from ipaddress import *
net = ip_network('146.180.173.153/255.192.0.0', False)
res = str(net[-2]).replace('.', '')
print(res)  # 146191255254


""" Взято на мой курс """
# 31221 Резерв 22.06.26(Уровень: Базовый)
from ipaddress import *
net = ip_network('64.237.228.143/255.255.248.0', False)
res = str(net.network_address).split('.')
print(sum(map(int, res)))  # 525




""" Сложные задания из других источников """
# https://stepik.org/lesson/1073822/step/13?unit=1085000 🌶️️🌶️🌶️
from ipaddress import *
res = 0
for m in range(0, 25): # первый октет уже полный а последнмй должен быть пустым
    net = ip_network(f'85.169.154.54/{m}', False)
    if sum(map(int, str(net.network_address).split('.'))) == 408:
        xy = sum(map(int, str(net.netmask).split('.')[1:3]))
        res = max(res, xy)
print(res)  # 510

res = 0
for x in range(256):
    for y in range( 256):
        try:
            net = str(ip_network(f'85.169.154.54/255.{x}.{y}.0', False).network_address)
            if sum(map(int, net.split('.'))) == 408:
                res = max(res, x+y)
        except:
            ...
print(res)  # 510


# https://stepik.org/lesson/1073822/step/15?unit=1085000 🌶️️🌶️
from ipaddress import *
res = set()
for m in range(33):
    net = ip_network(f'125.28.160.73/{m}', False)
    if str(net.network_address) == '125.28.160.0':
        if net.num_addresses >= 500:
            res.add(str(net.netmask).split('.')[2])
            # print(str(net.netmask).split('.')[2])
print(len(res))  # 5
