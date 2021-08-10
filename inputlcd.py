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
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)

lcd.clear()
  
lcd.show_cursor(False)
lcd.blink(False)

rolodex = sys.stdin.readlines()
lcd.message(rolodex[0].rstrip())
time.sleep(5)
if (sys.argv[1] == "clear"):
  lcd.clear()
if (sys.argv[1] == "repeat"):
  while "rolodex":
    for x in rolodex:
      #pause while time displays
      while (path.exists("/tmp/lock")):
       time.sleep(1)
      #check that message will fit
if len(word) < 34:
#check if message needs breaking
    if len(word) > 16:
        midpoint = 8
        #find the first space after the midpoint 
        space = word.find(' ', midpoint)
        last = word[space+1:]
      #if the last bit is too long to display, the midpoint needs to be earlier so that it can find a sooner space
        while len(last) > 16:
            midpoint = midpoint-1
            space = word.find(' ', midpoint)
            last = word[space+1:]
        first = word[:space]
        message = first + "\n" + last
    else:
        message = word
else:
    message = (len(word))
lcd.clear()
lcd.message(x.rstrip())
time.sleep(5)
