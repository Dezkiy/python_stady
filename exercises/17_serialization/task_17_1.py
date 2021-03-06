#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Задание 17.1

В этом задании нужно:
* взять содержимое нескольких файлов с выводом команды sh version
* распарсить вывод команды с помощью регулярных выражений и получить информацию об устройстве
* записать полученную информацию в файл в CSV формате

Скрипт должен:
* обработать информацию из каждого файла с выводом sh version:
 * sh_version_r1.txt, sh_version_r2.txt, sh_version_r3.txt
* с помощью функции parse_sh_version, из каждого вывода должна быть получена информация ios, image, uptime
* из имени файла нужно получить имя хоста
* после этого вся информация должна быть записана в файл routers_inventory.csv

В файле routers_inventory.csv должны быть такие столбцы:
* hostname, ios, image, uptime

В скрипте, с помощью модуля glob, создан список файлов, имя которых начинается на sh_vers.
Вы можете раскомментировать строку print(sh_version_files), чтобы посмотреть содержимое списка.

Кроме того, создан список заголовков (headers), который должен быть записан в CSV.
'''
import glob
import csv
import re

sh_version_files = glob.glob('sh_vers*')

headers = ['hostname', 'ios', 'image', 'uptime']

def parse_sh_version(output):
	'''
	Функция parse_sh_version:
	* ожидает аргумент output в котором находится вывод команды sh version (не имя файла)
	* обрабатывает вывод, с помощью регулярных выражений
	* возвращает кортеж из трёх элементов:
	* ios - в формате "12.4(5)T"
	* image - в формате "flash:c2800-advipservicesk9-mz.124-5.T.bin"
	* uptime - в формате "5 days, 3 hours, 3 minutes"
	'''
	# result=tuple()
	result=[]	
	with open(output) as f:
		for line in f:
			match=re.search('^Cisco IOS Software.+Version\s+(?P<ios>\d+\.\d+\(\d+\)\w+),.+\)$'
							'|^System image file is "(?P<image>\w+:.+)"$'
							'|(?P<uptime>\d+\s+days,\s+\d+\s+hours,\s+\d+\s+minutes$)'
							,line)
			if match:
				result.append(match.group(match.lastgroup))
	return tuple(result)

def write_to_csv(file, inlist):
	'''
	Функция write_to_csv:
	* ожидает два аргумента:
 	* имя файла, в который будет записана информация в формате CSV
 	* данные в виде списка списков, где:
    	* первый список - заголовки столбцов,
   		* остальные списки - содержимое
	* функция записывает содержимое в файл, в формате CSV и ничего не возвращает
	'''
	with open(file, 'w') as f:
	    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC, delimiter='|')
	    writer.writerows(inlist)

listt=[headers]
for file in sh_version_files:
	host_name=re.search('sh_version_(\w+)\.\w+$',file)
	li=list(parse_sh_version(file))
	listt.append([host_name[1],li[0],li[2],li[1]])

write_to_csv('routers_inventory.csv',listt)
