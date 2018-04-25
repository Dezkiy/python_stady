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

def parse_sh_cdp_neighbors(output):
	result={}
	res={}

	output_list=output.split('\n')

	finda=re.findall('(\w+)\s+(\w+\s?\d+/\d+).+(?:\w ){3}\s+\w+\s+(\w+\s?\d+/\d+)', output)

	for l in finda:
		res[l[1]]={l[0]:l[2]}

	for line in output_list:
		match=re.search('(?P<device>\w+)[>#].+', line)
		if match:
			result[match.group('device')]=res
			return result

with open('sh_cdp_n_sw1.txt') as f:
	print(parse_sh_cdp_neighbors(f.read()))