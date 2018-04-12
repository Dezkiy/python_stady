#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Задание 15.3b

Проверить работу функции parse_cfg из задания 15.3a на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция parse_cfg, интерфейсу Ethernet0/1
соответствует только один из них (второй).

Переделайте функцию parse_cfg из задания 15.3a таким образом,
чтобы она возвращала список кортежей для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет несколько кортежей.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''

import re

def parce_cfg(file):
	regex = ('^interface\s+(?P<intf>(Ethernet|Tunnel|Loopback)\d+/*\d*.*)'
			'|^\s+ip\s+address\s+(?P<ip_1>[\d+.]+)\s+(?P<mask_1>[\d+.]+)'
			'|^\s+ip\s+address\s+(?P<ip_2>[\d+.]+)\s+(?P<mask_2>[\d+.]+\s+secondary$)')
	result={}
	with open(file) as f:
		for line in f:
			match = re.search(regex, line)
			if match:
				if match.lastgroup == 'intf':
					intf = match.group(match.lastgroup)
					result[intf] = []
				elif intf:
					tupl=(match.group('ip_1'),match.group('mask_1'))
					if match.lastgroup == 'ip_2':
						print("!")
						tupl2=(match.group('ip_2'))
						result[intf] = [tupl2]
					else:
						# print("OK")
						result[intf] = [tupl]
	return result

print(parce_cfg('config_r2.txt'))