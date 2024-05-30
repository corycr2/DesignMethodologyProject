#Begin ADC, The ADC is a DAC comparator. This comparator is hooked up to a difference amplifier to enable the user to determine low voltage and high
#voltage. So if the low voltage is 2v and the high voltage is 3v the ADC will print 1v. This is done by using the output of the difference amplifier
#into a comparator that checks against known voltages from the table below.

import rgb1602
import RPi.GPIO as GPIO
import time

adc = 6
GPIO.setmode(GPIO.BCM) 
GPIO.setup(adc, GPIO.IN, pull_up_down=GPIO.PUD_UP) #adc

#LCD setup
lcd=rgb1602.RGB1602(16,2)

#This is the ADC function
def ADC():
    #Tell the user what they are in
    lcd.setCursor(0, 0)                                     
    lcd.printout(f"Voltage: ")
    
    #Test Greater than 2v
    #Set voltage to 2v
    pi.hardware_PWM(12,10000, 49*10000)
    time.sleep(.03)
    if GPIO.input(adc) == 1: #Greater than 2v
        #Greater than 2v
        #set voltage to 3v
        pi.hardware_PWM(12,10000, 73*10000)
        time.sleep(.03)
        if GPIO.input(adc) == 1: #Greater than 3v
            #Greater than 3v
            #Set voltage to 3.5v
            pi.hardware_PWM(12,10000, 85*10000)
            time.sleep(.03)
            if GPIO.input(adc) == 1: #Greater than 3.5v
                #Greater than 3.5v
                #set voltage to 3.75v
                pi.hardware_PWM(12,10000, 91*10000)
                time.sleep(.03)
                if GPIO.input(adc) == 1: #Greater than 3.75v
                    #Greater than 3.75
                    #set voltage to 4v
                    pi.hardware_PWM(12,10000, 96*10000)
                    time.sleep(.03)
                    if GPIO.input(adc) == 1: #Greater than 4v
                        Voltage = 4         #voltage will be equal to 4v
                    else:
                        Voltage = 3.75      #voltage will be equal to 3.75
                #Less than 3.75
                else:
                    Voltage = 3.5           #voltage will be equal to 3.5v

            #Less than 3.5v  
            else:
                #set voltage to 3.25v
                pi.hardware_PWM(12,10000, 79*10000)
                time.sleep(.03)
                if GPIO.input(adc) == 1:
                    Voltage = 3.25           #voltage will be equal to 3.25v
                else:
                    Voltage = 3              #voltage will be equal to 3v

        #Less than 3v
        else:
            #set voltage to 2.5
            pi.hardware_PWM(12,10000, 61*10000)
            time.sleep(.03)
            if GPIO.input(adc) == 1:
                #Greater then 2.5v
                #set voltage to 2.75v
                pi.hardware_PWM(12,10000, 67*10000)
                time.sleep(.03)
                if GPIO.input(adc) == 1:
                    Voltage = 2.75          #voltage will be equal to 2.75v
                else:
                    Voltage = 2.5           #voltage will be equal to 2.5v

            #Less than 2.5v        
            else:
                #Set voltage to 2.25v
                pi.hardware_PWM(12,10000, 55*10000)
                time.sleep(.03)
                if GPIO.input(adc) == 1:
                    Voltage = 2.25          #voltage will be equal to 2.25v
                else:
                    Voltage = 2             #voltage will be equal to 2v

    #This means that it was less than 2v
    else:
        #set voltage to 1v
        pi.hardware_PWM(12,10000, 25*10000)
        time.sleep(.03)
        if GPIO.input(adc) == 1:
            #Greater than 1v
            #set voltage to 1.5v          
            pi.hardware_PWM(12,10000, 37*10000)
            time.sleep(.03)
            if GPIO.input(adc) == 1:
                #Greater than 1.5v
                #set voltage to 1.75v
                pi.hardware_PWM(12,10000, 43*10000)
                time.sleep(.03)
                if GPIO.input(adc) == 1:
                    Voltage = 1.75          #voltage will be equal to 1.75v
                #Less than 1.75v    
                else:
                    Voltage = 1.5           #voltage will be equal to 1.5v

            #Less than 1.5v        
            else:
                #set voltage to 1.25v
                pi.hardware_PWM(12,10000, 31*10000)
                time.sleep(.03)
                if GPIO.input(adc) == 1:
                    Voltage = 1.25          #voltage will be equal to 1.25v
                #Less than 1.25v    
                else:
                    Voltage = 1             #voltage will be equal to 1v
    
        #Less than 1v
        else:
            #set voltage to .5v
            pi.hardware_PWM(12,10000, 13*10000)
            time.sleep(.03)
            if GPIO.input(adc) == 1:
                #Greater than .5v
                #set voltage to .75v
                pi.hardware_PWM(12,10000, 19*10000)
                time.sleep(.03)
                if GPIO.input(adc) == 1:
                    Voltage = .75           #voltage will be equal to .75v
                #Less than .75v
                else:
                    Voltage = .5            #voltage will be equal to .5v
            else:
                #set voltage to .25v
                pi.hardware_PWM(12,10000, 7*10000)
                time.sleep(.03)
                if GPIO.input(adc) == 1:
                    Voltage = .25           #voltage will be equal to .25v
                #Less than .25v
                else:
                    Voltage = 0             #voltage will be equal to 0v
    
    #Update output lcd for user
    lcd.clear()
    lcd.setCursor(0, 0)                                     
    lcd.printout(f"Voltage: ")
    lcd.setCursor(0, 1)                                     
    lcd.printout(f"{Voltage}v +/- .25v")



