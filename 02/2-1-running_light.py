import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)

for i in range(3):
    GPIO.output(2, 1)
    time.sleep(0.2)
    GPIO.output(2, 0)

    GPIO.output(3, 1)
    time.sleep(0.2)
    GPIO.output(3, 0)

    GPIO.output(4, 1)
    time.sleep(0.2)
    GPIO.output(4, 0)

    GPIO.output(17, 1)
    time.sleep(0.2)
    GPIO.output(17, 0)

    GPIO.output(27, 1)
    time.sleep(0.2)
    GPIO.output(27, 0)

    GPIO.output(22, 1)
    time.sleep(0.2)
    GPIO.output(22, 0)

    GPIO.output(10, 1)
    time.sleep(0.2)
    GPIO.output(10, 0)

    GPIO.output(9, 1)
    time.sleep(0.2)
    GPIO.output(9, 0)

GPIO.cleanup()