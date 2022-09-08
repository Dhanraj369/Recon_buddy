#sambhu
#!/usr/bin/env python
# Recon-buddy
# By Cipar-root 
# subscribe youtube channale >  https://www.youtube.com/channel/UCPGHkifv3-1i8j7pHThSHzg/featured
# github > https://github.com/Dhanraj369?tab=repositories



#updating and internet check

check_user=`whoami`

if [[ $check_user != "root" ]]; then
	echo "enter command = sudo su"
	sleep 5
	exit

	fi

online=`fping google.com`
if [[ $online=="google.com is alive" ]]; then
	echo "updating ...."
	apt-get update 
else
	echo "system is offline check your internet connection..";
fi



array_apllication=("scapy" "openssl" "lighttpd" "crunch " "john" "hcxpcapngtool" "reaver" "hcxdumptool" "wash"  "mdk4" "tshark" "etterlog" "hostapd" "wpaclean" "hashcat" "packetforge-ng" "asleap" "xterm" "aircrack-ng"  "pixiewps" "bully" "nft"  "aireplay-ng" "dhcpd" "airmon-ng"  "hostapd-wpe" "airodump-ng" "beef-xss" "bettercap" "lspci" "iw"  "wireshark" "airgeddon" "tcpdump" "nmap" "ettercap" "dnsmasq" "searchsploit" "wafw00f" "dmitry" "tor" "proxychains" "macchanger" "nmap" "netstat" "netdiscover" "wireshark" "dmitry" "wafw00f" "tcpdump" "searchsploit" "route" "ip" )


for (( i = 0; i <= 53; i++ )); do
	#apt-get install ${array_apllication[@]:$i} 
	apt-get install ${array_apllication[$i]} -y

done

proxy(){

    cp recon_buddy/proxychains4.conf /etc/proxychains4.conf
}
#malum he mere ko ak line ke liye functio ba diya jarurat nhi tha ;-)
proxy

#checking user for root

pip install -r recon_buddy/requirements.txt




check_user=`whoami`
if [[ $check_user != "root" ]]; then
	echo "enter command = sudo su"
elif [[ $check_user=="root" ]]; then
	
	echo "configering.... files..and setting up..."
	
	mkdir /usr/share/recon_buddy 
	cp -r recon_buddy/* /usr/share/recon_buddy
	
	cp recon_buddy/recon-bud  /usr/bin/
fi


rm -rf recon_buddy && rm run_me_first.sh