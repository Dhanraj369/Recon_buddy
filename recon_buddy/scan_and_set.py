#sambhu
#!/usr/bin/env python
# Recon-buddy
# By Cipar-root 
# subscribe youtube channale >  https://www.youtube.com/channel/UCPGHkifv3-1i8j7pHThSHzg/featured
# github > https://github.com/Dhanraj369?tab=repositories

import os , time

#ip scan func:
def ip_scan():

	options="""  choose number here after IP :\n   [1] Banner grabbing : IP 1\n   [2] Advanse ip scan : IP 2 [time consuming ~= 20m] \n   [3] Scan IP by nmap Scripts : IP 3\n"""
	
	ipinput=input("  enter IP OR domain to scan ─# ")
	print(options)
	print("  choose number from 1 to 3 ",end="")
	input_num=input("─# ")


	if input_num=="1":

		os.system(f"nmap  -Pn -sV -sC --script banner {ipinput}")

	if input_num=="2":

		os.system(f" nmap -Pn -sV -sC -Ar -O --reason --dns-servers  --traceroute -F {ipinput}")

	if input_num=="3":

		print("   ex. PROTOCOL : http,https,ftp,ssh\n   ex. servise : mysql,smb,mongodb,dns\n   enter command : All [for look all scripts]\n")
		script_find=input("  enter the name of PROTOCOL/servise ─# ")

		if script_find=="All" or "all":

			os.system("ls /usr/share/nmap/scripts/")

		if script_find!="All" or "all" or "":

			os.system(f"ls /usr/share/nmap/scripts/ | grep -e {script_find}")
			print()
			print("*"*69)
			print("   copy the name of script tou want to use with-out sxtension \n   valid :get > http-wordpress-brute.nse :use > http-wordpress-brute\n   invalid :get >http-wordpress-brute.nse :use > http-wordpress-brute.nse \n ")
			print("*"*69)
			input_name=input("enter your script name you find to apply ─# ")
			print("   \nnmap scan is processing...... please wait..a while....\n")
			os.system(f"nmap -Pn -sV --script {input_name} {ipinput}")


#-------------------------------------------------------------------

def search_exploit():

	print("   Information gather from : https://www.exploit-db.com/")
	print(""" ============
  Examples 
 ============
  search_exploit ─# Apache
  search_exploit ─# WordPress 4.1
  search_exploit ─# OpenSSH 8.7p1\n""")

	input_ser=input("   enter SERVICE or PROTOCOL for search_exploit ─# ")
  
	os.system(f"searchsploit --verbose -www {input_ser} && searchsploit --verbose {input_ser}")

	print("*"*69)
	print("   Above information is about EXPLOIT path in your system or url from exploit-db \n   download or copy exploit path or url and use it after modify \n   or use in metasploit : use multi/handler \n   you can also use search exploit -flag if you know!\n   ex. -j [service_name]\n")
	print("*"*69)


#-----------------------------------------------------------

def change_mac():

	options="""  choose number from 1 to 4 [on wlan0] :\n   [1] Set fully random MAC\n   [2] Reset to original, permanent hardware MAC \n   [3] Print the MAC address and exit \n   [4] Enter mac for change MAC XX:XX:XX:XX:XX:XX \n"""

	print(options)

	input_mac=input("   enter from above from 1 to 4 ─# ")

	if input_mac=="1":
		
		os.system("  ifconfig wlan0 down && macchanger --random wlan0 && ifconfig wlan0 up ")

	if input_mac=="2":
		
		os.system("  ifconfig wlan0 down && macchanger --permanent wlan0 && ifconfig wlan0 up ")

	if input_mac=="3":
		
		os.system("  ifconfig wlan0 down && macchanger --show wlan0 && ifconfig wlan0 up")

	if input_mac=="4":

		mac_add=input("   i hape you know format of MAC for assine \n   enter MAC in format =XX:XX:XX:XX:XX:XX \n   enter your desire MAC for assine to system  ─# ")
		
		os.system(f"  ifconfig wlan0 down && macchanger --mac={mac_add} wlan0 && ifconfig wlan0 up ")



#-------------------------------------------------------------------

def change_ip():
	
	ip_add=input("   enter IP for replase with real-one  ─# ")
	interfase_add=input("   ex- wlan0,etho,lo :enter your Interfase  ─# ")
		
	os.system(f"  ifconfig {interfase_add} {ip_add} ")

	print(f"check your ip on {interfase_add} :: command ifconfig {interfase_add}")



#-----------------------------------------------------------

def firewall_ids():


	print("   List all Firewall signature it's  able to detect command : list")

	check_firewall=input("   show : list or enter domain or IP for Identify Firewall ─# ")

	print("   this tool check for some signature of Firewall [ Take it as possibility ]")
	
	if check_firewall != "list" and check_firewall != "List" and check_firewall!="" :

		os.system(f"wafw00f -v --findall {check_firewall}")

	if check_firewall=="list" and check_firewall!="":
		os.system("wafw00f  --list")
	
	
#SABASH yaha tak pahunch gaay ;-}


#-------------------------------------------------------------------


def cap_traffic():
	
	options="""  choose number from 1 to 4 :\n   [1] Captucher all traffic over all Interfase \n   [2] Captucher all traffic between system:to:website  \n   [4] Captucher traffic over a Interfase"""

	print(options)

	input_val=input("choose from above 1 to 3 ─# ")


	if input_val=="1":
		
		#cap_traff_interfase=input("  enter Interfase name to Captucher traffic ─# ")
		print("   Captucher traffic over all Interfase ")
		os.system("tcpdump -i any -w all_interfase_traffic_capt.cap")
		#tcpdump net 192.168.43.1 
		ask=input("   open traffic Captucher  file in Wireshark [y/n] ─# ")

		if ask=="y":

			os.system("open all_interfase_traffic_capt.cap")

		if ask=="n":

			os.system(f"   echo file is save in current $(pwd)")

	if input_val=="2":

		print("   Captucher trafficbetween system::website Interfase ")

		cap_traff_interfase=input("  ex - wlan0,eth0,lo -enter Interfase name to Captucher traffic ─# ")

		ip_ask=input("   input your website or system IP [web IP not Domain ] ─# ")
		print("*"*69)
		print("    Do some request and response to Captucher traffic oe serve the webpage of target  \n   or send oe request on target system for Captucher")
		print("*"*69)

		os.system(f"   tcpdump -i {cap_traff_interfase} host {ip_ask} -w {ip_ask}.cap")

		ask2=input("   open traffic Captucher  file in Wireshark [y/n] ─# ")

		if ask2=="y":

			os.system(f"open {ip_ask}.cap")

		if ask2=="n":

			os.system(f"   echo file is save in current $(pwd)")
	if input_val=="3":

		cap_traff_interfase2=input("  ex - wlan0,eth0,lo -enter Interfase name to Captucher traffic ─# ")

		

		print("*"*69)
		print("    Do some request and response to Captucher traffic oe serve the webpage of target  \n   or send oe request on target system for Captucher")
		print("*"*69)

		os.system(f"   tcpdump -i {cap_traff_interfase2}  -w {cap_traff_interfase2}.cap")

		ask3=input("   open traffic Captucher  file in Wireshark [y/n] ─# ")

		if ask3=="y":
			os.system(f"open {cap_traff_interfase2}.cap")

		if ask3=="n":

			os.system(f"   echo file is save in current $(pwd)")



#---------------------------------------------------------

def dimittry():

	print("  [ recommended -use for CTF ] enter IP or domain for scan [ PORTS,EMAIL, Netcraft, Subdomain,TCP HOST ]")

	disply="""    [1] use for domain\n    [2] use foe IP"""

	print(disply)

	take_inpt=input("    choose from above 1 or 2 for corresponding result ─# ")

	if take_inpt=="1":

		domain_input=input("   enter domain of host  ─# ")

		os.system(f"dmitry -w {domain_input} ")
		os.system(f"dmitry -n {domain_input}")
		os.system(f"dmitry -s {domain_input}")
		os.system(f"dmitry -e {domain_input}")
		os.system(f"dmitry -p {domain_input}")
		os.system(f"dmitry -p -b {domain_input}")
		os.system(f"dmitry -p -f {domain_input}")

	if take_inpt=="2":
		
		ip_input=input("enter IP of host  ─# ")

		#os.system(f"dmitry -i {ip_input} && dmitry -n {ip_input} && dmitry  -s {ip_input} && dmitry -e {ip_input} && dmitry -p {ip_input} && dmitry -p -b {ip_input} && dmitry -p -f {ip_input} ")

		os.system(f"dmitry -i {ip_input} ")
		os.system(f"dmitry -n {ip_input}")
		os.system(f"dmitry -s {ip_input}")
		os.system(f"dmitry -e {ip_input}")
		os.system(f"dmitry -p {ip_input}")
		os.system(f"dmitry -p -b {ip_input}")
		os.system(f"dmitry -p -f {ip_input}")




#---------------close-----------------------fun-----------------------------------------------------

logo=""" 
    ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗      ██████╗ ██╗   ██╗██████╗ 
    ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║      ██╔══██╗██║   ██║██╔══██╗
    ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║█████╗██████╔╝██║   ██║██║  ██║
    ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║╚════╝██╔══██╗██║   ██║██║  ██║
    ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║      ██████╔╝╚██████╔╝██████╔╝
    ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝      ╚═════╝  ╚═════╝ ╚═════╝ """


Contributors=["Cipar-root"]

display_info=f""" =[ Scan and set  ]= \n
   Enter number for Dispaly :\n
     [1]  Advanse scan ip            
     [2]  search exploit                   
     [3]  Change macaddress               
     [4]  change ip address             
     [5]  Identify Firewall       
     [6]  Captucher Interfase Traffic
     [7]  scan for - PORT/EMAIL/Netcraft/Subdomain/TCP HOST   

       * for get back to main manu command : back *

   [ Linux command can be used here : e.i ls,clear,back]"""

def setup():

	os.system("clear")
	print("╚═══╝"*16,end="\n\n")
	print(logo)
	print("╚══════╝"*10,end="\n\n")
	print(display_info)




def scan():

	os.system("clear")
	setup()
	while True:
		get_num=input("""┌──(Cipar-root💀recon-bud)-[/Scan and set]
└─# """)

		if get_num=="back":

			os.system("python3 startup.py") #startup file location
			exit()

		
		elif get_num==get_num and get_num != "exit" and get_num != "3" and get_num != "4" and get_num != "5" and get_num != "6" and get_num != "7" and get_num != "1" and get_num != "2" :

			os.system(get_num)
			if get_num=="clear":
				print(display_info)

		if get_num=="1":

			ip_scan()

		if get_num=="2":
			search_exploit()

		if get_num=="3":
			change_mac()

		if get_num=="4":
			change_ip()

		if get_num=="5":

			firewall_ids()

		if get_num=="6":
			
			cap_traffic()

		if get_num=="7":
			
			dimittry()



	