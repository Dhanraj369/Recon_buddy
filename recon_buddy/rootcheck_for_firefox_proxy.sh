#sambhu
#!/usr/bin/env python
# Recon-buddy
# By Cipar-root 
# subscribe youtube channale >  https://www.youtube.com/channel/UCPGHkifv3-1i8j7pHThSHzg/featured
# github > https://github.com/Dhanraj369?tab=repositories

#!/bin/bash




check_user=`whoami`
if [[ $check_user == "root" ]]; then

	user=`uname -n`

	echo "   you are root now browser can't start with root user"

	echo "-----------------------------------------------------------------"

	echo "######################################################"
	echo -e "Don't use root user for this:: \n   firefox cant br run from this root session \n   ... redirecting traffic fail..\n   Here is manual way to do so :\n   step 1 : close exiting firefox browser  \n   step 2 ::  run command  below: proxychains firefox"
	echo "######################################################"

	echo -e "   chack for DNSleak  on Browser:https://www.dnsleaktest.com/\n   and check for location : https://www.dnsleaktest.com/results.html\n   check above link on firefox which open by this session \n   and look for your ISP OR COUNTRY  "

	echo "_---------------------------------------------------------------"
	su $user




fi

