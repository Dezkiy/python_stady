#!/usr/bin/python	
# -*- coding: utf-8 -*-
'''
Создать функцию ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые переданы ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.
'''

import subprocess
import ipaddress
from tabulate import tabulate
from task_12_1 import check_ip_addresses

columns=['Reachable','Unreachable']

# input=['8.8.8.8-9','10.1.1.1-10.1.1.3','192.168.8.254','192.168.8.250','78.9.85.8']
input=['192.168.8.1-20']

def is_it_ip(ip):
	try:
		ipaddress.ip_address(ip)
		return True
	except ValueError:
		return False 

def check_ip_availability(ip_list):
	'''
	Функция проверяет доступность IP-адресов.
	Функция ожидает как аргумент список IP-адресов.
	IP-адреса могут быть в формате:
	* 10.1.1.1
	* 10.1.1.1-10.1.1.10
	* 10.1.1.1-10
	Если адрес указан в виде диапазона, надо проверить доступность всех адресов диапазон
	а включая последний.
	'''
	result=[]
	result2=[]
	for ip in ip_list:
		if is_it_ip(ip):
			result.append(ip)
		if '-' in ip:
			spip=ip.split('-')
			if '.' in spip[1]:
				for i in range(int(spip[0].split('.')[3]),(int(spip[-1].split('.')[-1])+1)):
					result2.append('.'.join(spip[0].split('.')[:3])+'.'+str(i))
			else:
				for i in range(int(spip[0].split('.')[3]),(int(spip[-1])+1)):
					result2.append('.'.join(spip[0].split('.')[:3])+'.'+str(i))
	result.extend(result2)
	return check_ip_addresses(result)

tup=check_ip_availability(input)
wage=tup[0]
peeves=tup[1]

def ip_table(wage,peeves):
	list=[wage,peeves]	
	if len(wage)!=len(peeves):
		if len(wage)>len(peeves):
			dif=len(wage)-len(peeves)
			for i in range(dif):
				peeves.append(' ')
		if len(peeves)>len(wage):
			dif=len(peeves)-len(wage)
			for i in range(dif):
				wage.append(' ')
	print(tabulate((zip(wage,peeves)), headers=columns))

ip_table(wage,peeves)