import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.OUT)

led = GPIO.PWM(21,1000)
led.start(0)

try:
    while True:
        n = int(input())
        led.ChangeDutyCycle(n)
        print(3.3 * n / 100)

finally:
    led.stop()
    GPIO.setup(21, 0)
    GPIO.cleanup()