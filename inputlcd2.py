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
word = sys.stdin.readlines()
#test print 1: input/output
#print(word)
#set testrun to false
testrun = 0

def wordbreak(word):

  if len(word) < (lcd_rows*lcd_columns + 2):
    if len(word) > lcd_columns:
      midpoint = lcd_columns+1
      space = word.rfind(' ', 0, midpoint)
      last = word[space+1:]
      first = word[:space]
      #test print 3: length check
      #print(len(word))
      #print(len(first))
      #print(len(last))
      if (len(first) > lcd_columns):
        return "first row " + str(len(first))
      if (len(last) > lcd_columns):
        return "second row " + str(len(last))
      else:
        return first + "\n" + last

    else:
     return word
  else:
    return str(len(word))
    
#test print 2: broken word
#for x in word:
 #  print wordbreak(x)

def display(word):
  #check date 
  while (path.exists("/tmp/lock")):
         time.sleep(1)
  #take each item, clear screen, add wordbreak
  for x in word:
    lcd.clear()
    message = wordbreak(x)
    #test print 4: print the broken thing
    if testrun > 0:
      print(message)
    #display the broken thing
    lcd.message(message)
    #pause it
    time.sleep(5)
    #clear it
     

#if clear, display then clear
if len(sys.argv) > 1:
  if (sys.argv[1] == "clear"):
      display(word)
      lcd.clear()
  if (sys.argv[1] == "repeat"):
    while("rolodex"):
      display(word)
  if (sys.argv[1] == "print"):
    testrun = 1
    display(word)
 
else:
    display(word)
    time.sleep(1)
