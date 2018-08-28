# In_house_config_tool

This is a basic simple conifguration management tool for deplyoing the PHP web server on mupltipl nodes. 
I tired to make this tool in python as now a days python is used widely




File structure overview:

In_house_config_tool
+--- bootstrap.sh  
+--- code.py  
+--- metadata.txt  
+--- packages
     +--- install.txt	
     +--- uninstall.txt   
+--- README.md


Prcocess to configure:

-> To install package, make an entry of package in install.txt
-> To uninstall package, make an entry in uninstall.txt
-> For keeping the metadata of the file, keep them in a file name "metadata", keeping them with "=" sign and createa dictionary to make key and value pairs separated by "=" sign

Usage:

-> Use git clone from the repo
git clone https://github.com/Avdhesh2828/In_house_config_tool.git

-> Go to in dir:
In_house_config_tool

-> make executable both file bootstrap.sh  code.py
chmod +x bootstrap.sh
chmod +x code.py

-> Execute both scripts one by one
./bootstrap.sh
./code.py

-> Web server shoule be configure, you can access the web server by typing in web browser with port no






