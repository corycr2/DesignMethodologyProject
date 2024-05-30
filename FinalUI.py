#This is our main file. This file is responsible for the user interface. The user interface allows for the user to interact with all the other files.
#By using a rotary encoder and a 16x2 LCD screen the user can scroll through and select desired options. The list of possible options is located
#in the option list of list. The embedded list contain their own options to keep the user interface as simple as possible.

import sys
sys.path.append('../')
import rgb1602
import RPi.GPIO as GPIO
import time
import ohmmeter
import adc
import input_frequency
import LCD
import pigpio
import DC_Reference
import FrequencyRead
import sine

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
lcd=rgb1602.RGB1602(16,2)
pi = pigpio.pi()

#Initialize variables to be used
sineIs = False
squareIs = True
amplitude = 2.5
frequency = 5000
voltage = 0

# Define the UI options
options = {
    "main": ["Off_main", "Mode Select", "LCD Color"],
    "mode_select": ["Function gen", "Ohm Meter", "Voltmeter", "DC Reference", "measureFrequency", "Back", "Main"],
    "function_gen": ["Type", "Frequency", "Amplitude", "Output", "Back", "Main"],
    "type": ["Sine", "Square", "Back", "Main"],
    "frequency": ["Input Frequency", "Back", "Main"],
    "amplitude": ["Input Amplitude", "Back", "Main"],
    "output": ["On", "Off_function", "Back", "Main"],
    "output_dc": ["On", "Off_dc", "Back", "Main"],
    "ohm_meter": ["Display Reading", "Back", "Main"],
    "voltmeter": ["External", "Internal Reference", "Back", "Main"],
    "dc_reference": ["Voltage Value Input", "Output", "Back", "Main"],
    "MeasureFrequency": ["External", "Internal", "Back", "Main"],
    "LCD color": ["Change color", "Back", "Main"]
}

# Initialize the current UI level to "main"
current_level = "main"
current_option = "Off_main"

# Infinite loop for the UI
while True:
    # Get the rotary encoder state
    clk_state = GPIO.input(encoder.clk)
    dt_state = GPIO.input(encoder.dt)
    sw_state = GPIO.input(encoder.sw)

    # Handle the rotary encoder rotation
    if clk_state != dt_state:
        lcd.clear()
        if clk_state == 0:
            # Rotate clockwise
            current_option_index = options[current_level].index(current_option)
            current_option_index = (current_option_index + 1) % len(options[current_level])
            current_option = options[current_level][current_option_index]
            time.sleep(.13)
        else:
            # Rotate counterclockwise
            current_option_index = options[current_level].index(current_option)
            current_option_index = (current_option_index - 1) % len(options[current_level])
            current_option = options[current_level][current_option_index]
            time.sleep(.13)

    # Handle the rotary encoder button press
    if sw_state == 0:
        time.sleep(1)
        lcd.clear()
        # Get the selected option
        selected_option = options[current_level][current_option_index]

        # Handle the "Off" option
        if selected_option == "Off_main":
            # Exit the program
            exit()

        # Handle the "Mode Select" option
        elif selected_option == "Mode Select":
            # Go to the "mode_select" level
            current_level = "mode_select"
            current_option = options[current_level][0]
            current_option_index = options[current_level].index(current_option)
        
        elif selected_option == "LCD Color":
            # Go to the "LCD" level
            current_level = "LCD color"
            current_option = options[current_level][0]
            current_option_index = options[current_level].index(current_option)

            
        # Handle the other options
        elif current_level == "mode_select":
            if selected_option == "Function gen":
                current_level = "function_gen"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)
            elif selected_option == "Ohm Meter":
                current_level = "ohm_meter"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)
            elif selected_option == "Voltmeter":
                current_level = "voltmeter"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)
            elif selected_option == "DC Reference":
                current_level = "dc_reference"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)
            elif selected_option == "measureFrequency":
                current_level = "MeasureFrequency"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)
            elif selected_option == "Back":
                #Go back one level
                current_level = "main"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)
            elif selected_option == "Main":
                #Go to the "main" level
                current_level = "main"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)

        elif current_level == "function_gen":
            if selected_option == "Type":
                current_level = "type"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)
            elif selected_option == "Frequency":
                current_level = "frequency"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)
            elif selected_option == "Amplitude":
                current_level = "amplitude"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)
            elif selected_option == "Output":
                current_level = "output"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)
            elif selected_option == "Back":
                current_level = "mode_select"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)
            elif selected_option == "Main":
                current_level = "main"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)

        elif current_level == "type":
            if selected_option == "Sine":
                #Handle the "Sine" option
                squareIs = False
                sineIs = True
                current_level = "type"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)

            elif selected_option == "Square":
                #Handle the "Square" option
                squareIs = True
                sineIs = False
                current_level = "type"
                current_option = options[current_level][1]
                current_option_index = options[current_level].index(current_option)

            elif selected_option == "Back":
                current_level = "function_gen"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)
            elif selected_option == "Main":
                current_level = "main"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)

        # Handle the other levels and options similarly
        elif current_level == "frequency":
            if selected_option == "Input Frequency":
                #Handle the "Input Frequency" option
                frequency = input_frequency.input_frequency1(frequency)
                lcd.clear()
                lcd.setCursor(0, 0)         
                lcd.printout(f"Frequency is:")
                lcd.setCursor(0, 1)
                lcd.printout(f"{frequency} Hz")
                time.sleep(2)
                lcd.clear()
                current_level = "frequency"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)

            elif selected_option == "Back":
                current_level = "function_gen"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)
            elif selected_option == "Main":
                current_level = "main"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)
        
        
        elif current_level == "amplitude":
            if selected_option == "Input Amplitude":
                # Handle the "Input amplitude" option
                amplitude = input_frequency.input_amplitude(amplitude)
                lcd.clear()
                lcd.setCursor(0, 0)         
                lcd.printout(f"Amplitude is:")
                lcd.setCursor(0, 1)
                lcd.printout(f"{amplitude} v")
                time.sleep(2)
                lcd.clear()
                current_level = "amplitude"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)

            elif selected_option == "Back":
                current_level = "function_gen"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)
            elif selected_option == "Main":
                current_level = "main"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)

        elif current_level == "output":
            if selected_option == "On":
                #Handle the "On" option
                #Check to see what mode is set
                if squareIs == True:
                    pi = pigpio.pi()
                    pi.hardware_PWM(19, frequency, 500000)
                else:
                    sine.sine(frequency, amplitude)
                lcd.clear()
                lcd.setCursor(0, 0)         
                lcd.printout(f"Selected is:")
                lcd.setCursor(0, 1)
                lcd.printout(f"on")
                time.sleep(1)
                #Read frequency automatically
                FrequencyRead.read()
                lcd.clear()
                

                current_level = "output"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)

            elif selected_option == "Off_function":
                #Handle the "Off" option               
                 if squareIs == True:
                    pi = pigpio.pi()
                    pi.hardware_PWM(19, 10000, 0)
                else:
                    sine.sineOff()
                lcd.clear()
                
                #Report back to the user that the system was turned off
                lcd.setCursor(0, 0)         
                lcd.printout(f"Selected is:")
                lcd.setCursor(0, 1)
                lcd.printout(f"off")
                time.sleep(2)
                lcd.clear()
                current_level = "output"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)

            elif selected_option == "Back":
                #Auto "Off" option           
                if squareIs == True:
                    pi = pigpio.pi()
                    pi.hardware_PWM(19, 10000, 0)
                else:
                    sine.sineOff()
                current_level = "function_gen"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)
            elif selected_option == "Main":
                #Auto "Off" option               
                if squareIs == True:
                    pi = pigpio.pi()
                    pi.hardware_PWM(19, 10000, 0)
                else:
                    sine.sineOff()
                current_level = "main"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)
        #end of Function Generator

        elif current_level == "ohm_meter":
            if selected_option == "Display Reading":
                current_level = "ohm_meter"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)
                ohmmeter.ohm()
                time.sleep(2)
                lcd.clear()
            elif selected_option == "Back":
                current_level = "mode_select"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)
            elif selected_option == "Main":
                current_level = "main"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)
        #end of ohmmeter

        elif current_level == "voltmeter":
            if selected_option == "External":
                #Handle the "External" option
                current_level = "voltmeter"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)
                adc.ADC()
                time.sleep(2)
                lcd.clear()
            elif selected_option == "Internal Reference":
                current_level = "dc_reference"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)
            elif selected_option == "Back":
                current_level = "mode_select"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)
            elif selected_option == "Main":
                current_level = "main"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)
            

        elif current_level == "dc_reference":
            if selected_option == "Voltage Value Input":
                #DC Reference
                voltage = input_frequency.DC_Reference1(voltage)
                lcd.clear()
                lcd.setCursor(0, 0)         
                lcd.printout(f"Voltage is:")
                lcd.setCursor(0, 1)
                lcd.printout(f"{voltage} v")
                time.sleep(2)
                lcd.clear()
                current_level = "dc_reference"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)
                pass
            elif selected_option == "Output":
                current_level = "output_dc"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)
            elif selected_option == "Back":
                current_level = "mode_select"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)
            elif selected_option == "Main":
                current_level = "main"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)

        elif current_level == "output_dc":
            if selected_option == "On":
                #Handle the "On_dc" option
                DC_Reference.dc(voltage)
                time.sleep(2)
                lcd.clear()
                current_level = "output_dc"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)
            elif selected_option == "Off_dc":
                #Handle the "Off_dc" option
                DC_Reference.dc(0)
                lcd.clear()
                current_level = "output_dc"
                current_option = options[current_level][1]
                current_option_index = options[current_level].index(current_option)
            elif selected_option == "Back":
                #Auto off
                DC_Reference.dc(0)
                current_level = "dc_reference"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)
            elif selected_option == "Main":
                #Auto off
                DC_Reference.dc(0)
                current_level = "main"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)
        #end of DC Reference

        elif current_level == "MeasureFrequency":
            if selected_option == "External":
                FrequencyRead.read()
                lcd.clear()
                current_level = "MeasureFrequency"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)
                pass
            elif selected_option == "Internal":
                current_level = "function_gen"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)
            elif selected_option == "Back":
                current_level = "mode_select"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)
            elif selected_option == "Main":
                current_level = "main"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)
        
        elif current_level == "LCD color":
            if selected_option == "Change color":
                # Handle the "Change color" option
                current_level = "LCD color"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)
                LCD.LCD_Color()

            elif selected_option == "Back":
                current_level = "main"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)
            elif selected_option == "Main":
                current_level = "main"
                current_option = options[current_level][0]
                current_option_index = options[current_level].index(current_option)

    # Draw the current option on the display
    lcd.setCursor(0,0)
    lcd.printout(current_level)
    lcd.setCursor(0,1)
    lcd.printout(current_option)

GPIO.cleanup()
