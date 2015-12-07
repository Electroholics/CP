#launcher to run Stress testing script 
#Add the following lines to crontab 
#using crontab -e to start script on startup
#@reboot sh <path to file> 
#!/bin/sh
cd /
cd home/pi/local_run
sudo python timetest.py
cd /
