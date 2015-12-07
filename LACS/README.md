# Lab Access Control System

### About  
Lab access control system is a system built on Python with Raspberry Pi.The Project is an RFID interfaced Electronic system to restrict entry to lab. 

# Introduction to LACS:
## Basic Functionality
1)Detects Mifare Rfid cards
2)Displays Their UID(Function should be disabled while using in security systems like ours)
3)Authenticates Using MySQl database
4)Appends to log along with UNIX time stamp fetched from RTC
5)Triggers Relay accordingly

## Uses
1)Can be used as door entry mechanism.
2)Can be used as Attendance system.
3)Can be used in Electronic dispenser with certain changes.
4)Can be used in library for electronic issuing books.(Two Cards One for User other Inside the book)
..And lots of other Practical Uses.

## Setting up the system
###1)Connect the Relay and MFRC522 to switch mode power supply
###2)Connect RPi to external power supply
###3)Interface MFRC522 with Rpi
### a. Downloading and Installing official library to enable SPI communication with Python
### **Tip-Enable SPI and I2C using raspi-config** 
#### Type the Following commands in terminal   
`$ git clone https://github.com/lthiery/SPI-Py`  
`$ cd SPI-Py`  
`$ sudo python setup.py install`
### 4)Interfacing RTC with RPi
#### Enable the Kernel modules:-
`$ sudo nano /etc/modules`
#### Add the following:-
 i2c-bcm2708 
 i2c-dev
#### Save and reboot
#### Install the i2c tools for testing:-
`$ sudo i2cdetect -y 1`
#### For old models try 
`$ sudo i2cdetect -y 0`
#### You should see something like:-
`pi@raspberrypi ~ $ sudo i2cdetect -y 1`
`     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- UU -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- 68 -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
`
#### load up the RTC module and test by running :
`$ sudo modprobe rtc-ds1307`
`$ sudo bash`
`# echo ds1307 0x68 > /sys/class/i2c-adapter/i2c-1/new_device`
`# exit`
#### Check whether clock is running or not
`$ sudo hwclock -r`
#### Write the current system time to the hardware clock
`$ sudo hwclock -w`
#### Add the clock to the Kernel modules
`$ sudo nano /etc/modules`
#### Add line
`rtc-ds1307`
#### Reconfigure the hwclock.sh script
`$ sudo nano /etc/init.d/hwclock.sh`
#### After "unset TZ" add

    init_rtc_device()
    {
      [ -e /dev/rtc0 ] && return 0;
    
      # load i2c and RTC kernel modules
      modprobe i2c-dev
      modprobe rtc-ds1307
    
      # iterate over every i2c bus as we're supporting Raspberry Pi rev. 1 and 2
      # (different I2C busses on GPIO header!)
      for bus in $(ls -d /sys/bus/i2c/devices/i2c-*);
      do
        echo ds1307 0x68 >> $bus/new_device;
        if [ -e /dev/rtc0 ];
        then
          log_action_msg "RTC found on bus `cat $bus/name`";
          break; # RTC found, bail out of the loop
        else
          echo 0x68 >> $bus/delete_device
        fi
      done
    }
#### Find "case $1" and edit it as-

        case "$1" in
           start)
               # If the admin deleted the hwclock config, create a blank
               # template with the defaults.
               if [ -w /etc ] && [ ! -f /etc/adjtime ] && [ ! -e /etc/adjtime ]; then
                   printf "0.0 0 0.0\n0\nUTC" > /etc/adjtime
               fi
              init_rtc_device
        
       # Raspberry Pi doesn't have udev detectable RTC
               #if [ -d /run/udev ] || [ -d /dev/.udev ]; then
              #return 0
               #fi
#### Update the real HW clock and remove the fake:-
`sudo update-rc.d hwclock.sh enable
sudo update-rc.d fake-hwclock remove`
#### Now that real hardware clock is installed, remove the fake package and it’s crons:-
`sudo apt-get remove fake-hwclock
sudo rm /etc/cron.hourly/fake-hwclock
sudo rm /etc/init.d/fake-hwclock
`
#### Finally reboot and run our script to update Time from NTP server
`$ sudo bash init_rtc.sh`
####Stress Testing RTC module
####Install Twisted library for python
`$ sudo apt-get install python-dev`
`$ sudo apt-get install build-essential`
`$ sudo apt-get install python-twisted`
##### Run our python script 
`$ sudo python timetest.py`

This script runs after every second and logs unix timestamp into time.csv file
To check working of RTC remove power from raspi
After 5 minutes connect power and run our script or add the following to crontab

`$ crontab -e`

Add line

@reboot bash < path to script>

Check time.csv and [realtime unixtime stamp on another device](http://timestamp.1e5b.de/)

`$ tail -f time.csv`

### 5)Interfacing 16*2 LCD 

    # The wiring for the LCD is as follows:
    # 1 : GND
    # 2 : 5V
    # 3 : Contrast (0-5V)*
    # 4 : RS (Register Select)
    # 5 : R/W (Read Write)       - GROUND THIS PIN
    # 6 : Enable or Strobe
    # 7 : Data Bit 0             - NOT USED
    # 8 : Data Bit 1             - NOT USED
    # 9 : Data Bit 2             - NOT USED
    # 10: Data Bit 3             - NOT USED
    # 11: Data Bit 4
    # 12: Data Bit 5
    # 13: Data Bit 6
    # 14: Data Bit 7
    # 15: LCD Backlight +5V**
    # 16: LCD Backlight GND

Connect the following  pin of LCD to RPI
RPI----LCD
GND---01
+5V   ---02
GND---03
PIN37---04
GND---05
PIN35--06
 PIN33--11
 PIN15-12
 PIN13-13
 PIN11-14

For more info see lcd

###6)Configure your MySQL database
`mysql -u root -p`
`CREATE DATABASE [IF NOT EXISTS] databasename;`

a)Create Table

`CREATE TABLE [IF NOT EXISTS] table_name(`
`column_list`
`) engine=table_type`

 Our table has following columns
 
 

| sno    | int(11)  
| uid    | varchar(255)
| rollno | int(11)      
| name   | varchar(255) 




###7)Finally Run


` $ sudo python main.py`


## Hardware Requirements
1)Raspberry PI
2)Switch Mode Power Supply
3)MFRC522 Reader
4)Mifare Cards
5)4-pin Relay
6)16*2 lcd Display
7)RTC ds1307
8)Electromagnetic door lock
### To Do
Installing Three button Security
Installing Biometric system
Expanding into Lab control system with temp humidity sensors and live cams
Current sensing
PCB design for converting 12V to 3.3V
3D model for covering the system

### Installation
For Complete Installation guide , Refer this [wiki](https://github.com/Electroholics/CP/wiki/LACS---Installation)




