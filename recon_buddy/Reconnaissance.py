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

display_info=f""" =[ Reconnaissance  ]= \n
   Enter number for Dispaly :\n
     [1]  List TCP/UDP Listen Server     [8]   Display timers tcp/udp and PID ,State
     [2]  Rout Table                     [9]   All Listen Shocket and PID 
     [3]  Interfase Table                [10]  your IP  just everything about it 
     [4]  Network statistics             [11]  IP/ INTERFASE Forwarding Status
     [5]  Connected State Hardware       [12]  Discover All active system (MAC) AND (IP) (/16subnet)(LAN)
     [6]  All online and offline CPU     [13]  Logical IDS
     [7]  Statis file System info        [14]  which Service Start at Boot

       * for get back to main manu command : back *\n
       [ just greb whAT you need ] 

   [ Linux command can be used here : e.i ls,clear,back]"""

def setup():

	os.system("clear")
	print("╚═══╝"*16,end="\n\n")
	print(logo)
	print("╚══════╝"*10,end="\n\n")
	print(display_info)




def recon():

	os.system("clear")
	setup()
	while True:
		get_num=input("""┌──(Cipar-root💀recon-bud)-[/Reconnaissance]
└─# """)

		if get_num=="back":

			os.system("python3 /usr/share/startup.py") #startup file location
			exit()

		
		elif get_num==get_num and get_num != "exit" and get_num != "3" and get_num != "4" and get_num != "5" and get_num != "6" and get_num != "7" and get_num != "8" and get_num != "9" and get_num != "10"   and get_num != "11"   and get_num != "1"   and get_num != "2"   and get_num != "12"   and get_num != "13"   and get_num != "14"   and get_num != "15"   and get_num != "16"   and get_num != "17"  :
			os.system(get_num)
			if get_num=="clear":
				print(display_info)

#each and everu (--flag)falg i use here can be found in rool help manu which i use 
		if get_num=="1":
			print(" PID stand for process ID \n you can kill process usinf pid \n  use command : kill PID number under PID \nsleep 10 second to read.......")

			time.sleep(10)
			os.system("netstat --all --programs --tcp --udp")

		if get_num=="2":
			os.system("route --extend --numeric --verbose ")

		if get_num=="3":
			os.system("netstat --interfaces --tcp --udp")

		if get_num=="4":
			os.system("netstat --statistics")

		if get_num=="5":
		  os.system("netstat --symbolic --tcp --udp ")

		if get_num=="6":
			os.system("lscpu --all --extended -J &&  lscpu --all --parse -J") 

		if get_num=="7":
			os.system("less /etc/fstab")

		if get_num=="8":
			print(" PID stand for process ID \n you can kill process usinf pid \n  use command : kill PID number under PID \nsleep 10 second to read.......")

			time.sleep(10)
			os.system("netstat --timers --udp --tcp --programs")

		if get_num=="9":
			print(" PID stand for process ID \n you can kill process usinf pid \n  use command : kill PID number under PID \nsleep 10 second to read.......")

			time.sleep(10)
			os.system(" netstat  --listening --programs ")
			
		

		if get_num=="10":
			os.system("ip maddress && ip address && ip tcpmetrics && ip neighbour ")

		if get_num=="11":
			os.system("ip netconf")

		if get_num=="12":
		  os.system("netdiscover -f ")

		if get_num=="13":
			os.system("lscpu --output-all")

		if get_num=="14":
			print(" sign [+] means run after boot by default\n sign [-] means don't run after boot\nsleep for 6 second to read this..")
			time.sleep(6)
			os.system("service --status-all ")






		


	
	





