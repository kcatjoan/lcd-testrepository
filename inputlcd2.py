#SETUP STARTS
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
#SETUP ENDS


#set input to word
rolodex = sys.stdin.readlines()
#print input
print(rolodex)
#the load-bearing thing
for x in rolodex:
  rolodex = x
  time.sleep(1)

def wordbreak(word):
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
#break and then print it for test reasons           
wordbreak(rolodex)
print(message)          

def display(word):
  #just copy-pasting the whole linebreak thing. APPLY LINEBREAK ETC TO INPUT#
    wordbreak(word)
    #print the broken thing
    print(message)
    #display the broken thing
    lcd.message(message)
    #pause it
    time.sleep(1)

#if clear, display then clear 
if (sys.argv[1] == "clear"):
  display(message)
  lcd.clear()
else:
  display(message)
  time.sleep(1)
