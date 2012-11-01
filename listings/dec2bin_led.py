import sys
import RPi.GPIO as GPIO

# GPIO pins 
pins = [18,23]

def setup_gpio():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

if __name__=='__main__':

    if len(sys.argv) == 1:
        print 'Usage: dec2bin_led.py <decimal integer>'
        sys.exit()

    dec = int(sys.argv[1])
    if dec < 0 or dec > 2**len(pins)-1:
        print 'Please enter a decimal integer between 0 and %s (both inclusive)' \
            % str(2**len(pins)-1)
        sys.exit()

    binary = bin(dec).lstrip('0b')

    setup_gpio()

    for i,bit in enumerate(binary):
        if bit=='1':
            GPIO.output(pins[i], GPIO.HIGH)
        else:
            GPIO.output(pins[i], GPIO.LOW)
