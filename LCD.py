#This file uses the LCD screen provided and chooses random values for red, green, and blue and sends it to the LCD to randomly change its color.
import rgb1602
from random import randrange

#LCD setup
lcd=rgb1602.RGB1602(16,2)

#Start LCD_Color function
def LCD_Color():
    #set red green and blue to random variables between 0 and 255
    a = randrange(255)
    b = randrange(255)
    c = randrange(255)
    #set the lcd color from the random variables
    lcd.setRGB(a, b, c)
