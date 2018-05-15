#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
create_db.py
* сюда должна быть вынесена функциональность по созданию БД:
 * должна выполняться проверка наличия файла БД
 * если файла нет, согласно описанию схемы БД в файле dhcp_snooping_schema.sql,
   должна быть создана БД (БД отличается от примера в разделе)

В БД теперь две таблицы (схема описана в файле dhcp_snooping_schema.sql):
 * switches - в ней находятся данные о коммутаторах
 * dhcp - эта таблица осталась такой же как в примере, за исключением поля switch
  * это поле ссылается на поле hostname в таблице switches

"""
import sqlite3
import os

db_filename = 'dhcp_snooping.db'
schema_filename = 'dhcp_snooping_schema.sql'

def assay_to_exist_db_file(db_file):
	'''
	Осуществляет провреку на наличие файла базы данных (БД).
	Ожидает: имя файла.
	Возвращает: True or False.
	'''
	# db_exists = os.path.exists(db_file)
	if os.path.exists(db_file):
		return	True
	if not os.path.exists(db_file):
		return	False
	else:
		print('^^^ в функци assay_exist_db_file Не True и не False ^^^')

def create_db_file(db_file, schema_file):
	'''
	Создает файл БД с таблицами из файла schema_filename.
	Ожидает: имя файла БД и имя файла со схемами таблиц. 
	Возвращает: -
	'''	
	conn = sqlite3.connect(db_file)

	print('Creating schema...')
	with open(schema_file, 'r') as f:
		schema = f.read()
	conn.executescript(schema)
	print('Done')

if __name__ == "__main__":
	if assay_to_exist_db_file(db_filename) == False:
		create_db_file(db_filename, schema_filename)
	else:
		print('Database exists, assume dhcp table does, too.')