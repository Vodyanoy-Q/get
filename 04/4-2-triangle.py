import RPi.GPIO as GPIO
import time as time
def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

dac = [8,11,7,1,0,5,12,6]

GPIO.setup(dac, GPIO.OUT)



try:
    time1 = float(input("Enter a number: "))
    while True:
        for i in range(0, 255):
            GPIO.output(dac, dec2bin(i))
            time.sleep(time1/512)
            print(i)
        for i in range(0, 255):
            GPIO.output(dac, dec2bin(255 - i))
            time.sleep(time1/512)
            print(255 - i)
            
except Exception:
    print("Enter num")

finally:
    GPIO.setup(dac, 0)
    GPIO.cleanup()