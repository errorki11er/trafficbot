import os
name = """ 
\033[1;32;40m   ____________________________________________________________
 _              __  __ _          ____        _
| |_ _ __ __ _ / _|/ _(_) ___    | __ )  ___ | |_
| __| '__/ _` | |_| |_| |/ __|   |  _ \ / _ \| __|
| |_| | | (_| |  _|  _| | (__    | |_) | (_) | |_
 \__|_|  \__,_|_| |_| |_|\___|___|____/ \___/ \__|
                            |_____|
\033[1;32;40m       ====================================================  
033[1;35;40m        [+] \033[1;37mTool By \033[1;31mERROR \033[1;37mKI11ER
033[1;32;40m____________________________________________________________
"""
try:
	from torrequest import TorRequest
except:
	os.system("pip install torrequest && clear")
	from torrequest import TorRequest

tr=TorRequest(password=None)

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"}
a = str(input("URL    - "))
x = int(input("Amount - "))

def run():
	for i in range(x):
		tr.reset_identity()
		response= tr.get(a)
		print(i+1)

run()
