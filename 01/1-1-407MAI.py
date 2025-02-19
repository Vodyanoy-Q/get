import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.OUT)

GPIO.output(21, 1)

time.sleep(1)

GPIO.output(21, 0)

GPIO.output(21, 1)

time.sleep(1)

for i in range(10):
    
    GPIO.output(21, 1)
    time.sleep(1)
    GPIO.output(21, 0)
    time.sleep(1)