#!/bin/python
# -*- coding: utf-8 -*-

'''
Задание 11.2

и функции draw_topology из файла draw_network_graph.py
сгенерировать топологию, которая соответствует выводу
команды sh cdp neighbor в файле sw1_sh_cdp_neighbors.txt

Не копировать код функций parse_cdp_neighbors и draw_topology.

В итоге, должен быть сгенерировано изображение топологии.
Результат должен выглядеть так же, как схема в файле task_11_2_topology.svg

При этом:
* Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

from task_11_1 import parse_cdp_neighbors
from draw_network_graph import draw_topology

input=open('input2.txt')

topology_dict=(parse_cdp_neighbors(input))
    
#if __name__ == '__main__': 
#    print (parse_cdp_neighbors(input))

print (topology_dict)
draw_topology(topology_dict)

input.close()
