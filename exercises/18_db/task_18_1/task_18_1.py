#!/usr/bin/python
# -*- coding: utf-8 -*-
'''

На основе файла create_sqlite_ver3.py из примеров раздела, необходимо создать два скрипта:
* create_db.py
 * сюда должна быть вынесена функциональность по созданию БД:
  * должна выполняться проверка наличия файла БД
  * если файла нет, согласно описанию схемы БД в файле dhcp_snooping_schema.sql, должна быть создана БД (БД отличается от примера в разделе)
* add_data.py
 * с помощью этого скрипта, выполняется добавление данных в БД
  * добавлять надо не только данные из вывода sh ip dhcp snooping binding, но и информацию о коммутаторах

Код в скриптах должен быть разбит на функции.
Какие именно функции и как разделить код, надо решить самостоятельно.
Часть кода может быть глобальной.

В БД теперь две таблицы (схема описана в файле dhcp_snooping_schema.sql):
 * switches - в ней находятся данные о коммутаторах
 * dhcp - эта таблица осталась такой же как в примере, за исключением поля switch
  * это поле ссылается на поле hostname в таблице switches

Соответственно, в файле add_data.py должны быть две части:
* информация о коммутаторах добавляется в таблицу switches
 * данные о коммутаторах, находятся в файле switches.yml
* информация на основании вывода sh ip dhcp snooping binding добавляется в таблицу dhcp
 * вывод с трёх коммутаторов:
   * файлы sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt
 * так как таблица dhcp изменилась, и в ней теперь присутствует поле switch, его нужно также заполнять. Имя коммутатора определяется по имени файла с данными

На данном этапе, оба скрипта вызываются без аргументов.

'''
import glob,re,sqlite3,yaml,pprint
from create_db	import assay_to_exist_db_file,	create_db_file
from add_data	import create_data_for_db,		insert_data_to_db 

db_filename = 'dhcp_snooping.db'
schema_filename = 'dhcp_snooping_schema.sql'
dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')

regex_1 = '(\S+)  (.+)'
query_1 = '''insert into switches (hostname, location)
			values (?, ?)'''

regex_2	=	'(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+) +(\S+)'
query_2	=	'''insert into dhcp (mac, ip, vlan, interface, switch)
			values (?, ?, ?, ?, ?)'''

if assay_to_exist_db_file(db_filename) == False:
	create_db_file(db_filename, schema_filename)
else:
	print('Database exists, assume dhcp table does, too.')


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
			list_of_str_2.append(string.rstrip()+' '+file[:-4])

print('****OUTPUT create_data_for_db for "dhcp": ')
print(create_data_for_db (list_of_str_2, regex_2))

print('****************')
lot2=create_data_for_db (list_of_str_2, regex_2)
insert_data_to_db(lot2, query_2, db_filename)
