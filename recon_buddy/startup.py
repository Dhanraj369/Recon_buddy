#sambhu
#!/usr/bin/env python
# Recon-buddy
# By Cipar-root 
# subscribe youtube channale >  https://www.youtube.com/channel/UCPGHkifv3-1i8j7pHThSHzg/featured
# github > https://github.com/Dhanraj369?tab=repositories

import os , time
from Reconnaissance import *
from scan_and_set import *
from Anonymous import * 
from Offensive import *

logo=""" 
    ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗      ██████╗ ██╗   ██╗██████╗ 
    ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║      ██╔══██╗██║   ██║██╔══██╗
    ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║█████╗██████╔╝██║   ██║██║  ██║
    ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║╚════╝██╔══██╗██║   ██║██║  ██║
    ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║      ██████╔╝╚██████╔╝██████╔╝
    ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝      ╚═════╝  ╚═════╝ ╚═════╝ """

Contributors=["Cipar-root"]

display_info=f"""   =[ Reconn-buddy ]= 
   =[ Version: 1.0.2 ]= 
   =[ Contributors: [ {Contributors[:]} ]=
   =[ this tool use for [A]ttack [H]ide and [S]can and [S]niff ]=

   Enter number for choose :
     
     [1] Reconnaissance 
     [2] Offensive 
     [3] Scan and set
     [4] Anonymous
     [5] read note from cipar-root

   [ Linux command can be used here : e.i ls,clear , exit]"""

def setup():

	os.system("clear")
	print("╚═══╝"*16,end="\n\n")
	print(logo)
	print("╚══════╝"*10,end="\n\n")
	print(display_info)


def getparameter():

	setup()
	while True:
		reply=input("""┌──(Cipar-root💀recon-bud)-[/]
└─# """)

		if reply=="exit":
			exit()
			os.system("exit")
		#using and != for all options because reply==reply
		elif reply==reply and reply != "exit" and reply != "1" and reply != "2" and reply != "3" and reply != "4" and reply != "5":
			os.system(reply)
			if reply=="clear":
				print(display_info)
		if reply=="5":
			os.system("less /usr/share/recon_buddy/talk.txt")
		if reply=="1":
			recon()
		if reply=="2":
			offinseve()
		if reply=="3":
			scan()
		if reply=="4":
			Anonymous()
			


getparameter()
