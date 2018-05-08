#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Задание 17.2a

С помощью функции parse_sh_cdp_neighbors из задания 17.2,
обработать вывод команды sh cdp neighbor из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Объединить все словари, которые возвращает функция parse_sh_cdp_neighbors,
в один словарь topology и записать его содержимое в файл topology.yaml.

Структура словаря topology должна быть такой:
{'R4': {'Fa0/1': {'R5': 'Fa0/1'},
        'Fa0/2': {'R6': 'Fa0/0'}},
 'R5': {'Fa0/1': {'R4': 'Fa0/1'}},
 'R6': {'Fa0/0': {'R4': 'Fa0/2'}}}

При этом интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.

Не копировать код функции parse_sh_cdp_neighbors
'''

from task_17_2 import parse_sh_cdp_neighbors 
import yaml

infiles = ['sh_cdp_n_sw1.txt',
			'sh_cdp_n_r1.txt',
			'sh_cdp_n_r2.txt',
			'sh_cdp_n_r3.txt',
			'sh_cdp_n_r4.txt',
			'sh_cdp_n_r5.txt',
			'sh_cdp_n_r6.txt']

topology={}

for file in infiles:
	with open(file) as show_command:
		parsed = parse_sh_cdp_neighbors(show_command.read())
		for pk,pv in parsed.items():
			if not pk in topology.values():
				topology[pk]=pv

print(topology)

def dict_to_yaml (file, indict):
	'''
	ожидает словарь (indict)
	записыват в файл в формате yaml
	'''
	with open(file, 'w') as f:
		yaml.dump(indict, f, default_flow_style=False)

dict_to_yaml ('topology.yaml', topology)
