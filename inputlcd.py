#!/usr/bin/python
# Example using a character LCD connected to a Raspberry Pi or BeagleBone Black.
import time

import os.path 
from os import path

import Adafruit_CharLCD as LCD

import sys
# Raspberry Pi pin configuration:
lcd_rs        = 25  # Note this might need to be changed to 21 for older revision Pi's.
lcd_en        = 24
lcd_d4        = 23
lcd_d5        = 17
lcd_d6        = 18
lcd_d7        = 22
lcd_backlight = 4

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

lcd.clear()
  
lcd.show_cursor(False)
lcd.blink(False)
#word is input
word = sys.stdin.readlines()

#repeat causes loop, which really only works if input is rolodex.py

for x in word:
  word = x
  time.sleep(1)
  #just copy-pasting the whole linebreak thing. APPLY LINEBREAK ETC TO INPUT#
  if len(word) < 34:
    if len(word) > 16:
        midpoint = 8
        while len(word[midpoint:]) > 16:
            midpoint = midpoint+1
        space = word.find(' ', midpoint)
        last = word[space+1:]
        first = word[:space]
        message = first + "\n" + last
    else:
         message = word
        #end of linebreak stuff
#print the broken thing
    print(message)
#display the broken thing
    lcd.message(message)
#pause it
    time.sleep(1)
#if it says to clear it, clear it
    if (sys.argv[1] == "clear"):
      lcd.clear()
#if it says repeat....
    if (sys.argv[1] == "repeat"):
  #continue forever except at the date
      while "rolodex":
        while (path.exists("/tmp/lock")):
         time.sleep(1)
        #wipe the lcd
        lcd.clear()
        #display the message(which is the broken thing)
        lcd.message(message)
        #pause
        time.sleep(1)
        #end of paste
#i think this next chunk is redundant so im commenting it out
#applies linebreak thing to word
#if len(word) < 34:
 #   if len(word) > 16:
  #      midpoint = 8
   #     while len(word[midpoint:]) > 16:
   #         midpoint = midpoint+1
    #    space = word.find(' ', midpoint)
     #   last = word[space+1:]
      #  first = word[:space]
       # message = first + "\n" + last
 #   else:
  #       message = word
   # print(message)
#    lcd.message(message)
 #   time.sleep(1)
  #  if (sys.argv[1] == "clear"):
   #   lcd.clear()
    #if (sys.argv[1] == "repeat"):
  #start of fresh copy'
#      while "rolodex":
 #       while (path.exists("/tmp/lock")):
  #       time.sleep(1)
   #     lcd.clear()
    #    lcd.message(message.rstrip())
     #   time.sleep(1)
        #end
      
#else:
    #message = (len(word))
   # print(message)
    
#between here and prev comment should set the correct message
