#!/usr/bin/python

import commands
import os

#########################################################
#					       	      ###
# Check for package update with update manager 	      ###
#						      ###
#########################################################


package_update = "sudo apt-get update"
status,op_buffer_pkgupdate=commands.getstatusoutput(package_update)


############################################################
##                                                        ##
##                                                        ##
##  Remove Debian Packages provided in uninstall.txt file ##
##                                                        ##
############################################################


with open('packages/uninstall.txt','r') as obj:
	for pkg in obj:
		pkg = pkg.rstrip('\n')
		cmd = "dpkg -l | grep -i %s" % pkg
		status,op_buffer=commands.getstatusoutput(cmd)
		if op_buffer:
			cmd1="sudo apt-get remove %s -y" % pkg
			status1,op_buffer1=commands.getstatusoutput(cmd1)
			cmd2="sudo apt-get autoremove -y"
			cmd3="sudo apt-get purge -y $(dpkg --list |grep '^rc' |awk '{print $2}')"
			cmd4="sudo apt-get clean -y"
			status,op_buffer2=commands.getstatusoutput(cmd2)
			status,op_buffer3=commands.getstatusoutput(cmd3)
			status,op_buffer4=commands.getstatusoutput(cmd4)



###########################################################
##							 ##
##							 ##
##  Install Debian Packages provided in install.txt file ##
##							 ##
###########################################################
with open('packages/install.txt','r') as obj:
        for pkg in obj:
                pkg = pkg.rstrip('\n')
                cmd = "dpkg -l | grep -i %s" % pkg
                status,op_buffer=commands.getstatusoutput(cmd)
                if not op_buffer:
                        cmd1="sudo apt-get install %s -y" % pkg
                        status1,op_buffer1=commands.getstatusoutput(cmd1)




###################################################################
###								 ##
###								 ##
### Replace default index.html with index.php if the file exists ##
###								 ##
###################################################################

if os.path.isfile('/var/www/html/index.html'):
        os.remove('/var/www/html/index.html')
        os.mknod("/var/www/html/index.php")


# Build our associative array from key val pairs in metadata.txt
# Note: Separator and order are important in this text file

# Runs only if uninstall lot empty

###################################################
#						###
#  Create a dictionary for applying metadata  #####
#						###	
###################################################

with open('metadata.txt','r') as obj:
	dict = {}
	for line in obj:
		pkg = line.rstrip('\n')
		key = pkg.split("=")[0]
		value = pkg.split("=")[1]
		dict[key] = value



##################################################
##					    ######
##  Applyint metadata propert 		    ######
##					    ######	
##################################################

cmd11 = "sudo chmod %s %s" %( dict['permission'], dict['file'])
cmd12 = "sudo chown %s %s" %( dict['owner'], dict['file'])
cmd13 = "sudo chgrp %s %s" %( dict['group'], dict['file'])

status,op_buffer=commands.getstatusoutput(cmd11)
status,op_buffer=commands.getstatusoutput(cmd12)
status,op_buffer=commands.getstatusoutput(cmd13)




#################################################
###					     ####
###  Updating the content of index.html file ####
###					     ####
#################################################

file_name = dict['file']
with open(file_name,"w") as obj:
	obj.write(dict['content'])

######################################################################
# checks which daemons need to be restarted after library upgrades  ##
######################################################################
start = "needrestart"
status,op_buffer=commands.getstatusoutput(start)
