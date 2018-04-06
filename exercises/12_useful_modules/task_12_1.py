#!/usr/bin/python	
# -*- coding: utf-8 -*-

import subprocess
import ipaddress

def check_ip_addresses(list_ip_address):
	'''
	Проверяет доступность IP-адресов.

	Функция ожидает как аргумент список IP-адресов.
	И возвращает два списка:
	* список доступных IP-адресов
	* список недоступных IP-адресов

	Для проверки доступности IP-адреса, используйте ping.
	Адрес считается доступным, если на три ICMP-запроса пришли три ответа.
	'''
	wage=[]
	peeves=[]

	print(list_ip_address)
	for ip in list_ip_address: 
		print('pinging '+ip)
		reply = subprocess.run(['ping', '-c', '3', ip],
								stdout=subprocess.PIPE,
								stderr=subprocess.PIPE,
								encoding='utf-8')
		if reply.returncode == 0:
			wage.append(ip)
		else:
			peeves.append(ip)
	# print(wage,peeves)
	return wage, peeves

# print(check_ip_addresses(['8.8.8.8','192.168.8.254','7.8.78.7','192.168.8.252']))
