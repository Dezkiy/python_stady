#!/usr/bin/python	
# -*- coutf-8 -*-
'''
Функция check_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например,
192.168.100.1-10.

Создать функцию check_ip_availability, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

IP-адреса могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо проверить доступность всех адресов диапазон
а включая последний.

Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последни
й октет адреса.

Функция возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задачи можно воспользоваться функцией check_ip_addresses из задания 12.1
'''
import subprocess
import ipaddress
from task_12_1 import check_ip_addresses

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
	# print(ip_list)
	result=[]
	result2=[]
	for ip in ip_list:
		if is_it_ip(ip):
			result.append(ip)
		if '-' in ip:
			spip=ip.split('-')
			if '.' in spip[1]:# print('It is NOT ip ', ip)
				for i in range(int(spip[0].split('.')[3]),(int(spip[-1].split('.')[-1])+1)):
					result2.append('.'.join(spip[0].split('.')[:3])+'.'+str(i))
			else:
				for i in range(int(spip[0].split('.')[3]),(int(spip[-1])+1)):
					result2.append('.'.join(spip[0].split('.')[:3])+'.'+str(i))				
	result.extend(result2)
	return check_ip_addresses(result)

# input=['8.8.8.8-9','10.1.1.1-10.1.1.3','192.168.8.254','192.168.8.250','78.9.85.8']
# print(check_ip_availability(input))