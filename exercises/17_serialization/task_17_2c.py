#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
С помощью функции draw_topology из файла draw_network_graph.py
сгенерировать топологию, которая соответствует описанию в файле topology.yaml

Обратите внимание на то, какой формат данных ожидает функция draw_topology.
Описание топологии из файла topology.yaml нужно преобразовать соответствующим образом,
чтобы использовать функцию draw_topology.

Для решения задания можно создать любые вспомогательные функции.

Не копировать код функции draw_topology.

В итоге, должно быть сгенерировано изображение топологии.
Результат должен выглядеть так же, как схема в файле task_10_2c_topology.svg

При этом:
* Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме
'''

from draw_network_graph import draw_topology
import yaml

with open('topology.yaml') as f:
	topology = yaml.load(f)

# 		перепарсинг
# Перобразование из вида: {'R1': {'Eth 0/0': {'SW1': 'Eth 0/1'}}, 'R2': {'Eth 0/0': {'SW1': 'Eth 0/2'}}} 
#				 в	вид:	{('CentralRouter-1', 'Gig4/0'): ('khb-tet-lan1', 'Gig0/52')}
the_end={}

for Tk,Tv in topology.items():
	for k,v in Tv.items():
		for sk,sv in v.items():
			list1=[Tk,k]
			list2=[sk,sv] 
			tuple1=tuple(list1)
			tuple2=tuple(list2)
			the_end[tuple1] = tuple2

the_end_end={}
for pk,pv in the_end.items():
	if not pk in the_end_end.values():
		the_end_end[pk]=pv

print(the_end_end) 	

draw_topology(the_end_end)
