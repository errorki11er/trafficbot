import os
name = """ 
____________________________________________________________
 _              __  __ _          ____        _
| |_ _ __ __ _ / _|/ _(_) ___    | __ )  ___ | |_
| __| '__/ _` | |_| |_| |/ __|   |  _ \ / _ \| __|
| |_| | | (_| |  _|  _| | (__    | |_) | (_) | |_
 \__|_|  \__,_|_| |_| |_|\___|___|____/ \___/ \__|
                            |_____|
====================================================  
[+] Tool By ERROR_KI11ER
____________________________________________________________
"""
import urllib
os.system('clear')
print(name)

try:
	from torrequest import TorRequest
except:
	os.system('pip install torrequest')


tr=TorRequest(password=None)

h = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"}
a = input("URL    - ")
x = int(input("Amount - "))

def run():
	for i in range(x):
		tr.reset_identity()
		response= tr.get(a,headers=h)
		print("Added",i+1,"Views")

run()
