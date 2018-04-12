#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Задание 15.3a

Переделать функцию parse_cfg из задания 15.3 таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

Например (взяты произвольные адреса):
{'FastEthernet0/1':('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2':('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''
import re

def parce_cfg(file):
	regex = ('^interface\s+(?P<intf>(Ethernet|Tunnel|Loopback)\d+/*\d*.*)'
			'|^\s+ip\s+address\s+(?P<ip>[\d+.]+)\s+(?P<mask>[\d+.]+)') 
	result={}
	with open(file) as f:
		for line in f:
			match = re.search(regex, line)
			if match:
				if match.lastgroup == 'intf':
					intf = match.group(match.lastgroup)
					result[intf] = ()
				elif intf:
					result[intf] = (match.group('ip'),match.group('mask'))
	return result

print(parce_cfg('config_r1.txt'))