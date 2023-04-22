import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

p1=GPIO.PWM(5,20)
p2=GPIO.PWM(23,20)

p1.start(30)
p2.start(10)
time.sleep(10)

p1.start(15)
p2.start(15)
time.sleep(2)

p1.start(10)
p2.start(30)
time.sleep(10)

#while True:
    #p.start(20) #Motor will run at slow speed
    #GPIO.output(23,True)
    #GPIO.output(6,False)
    #GPIO.output(5,True)
    #time.sleep(3)
    #p.ChangeDutyCycle(100) #Motor will run at High speed
    #GPIO.output(23,True)
    #GPIO.output(6,False)
    #GPIO.output(5,True)
    #time.sleep(3)
    #GPIO.output(5,False)
    #p.stop()

p1.stop()
p2.stop()
GPIO.cleanup()
