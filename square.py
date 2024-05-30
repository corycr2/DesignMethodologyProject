#This is for our square wave. This code simple turns on our PWM pin from our raspberry pi. This PWM signal runs through an inverting op amp with a gain and offset to 
#create the desired +/-5v square wave.
import pigpio

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)

#Set square wave to on
def square_function_on(frequency):
    #Set up GPIO pin at the given frequency
    pwm = GPIO.PWM(13, frequency) # 1 kHz frequency
    pwm.start(50)
        
