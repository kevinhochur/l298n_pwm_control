import RPi.GPIO as GPIO
from time import sleep

# Pins for Motor Driver Inputs 
Motor1A = 5
Motor1B = 6
Motor1E = 23
Motor1F = 24
 
def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)              # GPIO Numbering
    GPIO.setup(Motor1A,GPIO.OUT)  # All pins as Outputs
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor1E,GPIO.OUT)
    GPIO.setup(Motor1F,GPIO.OUT) 

def loop():
    # Going forwards
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)
    GPIO.output(Motor1F,GPIO.LOW)
    print("Going forwards")
    sleep(1)

    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.LOW)
    sleep(3)

    # Going backwards
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.LOW)
    GPIO.output(Motor1F,GPIO.HIGH)
    print("Going backwards")
    sleep(1)
    
    # Stop
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1F,GPIO.LOW)
    print("Stop")

def destroy():  
    GPIO.cleanup()

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
