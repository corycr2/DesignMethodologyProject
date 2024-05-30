import pigpio
import rgb1602

#This creates the interface to talk to the digital potentiometer
pi = pigpio.pi()

#LCD setup
lcd=rgb1602.RGB1602(16,2)

#Begin DC Reference function
def dc(voltage):
    #Tell the user what they are in
    lcd.clear()
    lcd.setCursor(0, 0)                                     
    lcd.printout(f"Voltage: ")
    lcd.setCursor(0, 1)                                     
    lcd.printout(f"{voltage} +/- .25v ")
    
    #Using PWM from the raspberry pi, generate PWM waves that create voltages. These voltages go to an noninverting op amp to amplify the maximum
    #3.3v to a maximum of just over 4v. Using values that were determined to produce certain voltages use user input to determine the output.
    if (voltage == 4):
        pi.hardware_PWM(12,10000, 97*10000)
    elif (voltage == 3.75):
        pi.hardware_PWM(12,10000, 91*10000)
    elif (voltage == 3.5):
        pi.hardware_PWM(12,10000, 85*10000)
    elif (voltage == 3.25):
        pi.hardware_PWM(12,10000, 79*10000)
    elif (voltage == 3):
        pi.hardware_PWM(12,10000, 73*10000)
    elif (voltage == 2.75):
        pi.hardware_PWM(12,10000, 67*10000)
    elif (voltage == 2.5):
        pi.hardware_PWM(12,10000, 61*10000)
    elif (voltage == 2.25):
        pi.hardware_PWM(12,10000, 55*10000)
    elif (voltage == 2):
        pi.hardware_PWM(12,10000, 49*10000)
    elif (voltage == 1.75):
        pi.hardware_PWM(12,10000, 43*10000)
    elif (voltage == 1.5):
        pi.hardware_PWM(12,10000, 37*10000)
    elif (voltage == 1.25):
        pi.hardware_PWM(12,10000, 31*10000)
    elif (voltage == 1):
        pi.hardware_PWM(12,10000, 25*10000)
    elif (voltage == 0.75):
        pi.hardware_PWM(12,10000, 19*10000)
    elif (voltage == 0.5):
        pi.hardware_PWM(12,10000, 13*10000)
    elif (voltage == 0.25):
        pi.hardware_PWM(12,10000, 7*10000)
    elif (voltage == 0):
        pi.hardware_PWM(12,10000, 0*10000)
    
    #If somehow a value that was not in the lists above set the voltage to 0
    else:
        pi.hardware_PWM(12,10000, 0*10000)
#End DC Reference function
    
