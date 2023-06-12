#sambhu
#!/usr/bin/env python
# Recon-buddy
# By Cipar-root 
# subscribe youtube channale >  https://www.youtube.com/channel/UCPGHkifv3-1i8j7pHThSHzg/featured
# github > https://github.com/Dhanraj369?tab=repositories


if [[ $(id -u) -eq 0 ]]; then

    
    ping -c 1 8.8.8.8 > /dev/null 2>&1
    if [[ $? -eq 0 ]]; then
    
    	echo "Internet connection is online."
	array_apllication=("scapy" "openssl" "lighttpd" "crunch " "john" "hcxpcapngtool" "reaver" "hcxdumptool" "wash"  "mdk4" "tshark" "etterlog" "hostapd" "wpaclean" "hashcat" "packetforge-ng" "asleap" "xterm" "aircrack-ng"  "pixiewps" "bully" "nft"  "aireplay-ng" "dhcpd" "airmon-ng"  "hostapd-wpe" "airodump-ng" "beef-xss" "bettercap" "lspci" "iw"  "wireshark" "airgeddon" "tcpdump" "nmap" "ettercap" "dnsmasq" "searchsploit" "wafw00f" "dmitry" "tor" "proxychains" "macchanger" "nmap" "netstat" "netdiscover" "wireshark" "dmitry" "wafw00f" "tcpdump" "searchsploit" "route" "ip" )
    	for app in "${array_application[@]}"; do
	    echo "Installing $app..."
    	    sudo apt-get install -y "$app"
    	    echo "Done installing $app."
	done
	
        proxy(){

           cp recon_buddy/proxychains4.conf /etc/proxychains4.conf
         }
#malum he mere ko ak line ke liye functio ba diya jarurat nhi tha ;-)
        proxy
	pip install -r recon_buddy/requirements.txt
	
	echo "configering.... files..and setting up..."
	
	mkdir /usr/share/recon_buddy 
	cp -r recon_buddy/* /usr/share/recon_buddy
	
	cp recon_buddy/recon-bud  /usr/bin/
	
        rm -rf recon_buddy && rm run_me_first.sh
	
	
    else
    
    	echo "Internet connection is offline."
    fi
       
    
else
    echo "use [ sudo su ] to get root acess"
fi


















	


