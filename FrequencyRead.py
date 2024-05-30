#This file is a frequency read file it uses the input from GPIO 4 to read freqeuncies of an external circuit. This is done by using
#a comparator that can flip from high and low. This flip happens after the circuit gets past .6v. This allows for the user to be able 
#to read a freqeucny from any source with the limitations the top of the wave must past .6v and the low end of the wave must be under .6v.

import sys
sys.path.append('../')
import rgb1602
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

#LCD setup
lcd = rgb1602.RGB1602(16,2)

#Initialize count
count = 0

#Everytime a rising edge is detected increment count
def count_pulse(channel):
    global count
    count += 1

#Begin read function
def read():
    global count
    
    #Get starting time
    starttime = time.time()
    
    #Update uses letting them know that it is reading frequency.
    lcd.clear()
    lcd.setCursor(0,0)
    lcd.printout("Reading")
    lcd.setCursor(0,1)
    lcd.printout("Frequency ")
    
    #Create an event detect that goes to the count function. This is done by having the GPIO pin check for a high voltage. GPIO pins check for a voltage 
    #Greater than .8v. The compartor makes the GPIO high by having the voltage go to 3.3v.
    GPIO.add_event_detect(4, GPIO.RISING, callback=count_pulse)
    
    #Wait 10 seconds to get multiple readings for accuracy.
    time.sleep(10)
    
    #Measure the time expended.
    elasped_time = time.time() - starttime
    
    #Return the read time back to the user
    readfreq = (count/elasped_time)*1.0123 #equal to (1/T)/number of times read.  1.01 is an offset for more accurate reading
    lcd.clear()
    lcd.setCursor(0,0)
    lcd.printout("Frequency is:")
    lcd.setCursor(0,1)
    lcd.printout(f"{int(readfreq)}Hz")
    time.sleep(4)
    count = 0
    
    #Remove the event detect to prevent issues
    GPIO.remove_event_detect(4)
#End read function
