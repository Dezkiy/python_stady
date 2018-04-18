#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Задание 15.4

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'up', 'up')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br_2.txt.

R1#show ip interface brief
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            15.0.15.1       YES manual up                    up
FastEthernet0/1            10.0.12.1       YES manual up                    up
FastEthernet0/2            10.0.13.1       YES manual up                    up
FastEthernet0/3            unassigned      YES unset  administratively down down
Loopback0                  10.1.1.1        YES manual up                    up
Loopback100                100.0.0.1       YES manual up                    up

'''
import re
from pprint import pprint

def parse_sh_ip_int_br(file):
	result = []
	regex = ('(?P<intf>^\S+)\s+(?P<ip>(unassigned|[\d+.]+))\s+(YES|NO)\s+(manual|unset)'
			'\s+(?P<stat>(up|down|administratively down))\s+(?P<prot>(up|down))$')
	with open(file) as f:
		for line in f:
			match = re.search(regex, line)
			if match:
				result.append(match.group('intf','ip','stat','prot'))
	return result

# pprint(parse_sh_ip_int_br('sh_ip_int_br_2.txt'))
