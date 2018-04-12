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
	result={}
	regex_ip='^\s+ip\s+address\s+(?P<ip>[\d+.]+)\s+(?P<mask>[\d+.]+$)'
	regex_ip_sec='^\s+ip\s+address\s+(?P<ip2>[\d+.]+)\s+(?P<mask2>[\d+.]+)\s+secondary$'
	with open(file) as f:
		for line in f:
			if line.startswith('interface'):
				interface = re.search('^interface\s(?P<intf>\S+)', line).group('intf')
				result[interface] = ()
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