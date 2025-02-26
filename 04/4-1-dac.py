import RPi.GPIO as GPIO

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

dac = [8,11,7,1,0,5,12,6]

GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        num = input("Enter a number: ")
        try:
            if num.isalpha() and num != "q":
                print("Please enter num")
                continue
            num = float(num)
            if int(num) != float(num):
                print("Don't enter float")
                continue
            num = int(num)
            if 0 <= num <= 255:
                GPIO.output(dac, dec2bin(num))
                volt = float(num) / 256 * 3.3
                print(f"Output volt = {volt:.4}")
            elif int(num) < 0:
                    print("Please enter positive number.")
            elif int(num) > 255:
                    print("Enter number in range: [0, 255]")

        except Exception:
            if num == "q":
                break

finally:
    GPIO.setup(dac, 0)
    GPIO.cleanup()
