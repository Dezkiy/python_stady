#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

	{('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
	 ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.

Проверить работу функции на содержимом файла sw1_sh_cdp_neighbors.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

from pprint import pprint

file=open('sh_cdp_n_sw1.txt')
# file=open('input2.txt')
def parse_cdp_neighbors(inf):
	'''
	inf - file, для которых необходимо сгенерировать конфигурацию, вида:
		{('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
		('R4', 'Fa0/2'): ('R6', 'Fa0/0')}
	'''
	result={}

	for line in inf:
		if '>' in line:
			device=line.split('>')[0]
		if not line.startswith('\n') and not line.startswith('Device ID') and not '>' in line and not ',' in line:
			list1=[device,(line.split()[1] + line.split()[2])]
			list2=[(line.split()[0]),(line.split()[-2] + line.split()[-1])] 
			tuple1=tuple(list1)
			tuple2=tuple(list2)
			result[tuple1] = tuple2
	return result   

# pprint (parse_cdp_neighbors(file))
file.closed