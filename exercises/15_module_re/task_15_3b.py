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
	result={}
	regex_ip	 =	'^\s+ip\s+address\s+(?P<ip>[\d+.]+)\s+(?P<mask>[\d+.]+$)'
	regex_ip_sec =	'^\s+ip\s+address\s+(?P<ip2>[\d+.]+)\s+(?P<mask2>[\d+.]+)\s+secondary$'
	with open(file) as f:
		for line in f:
			if line.startswith('interface'):
				interface = re.search('^interface\s(?P<intf>\S+)', line).group('intf')
				result[interface] = []
			elif re.match(regex_ip, line):
				ip, mask = re.search(regex_ip, line).group('ip','mask')
				tupl=(ip,mask)
				lis=[tupl]
				result[interface] = lis
			elif re.search(regex_ip_sec, line):
				ip2, mask2 = re.search(regex_ip_sec, line).group('ip2','mask2')
				tupl2=(ip2, mask2)
				lis.append(tupl2)
				result[interface] = lis
	return result

print(parce_cfg('config_r2.txt'))