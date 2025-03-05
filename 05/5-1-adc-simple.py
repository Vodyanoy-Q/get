import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    for i in range(256):
        out_val = dec2bin(i)
        GPIO.output(dac, out_val)
        comp_val = GPIO.input(comp)
        time.sleep(0.01)

        if comp_val == 0:
            return i

    return 0
try:
    while True:
        val = adc()
        print(f"Number = {val} | Voltage = {val*3.3/256}")

finally:
    GPIO.setup(dac, 0)
    GPIO.cleanup()
