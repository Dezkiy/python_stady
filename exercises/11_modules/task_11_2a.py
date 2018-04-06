#!/bin/python
# -*- coding: utf-8 -*-
'''
Задание 11.2a

С помощью функции parse_cdp_neighbors из задания 11.1
и функции draw_topology из файла draw_network_graph.py
сгенерировать топологию, которая соответствует выводу
команды sh cdp neighbor из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt

Не копировать код функций parse_cdp_neighbors и draw_topology.

В итоге, должен быть сгенерировано изображение топологии.
Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg
'''
from pprint import pprint
from task_11_1 import parse_cdp_neighbors
from draw_network_graph import draw_topology

infiles = [ 'sh_cdp_n_sw1.txt',
			'sh_cdp_n_r1.txt',
			'sh_cdp_n_r2.txt',
			'sh_cdp_n_r3.txt']

topology = {}

for file in infiles:
	with open(file) as show_command:
		parsed = parse_cdp_neighbors(show_command)
		for pk,pv in parsed.items():
			if not pk in topology.values():
				topology[pk]=pv

pprint(topology)

draw_topology(topology)