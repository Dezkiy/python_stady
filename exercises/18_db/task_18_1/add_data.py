#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
add_data.py
* с помощью этого скрипта, выполняется добавление данных в БД
* добавлять надо не только данные из вывода sh ip dhcp snooping binding, но и информацию о коммутаторах

В файле add_data.py должны быть две части:
* информация о коммутаторах добавляется в таблицу switches
 * данные о коммутаторах, находятся в файле switches.yml
* информация на основании вывода sh ip dhcp snooping binding добавляется в таблицу dhcp
 * вывод с трёх коммутаторов:
   * файлы sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt
 * так как таблица dhcp изменилась, и в ней теперь присутствует поле switch, его нужно также заполнять. 
   Имя коммутатора определяется по имени файла с данными
'''
import glob,re,sqlite3,yaml,pprint

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



if __name__ == "__main__":

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
	
	for file in dhcp_snoop_files:
		with open (file) as f:
			for string in f:
				list_of_str_2.append(string.rstrip())

	print('****OUTPUT create_data_for_db for "dhcp": ')
	print(create_data_for_db (list_of_str_2, regex_2))

	print('****************')
	lot2=create_data_for_db (list_of_str_2, regex_2)
	insert_data_to_db(lot2, query_2, db_filename)
