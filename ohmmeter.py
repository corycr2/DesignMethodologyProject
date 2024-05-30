#This function is designed for a wheatstone/digipot comparator circuit. By knowing the voltage and resistors on one side of a wheatstone bridge
#this can compare to another side wheat stone bridge to determine resistance of the resistor. By having the unknown resistor in series with a know variable
#resistor it is possible to compare a voltage across them and our other side of the wheatstone bridge. This function below goes through a list of possible
#resistances until coming to a voltage that makes each side of the bridge match or until it runs out of options meaning it is outside of the scope of 
#our project.
import rgb1602
import RPi.GPIO as GPIO
import time
import pigpio

#This creates the interface to talk to the digital potentiometer
pi1 = pigpio.pi()
h = pi1.spi_open(0,97600)

ohm = 5
GPIO.setmode(GPIO.BCM) 
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP) #ohm

#LCD setup
lcd=rgb1602.RGB1602(16,2)

#This function is our charaterization of our digipot the first number is the voltage divider in the wheatstone bridge to allow our digipot that does 
#not reach 10k ohms to still be able to match the voltage output needed with a 10k ohm resistor. The second number is the measured digipot value at 
#the step(value). The last number is the calibration value to match them to the correct values. In hindsight this should have been a simple table.
def digipot_table(value):
    if value == 0:                      #Anything less than 117 ohms
        resistance = 1.3459 * 87 * .996
        return resistance
    elif value == 1:
        resistance = 1.3459 * 158 * .996
        return resistance
    elif value == 2:
        resistance = 1.3459 * 230 * .996
        return resistance
    elif value == 3:
        resistance = 1.3459 * 300 * .996
        return resistance
    elif value == 4:                    #500 ohms
        resistance = 1.3459 * 375 * .996
        return resistance
    elif value == 5:
        resistance = 1.3459 * 450 *.933
        return resistance
    elif value == 6:
        resistance = 1.3459 * 510 *.933
        return resistance
    elif value == 7:
        resistance = 1.3459 * 580 *.933
        return resistance
    elif value == 8:
        resistance = 1.3459 * 650 *.933
        return resistance
    elif value == 9:
        resistance = 1.3459 * 725 *.933
        return resistance
    elif value == 10:                   #1000 ohms
        resistance = 1.3459 * 800 *.933
        return resistance
    elif value == 11:
        resistance = 1.3459 * 860 *.971
        return resistance
    elif value == 12:
        resistance = 1.3459 * 940 *.971
        return resistance
    elif value == 13:
        resistance = 1.3459 * 1000 *.971
        return resistance
    elif value == 14:
        resistance = 1.3459 * 1075 *.971
        return resistance
    elif value == 15:                   #1500 ohms
        resistance = 1.3459 * 1150 *.971
        return resistance
    elif value == 16:
        resistance = 1.3459 * 1220 *.991
        return resistance
    elif value == 17:
        resistance = 1.3459 * 1300 *.991
        return resistance
    elif value == 18:
        resistance = 1.3459 * 1360 *.991
        return resistance
    elif value == 19:
        resistance = 1.3459 * 1430 *.991
        return resistance
    elif value == 20:                   #2000 ohms
        resistance = 1.3459 * 1500 *.991
        return resistance
    elif value == 21:
        resistance = 1.3459 * 1575 *.966
        return resistance
    elif value == 22:
        resistance = 1.3459 * 1640 *.966
        return resistance
    elif value == 23:
        resistance = 1.3459 * 1710 *.966
        return resistance
    elif value == 24:
        resistance = 1.3459 * 1775 *.966
        return resistance
    elif value == 25:
        resistance = 1.3459 * 1850 *.966
        return resistance
    elif value == 26:                   #2500 ohms
        resistance = 1.3459 * 1920 *.987
        return resistance
    elif value == 27:
        resistance = 1.3459 * 1985 *.987
        return resistance
    elif value == 28:
        resistance = 1.3459 * 2050 *.987
        return resistance
    elif value == 29:
        resistance = 1.3459 * 2125 *.987
        return resistance
    elif value == 30:
        resistance = 1.3459 * 2200 *.987
        return resistance
    elif value == 31:                   #3000 ohms
        resistance = 1.3459 * 2260 *.987
        return resistance
    elif value == 32:
        resistance = 1.3459 * 2320 *.972
        return resistance
    elif value == 33:
        resistance = 1.3459 * 2400 *.972
        return resistance
    elif value == 34:
        resistance = 1.3459 * 2470 *.972
        return resistance
    elif value == 35:
        resistance = 1.3459 * 2535 *.972
        return resistance
    elif value == 36:                   
        resistance = 1.3459 * 2590 *.972
        return resistance
    elif value == 37:                   #3500 ohms
        resistance = 1.3459 * 2675 *.972
        return resistance
    elif value == 38:
        resistance = 1.3459 * 2740 *.983
        return resistance
    elif value == 39:
        resistance = 1.3459 * 2810 *.983
        return resistance
    elif value == 40:
        resistance = 1.3459 * 2860 *.983
        return resistance
    elif value == 41:
        resistance = 1.3459 * 2950 *.983
        return resistance
    elif value == 42:                   #4000 ohms
        resistance = 1.3459 * 3020 *.983
        return resistance
    elif value == 43:
        resistance = 1.3459 * 3080 *.986
        return resistance
    elif value == 44:
        resistance = 1.3459 * 3125 *.986
        return resistance
    elif value == 45:
        resistance = 1.3459 * 3215 *.986
        return resistance
    elif value == 46:
        resistance = 1.3459 * 3290 *.986
        return resistance
    elif value == 47:
        resistance = 1.3459 * 3350 *.986
        return resistance
    elif value == 48:                   #4500 ohms
        resistance = 1.3459 * 3390 *.986
        return resistance
    elif value == 49:
        resistance = 1.3459 * 3480 *.991
        return resistance
    elif value == 50:
        resistance = 1.3459 * 3560 *.991
        return resistance
    elif value == 51:
        resistance = 1.3459 * 3620 *.991
        return resistance
    elif value == 52:
        resistance = 1.3459 * 3650 *.991
        return resistance
    elif value == 53:                   #5000 ohms
        resistance = 1.3459 * 3750 *.991
        return resistance
    elif value == 54:
        resistance = 1.3459 * 3820 *.985
        return resistance
    elif value == 55:
        resistance = 1.3459 * 3890 *.985
        return resistance
    elif value == 56:
        resistance = 1.3459 * 3910 *.985
        return resistance
    elif value == 57:
        resistance = 1.3459 * 4015 *.985
        return resistance
    elif value == 58:
        resistance = 1.3459 * 4090 *.985
        return resistance
    elif value == 59:                   #5500 ohms
        resistance = 1.3459 * 4150 *.985
        return resistance
    elif value == 60:
        resistance = 1.3459 * 4170 *1.00867
        return resistance
    elif value == 61:
        resistance = 1.3459 * 4280 *1.00867
        return resistance
    elif value == 62:
        resistance = 1.3459 * 4360 *1.00867
        return resistance
    elif value == 63:
        resistance = 1.3459 * 4420 *1.00867
        return resistance
    elif value == 64:                   #6000 ohms
        resistance = 1.3459 * 4420 *1.00867
        return resistance
    elif value == 65:
        resistance = 1.3459 * 4540 *.989
        return resistance
    elif value == 66:
        resistance = 1.3459 * 4620 *.989
        return resistance
    elif value == 67:
        resistance = 1.3459 * 4685 *.989
        return resistance
    elif value == 68:
        resistance = 1.3459 * 4675 *.989
        return resistance
    elif value == 69:
        resistance = 1.3459 * 4796 *.989
        return resistance
    elif value == 70:                   #6500 ohms
        resistance = 1.3459 * 4880 *.989
        return resistance
    elif value == 71:
        resistance = 1.3459 * 4945 *.972
        return resistance
    elif value == 72:
        resistance = 1.3459 * 4925 *.972
        return resistance
    elif value == 73:
        resistance = 1.3459 * 5050 *.972
        return resistance
    elif value == 74:
        resistance = 1.3459 * 5235 *.972
        return resistance
    elif value == 75:
        resistance = 1.3459 * 5310 *.972
        return resistance
    elif value == 76:                   #7000 ohms
        resistance = 1.3459 * 5345 *.972
        return resistance
    elif value == 77:
        resistance = 1.3459 * 5420 *.973
        return resistance
    elif value == 78:
        resistance = 1.3459 * 5500 *.973
        return resistance
    elif value == 79:
        resistance = 1.3459 * 5575 *.973
        return resistance
    elif value == 80:
        resistance = 1.3459 * 5610 *.976
        return resistance
    elif value == 81:
        resistance = 1.3459 * 5690 *.976
        return resistance
    elif value == 82:                   #7500 ohms
        resistance = 1.3459 * 5765 *.976
        return resistance
    elif value == 83:
        resistance = 1.3459 * 5840 *.976
        return resistance
    elif value == 84:
        resistance = 1.3459 * 5870 *.976
        return resistance
    elif value == 85:
        resistance = 1.3459 * 5950 *.976
        return resistance
    elif value == 86:
        resistance = 1.3459 * 6030 *.976 
        return resistance
    elif value == 87:
        resistance = 1.3459 * 6100 *.976 
        return resistance
    elif value == 88:                   #8000 ohms
        resistance = 1.3459 * 6130 *.976
        return resistance
    elif value == 89:
        resistance = 1.3459 * 6210 *.976
        return resistance
    elif value == 90:
        resistance = 1.3459 * 6290 *.976
        return resistance
    elif value == 91:
        resistance = 1.3459 * 6370 *.976 
        return resistance
    elif value == 92:
        resistance = 1.3459 * 6390 *.976 
        return resistance
    elif value == 93:                   #8500 ohms
        resistance = 1.3459 * 6470 *.976 
        return resistance
    elif value == 94:
        resistance = 1.3459 * 6550 *.971 
        return resistance
    elif value == 95:
        resistance = 1.3459 * 6630 *.971
        return resistance
    elif value == 96:
        resistance = 1.3459 * 6635 *.971 
        return resistance
    elif value == 97:
        resistance = 1.3459 * 6720 *.971 
        return resistance
    elif value == 98:
        resistance = 1.3459 * 6800 *.971 
        return resistance
    elif value == 99:
        resistance = 1.3459 * 6885 *.971 
        return resistance
    elif value == 100:                   #9000 ohms
        resistance = 1.3459 * 6885 *.971 
        return resistance
    elif value == 101:
        resistance = 1.3459 * 6975 *.966
        return resistance
    elif value == 102:
        resistance = 1.3459 * 7050 *.966 
        return resistance
    elif value == 103:
        resistance = 1.3459 * 7140 *.966 
        return resistance
    elif value == 104:
        resistance = 1.3459 * 7130 *.966
        return resistance
    elif value == 105:
        resistance = 1.3459 * 7220 *.966 
        return resistance
    elif value == 106:                   #9500 ohms
        resistance = 1.3459 * 7300 *.966 
        return resistance
    elif value == 107:
        resistance = 1.3459 * 7390 *.965 
        return resistance
    elif value == 108:
        resistance = 1.3459 * 7375 *.965
        return resistance
    elif value == 109:
        resistance = 1.3459 * 7465 *.965 
        return resistance
    elif value == 110:
        resistance = 1.3459 * 7555 *.965 
        return resistance
    elif value == 111:
        resistance = 1.3459 * 7640 *.965 
        return resistance
    elif value == 112:                  #10000 ohms
        resistance = 1.3459 * 7620 *.965 
        return resistance
    elif value == 113:
        resistance = 1.3459 * 7710 *.965 
        return resistance
    elif value == 114: 
        resistance = 1.3459 * 7800 *.965 
        return resistance
    elif value == 115:
        resistance = 1.3459 * 7890 *.965 
        return resistance
    elif value == 116:
        resistance = 1.3459 * 7860 *.965
        return resistance
    elif value == 117:
        resistance = 1.3459 * 7950 *.965
        return resistance
    elif value == 118:
        resistance = 1.3459 * 8045 *.965 
        return resistance
    elif value == 119:
        resistance = 1.3459 * 8130 *.965 
        return resistance
    elif value == 120:
        resistance = 1.3459 * 8100 *.965 
        return resistance
    elif value == 121:
        resistance = 1.3459 * 8195 *.965 
        return resistance
    elif value == 122:
        resistance = 1.3459 * 8285 *.965 
        return resistance
    elif value == 123:
        resistance = 1.3459 * 8375 *.965 
        return resistance
    elif value == 124:
        resistance = 1.3459 * 8330 *.965 
        return resistance
    elif value == 125:
        resistance = 1.3459 * 8435 *.965 
        return resistance
    elif value == 126:
        resistance = 1.3459 * 8530 *.965 
        return resistance
    elif value == 127:
        resistance = 1.3459 * 8620 *.965 
        return resistance
    elif value == 128:
        resistance = 1.3459 * 8700 *.965 
        return resistance
#End of digipot_table function

#Begin ohm meter function
def ohm():
    #initialize values and digipot to beginning
    value = 1
    pi1.spi_write(h, [0b0000_0000, 0])
    while value != -1:
        if GPIO.input(5) == 1:
            value -= 1
            resistance = int(digipot_table(value))
            lcd.setCursor(0, 0)
            lcd.printout(f"Resistance is: ")   
            lcd.setCursor(0, 1)
            lcd.printout(f"{resistance} +/- 25 ohms")
            pi1.spi_write(h, [0b0000_0000, value])
            value = -1
            time.sleep(1)
        elif value > 128:
            lcd.setCursor(0, 0)
            lcd.printout(f"Resistance is: ")
            lcd.setCursor(0, 1)
            lcd.printout(f" > 12000 ohms")
            value = -1
        else:
            pi1.spi_write(h, [0b0000_0000, value])
            value += 1
#End of ohm meter function


