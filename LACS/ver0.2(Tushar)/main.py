#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import time
import software
import lcd

continue_reading = True
# GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)  #SETTING UP GPIO BOARD
GPIO.setup(29,GPIO.OUT)   #SETTING PIN 29 AS OUTPUT PIN TO RELAY 
GPIO.output(29,True)    #SETTING INITIAL VALUE AS TRUE AS RELAY IS TRIGGERED ON GROUND
lcd.lcd_init() #Intialising the LCD 
lock_delay=3
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
 


# This loop keeps checking for RFID cards. If one is near it will get the UID and authenticate
while continue_reading:
    #Using lcd to display on line 1
    lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD) 
    lcd.lcd_string("Welcome to LACS",1)
    #Setting default Trigger for Relay
    GPIO.output(29,True)
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print "Card detected"
        #Using lcd to display on line 1
        lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
        lcd.lcd_string("Card detected",1)   #log into lcd    
        # Get the UID of the card
        time.sleep(0.6)
        (status,uid) = MIFAREReader.MFRC522_Anticoll()
        print uid
        #Using lcd to display on UID
        lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
        lcd.lcd_string("Your UID:",1)
        #Using lcd to display on UID
        lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
        lcd.lcd_string(''.join(str(x) for x in uid),1)
        time.sleep(3) 
        lcd.lcd_string("",1)
        #Authentication
        (auth,name)=software.auth(uid)
        if(auth==1):
                #Displaying Welcome message on led with User's name
                lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
                lcd.lcd_string("WELCOME",1)
                lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
                lcd.lcd_string(name,1)
                #Trigerring Relay
                GPIO.output(29,False)
                time.sleep(lock_delay)
                lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
                lcd.lcd_string("",1)
        elif(auth==0):
                #Displaying Unauthorize attempt on LCD
                lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
                lcd.lcd_string("Unauthorize",1)
                lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
                lcd.lcd_string("attempt",1)
                lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
                lcd.lcd_string("",1)

            
    time.sleep(0.1)
