#!/usr/bin/python
# -*- coding: utf-8 -*-
'''

Добавить в файл add_data.py проверку на наличие БД:
* если файл БД есть, записать данные
* если файла БД нет, вывести сообщение, что БД нет и её необходимо сначала создать
'''

import glob,re,sqlite3,yaml,pprint
from create_db	import assay_to_exist_db_file,	create_db_file
from add_data	import create_data_for_db,		insert_data_to_db 

db_filename = 'dhcp_snooping.db'
# schema_filename = 'dhcp_snooping_schema.sql'
dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')

# Регулярное выражения и запрос для такблици "switches"
regex_1 =	'(\S+)  (.+)'
query_1 = 	'''insert into switches (hostname, location)
			values (?, ?)'''

# Регулярное выражения и запрос для такблици "dhcp"
regex_2	=	'(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+) +(\S+)'
query_2	=	'''insert into dhcp (mac, ip, vlan, interface, switch)
			values (?, ?, ?, ?, ?)'''


print('===============Data for creating table "switches"===============')

with open('switches.yml') as f:
	templates = yaml.load(f)

list_of_str_1=[]
li=list(list(templates.values())[0].items())
for c,v in li:
	list_of_str_1.append(c+'  '+v)

print('****OUTPUT create_data_for_db for "switches": ')
print(create_data_for_db (list_of_str_1, regex_1))

print('****************')
lot=create_data_for_db (list_of_str_1, regex_1)
insert_data_to_db(lot, query_1, db_filename, assay_to_exist_db_file(db_filename))

print('===============Data for creating table "dhcp"===================')

list_of_str_2=[]
for file in dhcp_snoop_files:
	with open (file) as f:
		for string in f:
			list_of_str_2.append(string.rstrip()+' '+file[:-4]) #file[:-4] - имя файла без расширения (последнии 4 символа). Эти данные идут в таблицу DHCP  в столбец switch

print('****OUTPUT create_data_for_db for "dhcp": ')
print(create_data_for_db (list_of_str_2, regex_2))

print('****************')
lot2=create_data_for_db (list_of_str_2, regex_2)
insert_data_to_db(lot2, query_2, db_filename, assay_to_exist_db_file(db_filename))
