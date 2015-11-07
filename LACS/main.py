#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import time
import software

continue_reading = True
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)  #SETTING UP GPIO BOARD
GPIO.setup(29,GPIO.OUT)   #SETTING PIN 29 AS OUTPUT PIN TO RELAY 
GPIO.output(29,True)    #SETTING INITIAL VALUE AS TRUE AS RELAY IS TRIGGERED ON GROUND

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print "Welcome to LACS"


# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading: 
    
    GPIO.output(29,True)
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print "Card detected"    
        # Get the UID of the card
        (status,uid) = MIFAREReader.MFRC522_Anticoll()
        print uid
		#Creating the Log
	software.log(uid) 
        # If we have the UID, continue

        authenticated = software.auth(uid)
        if int(authenticated) == 1:
			GPIO.output(29,False)
        else:
            print "Authentication error"
            #Adding delay of 0.1 sec for user to enter
	
	time.sleep(0.1)
