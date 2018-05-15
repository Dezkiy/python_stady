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
 * так как таблица dhcp изменилась, и в ней теперь присутствует поле switch, его нужно также заполнять. Имя коммутатора определяется по имени файла с данными

Код должен быть разбит на функции.
Какие именно функции и как разделить код, надо решить самостоятельно.
Часть кода может быть глобальной.
'''
import glob,re

db_filename = 'dhcp_snooping.db'
dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')

regex_1='(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)'
list_of_str_1=[
'00:09:BB:3D:D6:58   10.1.10.2        86250       dhcp-snooping   10    FastEthernet0/1',
'00:04:A3:3E:5B:69   10.1.5.2         63951       dhcp-snooping   5     FastEthernet0/10',
'00:05:B3:7E:9B:60   10.1.5.4         63253       dhcp-snooping   5     FastEthernet0/9',
'00:07:BC:3F:A6:50   10.1.10.6        76260       dhcp-snooping   10    FastEthernet0/3',
'00:09:BC:3F:A6:50   192.168.100.100  76260       dhcp-snooping   1     FastEthernet0/7'
]
def create_data_for_db (list_of_str, regex):
	'''
	Создает данные для передачи в БД.
	Ожидает: список строк и регулряное выражение для выборки.
	Возвращает: список кортежей. 
	'''
	result = []
	for str in list_of_str:
		match = re.search(regex, str)
		if match:
			result.append(match.groups())
	return result

print('Inserting DHCP Snooping data')

def insert_data_to_db ():
	'''
	Добавляет данные в БД.
	Ожидает: 
	Возвращает:	
	'''

	for row in result:
		try:
			with conn:
				query = '''insert into dhcp (mac, ip, vlan, interface)
						   values (?, ?, ?, ?)'''
				conn.execute(query, row)
		except sqlite3.IntegrityError as e:
			print('Error occured: ', e)

	conn.close()
	return

if __name__ == "__main__":
	print(create_data_for_db (list_of_str_1, regex_1))

	# for file in dhcp_snoop_files:
	# 	print('END')
