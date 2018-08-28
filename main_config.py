#!/usr/bin/python

wiht open('uninstall.txt','r') as obj:
	for pkg in obj:
		cmd="dpkg -l | grep -i pkg"
		status,op_buffer=commands.getstatusoutput(cmd)
		if op_buffer:
			cmd1="sudo apt-get remove pkg"
			cmd2="sudo apt-get autoremove"
			cmd3="sudo apt-get purge -y $(dpkg --list |grep '^rc' |awk '{print $2}')"
			cmd4="sudo apt-get clean"



