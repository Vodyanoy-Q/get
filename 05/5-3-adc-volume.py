import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    val = 0
    for i in range(8):
        val += 2**(7-i)
        out_val = dec2bin(val)
        GPIO.output(dac, out_val)
        comp_val = GPIO.input(comp)
        time.sleep(0.01)
        if comp_val == 0:
            val -= 2**(7-i)
        
    return val

def LEDS(val):
    val = int(val/52*8)

    out_val = [0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(val):
        out_val[7-i] = 1
    
    return out_val

try:
    while True:
        val = adc()
        if val != 0:
            leds_out = LEDS(val)
            GPIO.output(leds, leds_out)
            print(f"Percent = {val/52*100} | Voltage = {val*3.3/256} | Number = {val}")

finally:
    GPIO.setup(dac, 0)
    GPIO.cleanup()