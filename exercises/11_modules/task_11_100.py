#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
А перебирать значения из topology и не нужно.
Чтобы избавиться от дублей, можно в цикле перебирать ключи
и значения текущего словаря parsed и добавлять `(key, value)`
 в итоговый словарь topology только если в нем нет пары
 '(value, key)`, но достаточно даже проверки,
 что `value` нет среди ключей topology
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
			print('pk',pk)
		# 	print('pv',pv)
			if not pk in topology.values():
				print('!')
				topology[pk]=pv
				# else:
				# 	topology[pk]=pv
		print('-------')
			

pprint(topology)

