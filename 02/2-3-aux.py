import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

leds = [2,3,4,17,27,22,10,9]
aux = [21,20,26,16,19,25,23,24]
aux_mode = [1,1,1,1,1,1,1,1]

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(aux, GPIO.IN)

while True:
    aux_mode = [GPIO.input(21), GPIO.input(20), GPIO.input(26), GPIO.input(16), GPIO.input(19), GPIO.input(25), GPIO.input(23), GPIO.input(24)]
    GPIO.output(leds, aux_mode)



GPIO.cleanup()