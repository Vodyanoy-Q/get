import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.IN)

GPIO.setup(21, GPIO.OUT)

status = GPIO.input(24)

print(status)

GPIO.output(21, status)