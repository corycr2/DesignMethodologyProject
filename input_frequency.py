#This file is used for updating values determined from the user. The values include frequency, amplitude, and voltage value in. They each work exactly the same.
#Using the rotary encoder we can update values. Using a time function we can determine how long it was between the last input and the current one. This 
#can be used to increase how much each value is being updated by. Each function also has limits to prevent the user from being able to select something outside
#the possiblities of our project.

import pigpio
import rgb1602
import time
import RPi.GPIO as GPIO

#Class to set up values dedicated to the encoder
class encoder:
    clk = 18
    dt = 23
    sw = 24

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(encoder.clk, GPIO.IN, pull_up_down=GPIO.PUD_UP) #clk
GPIO.setup(encoder.dt, GPIO.IN, pull_up_down=GPIO.PUD_UP) #dt
GPIO.setup(encoder.sw, GPIO.IN, pull_up_down=GPIO.PUD_UP) #sw


#LCD setup
lcd = rgb1602.RGB1602(16,2)
frequency = 1000

#setup pigipo for reading frequency
pi = pigpio.pi()

#Begin input frequency
def input_frequency1(frequency):
    #initialize values
    previousValue = 1
    prev_time = time.time()
    lcd.clear()
    lcd.setCursor(0, 0)         
    lcd.printout(f"Select with knob")
    lcd.setCursor(0, 1)
    lcd.printout(f"{frequency} Hz")
    
    #while the user has not pressed the rotary encoder update values once pressed stop.
    while(GPIO.input(encoder.sw) != 0):
        current_time = time.time()
        if previousValue != GPIO.input(encoder.clk):            #this is to poll the rotary encoder to check if anything is changed so it is not always running through the code.
            if GPIO.input(encoder.clk) == 0:                    #if encoder.clk is open prior to dt than you know the knob is being spun anti clockwise and can update values accordingly
                if GPIO.input(encoder.dt) == 0:
                    direction = "anti-clockwise"
                    speed = current_time - prev_time
                    if speed < .2:                      #speed is to test how fast the knob is spinning this is just recorded from current time to last time the knob was spun
                        if (frequency - 100) > 100:    
                            frequency -= 100
                        else:
                            frequency = 100
                    elif (frequency - 10) > 100:
                        frequency -= 10
                    else:
                        frequency = 100
                    #print(f"Direction: {direction}, frequency: {frequency}, Speed: {speed}")      #this shows what direction the user spun the knob the new frequency value and how fast the spin was this if for debugging
                    lcd.clear()
                    lcd.setCursor(0, 0)                     #cursor requires a row and column number for the display this just says start from top right
                    lcd.printout(f"Select with knob")       #print to display
                    lcd.setCursor(0, 1)                     #cursor points to second row
                    lcd.printout(f"{frequency} Hz")      #print to display
                    time.sleep(.1)                          #This is for a debounce so the rotary encoder is not double reading or reading backwards. 
                    prev_time = current_time                #update time
                else:                                       #this is to show dt was before clk meaning this part of the function is for clock wise everything below is the same as above but calculated for going clockwise instead of anti clockwise
                    direction = "clockwise"
                    speed = current_time - prev_time
                    if speed < .2:
                        if (frequency + 100) < 10000:
                            frequency += 100
                        else:
                            frequency = 10000
                    elif (frequency + 10) < 10000:
                        frequency += 10
                    else:
                        frequency = 10000
                    #print(f"Direction: {direction}, frequency: {frequency}, Speed: {speed}")
                    lcd.clear()
                    lcd.setCursor(0, 0)         
                    lcd.printout(f"Select with knob")
                    lcd.setCursor(0, 1)
                    lcd.printout(f"{frequency} Hz")
                    time.sleep(.1)
                    prev_time = current_time                
            previousValue = GPIO.input(encoder.clk)                 #update previous value for polling so you can retest if something has changed
    return frequency
#End input frequency

#Begin input amplitude
def input_amplitude(amplitude):
    previousValue = 1
    prev_time = time.time()
    lcd.clear()
    lcd.setCursor(0, 0)         
    lcd.printout(f"Select with knob")
    lcd.setCursor(0, 1)
    lcd.printout(f"{amplitude} v")
    while(GPIO.input(encoder.sw) != 0):
        current_time = time.time()
        if previousValue != GPIO.input(encoder.clk):            #this is to poll the rotary encoder to check if anything is changed so it is not always running through the code.
            if GPIO.input(encoder.clk) == 0:                    #if encoder.clk is open prior to dt than you know the knob is being spun anti clockwise and can update values accordingly
                if GPIO.input(encoder.dt) == 0:
                    speed = current_time - prev_time
                    if speed < .2:              #speed is to test how fast the knob is spinning this is just recorded from current time to last time the knob was spun
                        if (amplitude - 1) > 1:    
                            amplitude -= 1
                        else:
                            amplitude = 1
                    elif (amplitude - .25) > 1:
                        amplitude -= .25
                    else:
                        amplitude = 1
                    #print(f"Direction: {direction}, frequency: {frequency}, Speed: {speed}")      #this shows what direction the user spun the knob the new frequency value and how fast the spin was this if for debugging
                    lcd.clear()
                    lcd.setCursor(0, 0)                     #cursor requires a row and column number for the display this just says start from top right
                    lcd.printout(f"Select with knob")       #print to display
                    lcd.setCursor(0, 1)                     #cursor points to second row
                    lcd.printout(f"{amplitude} v")      #print to display
                    time.sleep(.1)                          #This is for a debounce so the rotary encoder is not double reading or reading backwards. 
                    prev_time = current_time                #update time
                else:                                       #this is to show dt was before clk meaning this part of the function is for clock wise everything below is the same as above but calculated for going clockwise instead of anti clockwise
                    speed = current_time - prev_time
                    if speed < .2:
                        if (amplitude + 1) < 5:
                            amplitude += 1
                        else:
                            amplitude = 5
                    elif (amplitude + .25) < 5:
                        amplitude += .25
                    else:
                        amplitude = 5
                    #print(f"Direction: {direction}, frequency: {frequency}, Speed: {speed}")
                    lcd.clear()
                    lcd.setCursor(0, 0)         
                    lcd.printout(f"Select with knob")
                    lcd.setCursor(0, 1)
                    lcd.printout(f"{amplitude} v")
                    time.sleep(.1)
                    prev_time = current_time                
            previousValue = GPIO.input(encoder.clk)                 #update previous value for polling so you can retest if something has changed
    return amplitude
#End input amplitude

#Begin DC Reference
def DC_Reference1(voltage):
    previousValue = 1
    prev_time = time.time()
    lcd.clear()
    lcd.setCursor(0, 0)         
    lcd.printout(f"Select with knob")
    lcd.setCursor(0, 1)
    lcd.printout(f"{voltage} v")
    while(GPIO.input(encoder.sw) != 0):
        current_time = time.time()
        if previousValue != GPIO.input(encoder.clk):            #this is to poll the rotary encoder to check if anything is changed so it is not always running through the code.
            if GPIO.input(encoder.clk) == 0:                    #if encoder.clk is open prior to dt than you know the knob is being spun anti clockwise and can update values accordingly
                if GPIO.input(encoder.dt) == 0:
                    direction = "anti-clockwise"
                    speed = current_time - prev_time
                    if speed < .2:              #speed is to test how fast the knob is spinning this is just recorded from current time to last time the knob was spun
                        if (voltage - 1) > 0:    
                            voltage -= 1
                        else:
                            voltage = 0
                    elif (voltage - .25) > 0:
                        voltage -= .25
                    else:
                        voltage = 0
                    #print(f"Direction: {direction}, frequency: {frequency}, Speed: {speed}")      #this shows what direction the user spun the knob the new frequency value and how fast the spin was this if for debugging
                    lcd.clear()
                    lcd.setCursor(0, 0)                     #cursor requires a row and column number for the display this just says start from top right
                    lcd.printout(f"Select with knob")       #print to display
                    lcd.setCursor(0, 1)                     #cursor points to second row
                    lcd.printout(f"{voltage} v")      #print to display
                    time.sleep(.1)                          #This is for a debounce so the rotary encoder is not double reading or reading backwards. 
                    prev_time = current_time                #update time
                else:                                       #this is to show dt was before clk meaning this part of the function is for clock wise everything below is the same as above but calculated for going clockwise instead of anti clockwise
                    direction = "clockwise"
                    speed = current_time - prev_time
                    if speed < .2:
                        if (voltage + 1) < 4:
                            voltage += 1
                        else:
                            voltage = 4
                    elif (voltage + .25) < 4:
                        voltage += .25
                    else:
                        voltage = 4
                    #print(f"Direction: {direction}, frequency: {frequency}, Speed: {speed}")
                    lcd.clear()
                    lcd.setCursor(0, 0)         
                    lcd.printout(f"Select with knob")
                    lcd.setCursor(0, 1)
                    lcd.printout(f"{voltage} v")
                    time.sleep(.1)
                    prev_time = current_time                
            previousValue = GPIO.input(encoder.clk)                 #update previous value for polling so you can retest if something has changed
    return voltage
#End DC Reference
