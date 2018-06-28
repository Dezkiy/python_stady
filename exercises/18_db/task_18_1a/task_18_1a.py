#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Задание 18.1a

Скопировать скрипт add_data.py из задания 18.1.

Добавить в файл add_data.py проверку на наличие БД:
* если файл БД есть, записать данные
* если файла БД нет, вывести сообщение, что БД нет и её необходимо сначала создать

'''


import glob,re,sqlite3,yaml,pprint
from create_db	import assay_to_exist_db_file,	create_db_file
from add_data	import create_data_for_db,		insert_data_to_db 

db_filename = 'dhcp_snooping.db'
schema_filename = 'dhcp_snooping_schema.sql'
dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')

# Регулярное выражения и запрос для такблици "switches"
regex_1 =	'(\S+)  (.+)'
query_1 = 	'''insert into switches (hostname, location)
			values (?, ?)'''

# Регулярное выражения и запрос для такблици "dhcp"
regex_2	=	'(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+) +(\S+)'
query_2	=	'''insert into dhcp (mac, ip, vlan, interface, switch)
			values (?, ?, ?, ?, ?)'''

# Проверяем существует ли файл базы(ф-я: assay_to_exist_db_file),
# если файла нет,то создаем (ф-я: create_db_file)
if assay_to_exist_db_file(db_filename) == False:
	create_db_file(db_filename, schema_filename)
else:
	print('Database exists, assume dhcp table does, too.')
	# Если файл базы есть, то подразумевается, что в ней есть таблица DHCP

print('==DATA fo creating table "switches"==')

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
insert_data_to_db(lot, query_1, db_filename)

print('==DATA fo creating table "dhcp"=====')

list_of_str_2=[]

for file in dhcp_snoop_files:
	with open (file) as f:
		for string in f:
			list_of_str_2.append(string.rstrip())

print('****OUTPUT create_data_for_db for "dhcp": ')
print(create_data_for_db (list_of_str_2, regex_2))

print('****************')
lot2=create_data_for_db (list_of_str_2, regex_2)
insert_data_to_db(lot2, query_2, db_filename)
