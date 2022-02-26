import time
from colorama import init 
from colorama import Fore, Back, Style
import time
import smtplib
import subprocess
import multiprocessing
import os
from os import system
from progress.bar import IncrementalBar

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

bar = IncrementalBar('Bar', max = len(mylist))
print(Fore.BLUE)
print ('Off Anti-Virus')
print(Fore.GREEN)
for item in mylist:
    bar.next()
    time.sleep(0.1)
    bar.finish()
time.sleep(1)

    
while True:
	print('Ready! You phone have been killd! Wait 1 min! :3')
	time.sleep(0.1)

