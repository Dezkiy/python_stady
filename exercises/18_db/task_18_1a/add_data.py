#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Задание 18.1a

Скопировать скрипт add_data.py из задания 18.1.

Добавить в файл add_data.py проверку на наличие БД:
* если файл БД есть, записать данные
* если файла БД нет, вывести сообщение, что БД нет и её необходимо сначала создать

'''

import glob,re,os,sqlite3,yaml,pprint

db_filename = 'dhcp_snooping.db'
dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')

regex_1='(\S+)  (.+)'
query_1='''insert into switches (hostname, location)
		values (?, ?)'''

regex_2='(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)'
query_2='''insert into dhcp (mac, ip, vlan, interface)
		values (?, ?, ?, ?)'''

def create_data_for_db (list_of_str, regex):
	'''
	Создает данные для передачи в БД процеживая строки через регулярное выражение.
	Ожидает: список строк и регулряное выражение для выборки.
	Возвращает: список кортежей. 
	'''
	result = []
	for str in list_of_str:
		match = re.search(regex, str)
		if match:
			result.append(match.groups())
	return result

def insert_data_to_db (list_of_tuple, query, db_file):
	'''
	Добавляет данные в БД.
	Ожидает: списко кортежей, sqlite запрос и файл БД.
	'''
	print('Inserting data')
	
	conn = sqlite3.connect(db_file)

	for tupl in list_of_tuple:
		print(tupl)
		try:
			with conn:
				conn.execute(query, tupl)
		except sqlite3.IntegrityError as e:
			print('Error occured: ', e)
	conn.close()

# ##
# db_exists = os.path.exists(db_filename)

# conn = sqlite3.connect(db_filename)

# if not db_exists:
#     print('Creating schema...')
#     with open(schema_filename, 'r') as f:
#         schema = f.read()
#     conn.executescript(schema)
#     print('Done')
# else:
#     print('Database exists, assume dhcp table does, too.')
##

if __name__ == "__main__":
	
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

	print('=========================')
	
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
