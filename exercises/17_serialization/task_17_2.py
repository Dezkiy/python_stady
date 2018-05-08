#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Задание 17.2

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa0/1': {'R5': 'Fa0/1'},
		'Fa0/2': {'R6': 'Fa0/0'}}}

При этом интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
'''
import re

# def parse_sh_cdp_neighbors(output):						# вариант с двумя циклами отрабатывает не так как нужно (оставляет пустой словарь)
# 	result={}
# 	res={}

# 	output_list=output.split('\n')

# 	finda=re.findall('(\w+)\s+(\w+\s?\d+/\d+).+(?:\w ){3}\s+\w+\s+(\w+\s?\d+/\d+)', output)
# 					#  \w+ +\S+ +\S+ +\d+ +[RTBSHIr ]+\S+ +\S+ +\S+
# 	for l in finda:
# 		res[l[1]]={l[0]:l[2]}

# 	for line in output_list:
# 		match=re.search('(?P<device>\w+)[>#].+', line)
# 		if match:
# 			result[match.group('device')]=res
# 			return result

# with open('sh_cdp_n_sw1.txt') as f:
# 	print(parse_sh_cdp_neighbors(f.read()))


def parse_sh_cdp_neighbors(command_output):								#вариант от natasha(переделанный)			
	regex = re.compile('(?P<rem_dev>\w+)  +(?P<loc_intf>\S+ \S+)'
					'  +\d+  +[RTBSHIr ]+  +\S+ +(?P<rem_intf>\S+ \S+)')
	connect_dict = {}
	dev = re.search('(\S+)[>#].*', command_output).group(1)
	connect_dict[dev] = {}
	for match in regex.finditer(command_output):
		rem_dev, loc_intf, rem_intf = match.group('rem_dev', 'loc_intf', 'rem_intf')
		connect_dict[dev][loc_intf] = {rem_dev: rem_intf}
	return connect_dict

# with open('sh_cdp_n_sw1.txt') as f:
# 	print(parse_sh_cdp_neighbors(f.read()))
