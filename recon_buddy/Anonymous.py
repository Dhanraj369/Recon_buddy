#sambhu
#!/usr/bin/env python
# Recon-buddy
# By Cipar-root 
# subscribe youtube channale >  https://www.youtube.com/channel/UCPGHkifv3-1i8j7pHThSHzg/featured
# github > https://github.com/Dhanraj369?tab=repositories

import os , time









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
     
     [1] Anonymous terminal
     [2] Anonymous Browseing 
    
     
   [ Linux command can be used here : e.i ls,clear , back]"""


def Anonymous_termin():


	print("*"*70)
	print("   whatever you type here or whatever request you search \n   from proxychains terminal this traffic goes through TOR  sockets \n   use :: nmap -sV -sC --script banner targe.com \n   nc[netcat]  -z 119.18.52.197 20-80 \n  you can also piing a host and captcher traffic in wireshark and look for sourse IP \n    or ping target.IP \n   as following example for use this terminal for any active/passive scan \n   no one can find out your private IP or about your devise\n   TIPS: run your real world target exploits from here ;-)\n ")
	print("*"*70)

	
	for x in range(100000):

		anon_inp=input("  proxychains ─# ")
		
		if anon_inp!="back":

			os.system(f"  proxychains {anon_inp}")
			print()
			print("*"*70)
			print("   enter command :: back [ for quit proxyterminal ]")
			print("*"*70)
			print()

		if anon_inp=="back":
			
			break





def Anonymous_brows():

	print("*"*70)
	print("   make shure you dont-t have root session here..")
	print("*"*70)

	print("""   choose your Browse for redirect traffic through TOR:\n     [1] Firefox   """)

	inp_brows=input("   choose 1 or to for your Browser ─# ")


	if inp_brows=="1":

		

		try:

			print("*"*70)
			print("   run TOR proxy through your Browser [ firefox , chrome ]\n   chack for DNSleak  on Browser:https://www.dnsleaktest.com/\n   and check for location : https://www.dnsleaktest.com/results.html\n   check your ISP or country  its true right !! ;) ")
			print("*"*70)
			os.system("proxychains firefox https://www.dnsleaktest.com")

		except Exception as e:
			raise
		else:
			os.system("bash /usr/share/recon_buddy/rootcheck_for_firefox_proxy.sh")

	else:
		print("invalid..........")
			
			








	

	



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
		get_num=input("""┌──(Cipar-root💀recon-bud)-[/Anonymous]
└─# """)

		if get_num=="back":

			os.system("python3 /usr/share/recon_buddy/startup.py") #startup file location
			exit()

		
		elif get_num==get_num and get_num != "exit" and get_num != "1" and get_num != "2" :

			os.system(get_num)
			if get_num=="clear":
				print(display_info)


		if get_num=="1":

			Anonymous_termin()

		if get_num=="2":
			
			Anonymous_brows()

		


