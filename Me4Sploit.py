B = '\u0040\u006C\u0061\u006D\u0065\u0072\u0031\u0031\u0032\u0033\u0031\u0031' #blue
R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

import os
import csv
import sys
import time
import json
import argparse
import requests
import subprocess as subp
from shutil import which
from colorama import init 
from colorama import Fore, Back, Style
import time
import smtplib
import multiprocessing
from os import system
import re
version = '1.2'
#design me4
def banner():
	print( Fore.GREEN)
	print ('======================================================')
	print ('                                             create by Kat̵̙̞͔͛̒͝an/\                  ')
	print ('======================================================')
	print('▒█▀▄▀█ █▀▀ ░█▀█░ ▒█▀▀▀█ █▀▀█ █░░ █▀▀█ ░▀░ ▀▀█▀▀ ')
	print('▒█▒█▒█ █▀▀ █▄▄█▄ ░▀▀▀▄▄ █░░█ █░░ █░░█ ▀█▀ ░░█░░ ')
	print('▒█░░▒█ ▀▀▀ ░░░█░ ▒█▄▄▄█ █▀▀▀ ▀▀▀ ▀▀▀▀ ▀▀▀ ░░▀░░')
	print('                                                                                                \       1.2      /')
	print('                                                                                                  \________/')
	print('[1] ActiveKey')
	print('[2] Check Updates')
	print('[3] Exit')
	print('\n')
def code():
	print(Fore.GREEN)
	option = input('Me4Sploit ==>  ')
	if option == "1":
		print('                                 \n \n            Copy and Past \n \n' + Fore.YELLOW + '2jsjejHEkdjutt54lkvxa83etrbKB4hUeJLiwlfu56rhcksnrix')
		key = input ("Syst-Key: ")
		
		if key == "2jsjejHEkdjutt54lkvxa83etrbKB4hUeJLiwlfu56rhcksnrix":
			print( Fore.YELLOW )
			print('Active')
			time.sleep(2)
			lists = input ('[1] Gemail-hack \n[2] B0mb3r \n[3] Mail-Spammer \n[4] Brute_Force \n[5] Grab-Cam \n[6] Shark \nMe4Sploit ==>  ')
			if lists == "1":
				os.system('git clone https://github.com/Ha3MrX/Gemail-Hack')
				
			if lists == "2":
				os.system('git clone https://github.com/Denishnc/b0mb3r')
				
			if lists == "3":
				os.system('git clone https://github.com/pashokkok/Mail_Smmp')
			
			if lists == "4":
				os.system('git clone https://github.com/Tim55667757/pwd_brut')
				
			if lists == "5":
				os.system('git clone https://github.com/noob-hackers/grabcam')
			
			if lists == "6":
				os.system('git clone https://github.com/Bhaviktutorials/shark')
				
			else:
				print('ERROR: 102' + Fore.YELLOW + '$' + Fore.RED + 'Invalid Tool')
		
		else:
			print( Fore.RED )
			print('ERROR: 101' + Fore.YELLOW + '$' + Fore.RED + 'Invalid Syst-Key')
	if option == "2" :
		print(G + '[+]' + C + ' Проверка обновлений.....', end='')
		ver_url = 'https://raw.githubusercontent.com/pashokkok/Me4Sploit/main/version.txt'
		try:
			ver_rqst = requests.get(ver_url)
			ver_sc = ver_rqst.status_code
			if ver_sc == 200:
				github_ver = ver_rqst.text
				github_ver = github_ver.strip()
	
				if version == github_ver:
					print(C + '[' + G + ' Актуально ' + C +']' + '\n')
					return code()
				else:
					print(C + '[' + G + ' Доступно : {} '.format(github_ver) + C + ']' + '\n')
					return code()
			else:
				print(C + '[' + R + ' Статус : {} '.format(ver_sc) + C + ']' + '\n')
		except Exception as e:
			print('\n' + R + '[-]' + C + ' Исключение : ' + W + str(e))
	if option == "3" :
		exit()

try:
	banner()
	code()
	
except:
	print("error")