#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Задание 18.1a

Добавить в файл add_data.py проверку на наличие БД:
* если файл БД есть, записать данные
* если файла БД нет, вывести сообщение, что БД нет и её необходимо сначала создать
'''

import glob, sqlite3, re           #,os
from create_db import assay_to_exist_db_file

# db_filename = 'dhcp_snooping.db'
# dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')

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

def insert_data_to_db (list_of_tuple, query, db_file, assay_to_exist_db_file_IN_DEF):
	'''
	Добавляет данные в БД.
	Ожидает: списко кортежей, sqlite запрос,файл БД и флаг наличия файла ДБ.
	Есть проверка на наличие файла БД
	'''
	print('> Inserting data...')
	
	if assay_to_exist_db_file_IN_DEF == True:
		print ('>> File DB exist')
		conn = sqlite3.connect(db_file)

		for tupl in list_of_tuple:
			print(tupl)
			try:
				with conn:
					conn.execute(query, tupl)
			except sqlite3.IntegrityError as e:
				print('>>> Error occured: ', e)
		conn.close()
	else:
		print ('>> File DB does not exist')
