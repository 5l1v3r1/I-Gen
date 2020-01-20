#!/usr/bin/python2

# Creator :  ./FUKUR0-3XP
# Team : Black Coders Satanic Exploiter Team ( BCA - X666X )
# Recode Tidak Akan Membuat Anda Menjadi Pencipta Kode :3

# coding: utf-8

import time
import sys
import os

M = '\033[1;31m'
H = '\033[1;32m'
K = '\033[1;33m'
U = '\033[1;34m'
P = '\033[1;35m'
C = '\033[1;36m'
W = '\033[1;37m'
A = '\033[90m'

def banner():
	print(''+C+'''
\t  _             _____            
\t (_)           / ____|           
\t  _   ______  | |  __  ___ _ __  
\t | | |______| | | |_ |/ _ \ '_ \ 
\t | |          | |__| |  __/ | | |
\t |_|           \_____|\___|_| |_|
              '''+W+'Creator : ./Fukur0\n\t\t   YT : Jejak Cyber')
        
def main():
	os.system('clear')
	banner() 
	print
	print
	f = raw_input(''+C+'Masukkan Kata : '+W+'')
	print
	print(''+C+'-------------- '+W+'Starting'+C+' --------------')
	print
	u = f.replace('A','I').replace('a','i').replace('U', 'I').replace('u','i').replace('E','I').replace('e', 'i').replace('O','I').replace('o','i')
	k = [
	'|', '/', '-', '\\', '|', '/', '-', '\\', '|', '/', '-', '\\', '|', '/', '-', '\\', '|', '/', '-', '\\', '|',str(u)+'\n']
	for i in k:
		print ''+H+'\rHasil : '+W+'➤ '+i,
		sys.stdout.flush()
		time.sleep(0.1)
	
def loop():
	print
	loop = raw_input('Ulang Lagi ? '+C+'['+W+'Y'+C+'/'+W+'n'+C+'] '+W+'')
	if loop == 'Y' or loop == 'y':
		main()
	else:
		sys.exit()
		
if __name__ == '__main__':
	main()
	loop()
