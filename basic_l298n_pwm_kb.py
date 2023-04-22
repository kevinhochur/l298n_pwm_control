# File: basic_l298n_pwm_kb.py
# Project: Actka (COMPS456F)
# Date: 04 Dec 2022
# Programmer: Kevin Li
# Purpose: To control the robotic car by arrow keys

import RPi.GPIO as GPIO
import time
import pygame
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

# Set the rotational frequency by PWM 
motor1_positive=GPIO.PWM(5, 10) 
motor1_negative=GPIO.PWM(6, 10)
motor2_positive=GPIO.PWM(23, 10)
motor2_negative=GPIO.PWM(24, 10)

go_rotation_speed = 90
turn_rotation_speed = 100

def goForward():
    motor1_positive.start(go_rotation_speed)
    motor2_positive.start(go_rotation_speed)
    
def goBack():
    motor1_negative.start(go_rotation_speed)
    motor2_negative.start(go_rotation_speed)
    
def turnLeft():
    motor1_positive.start(turn_rotation_speed)
    motor2_negative.start(turn_rotation_speed)
    
def turnRight():
    motor1_negative.start(turn_rotation_speed)
    motor2_positive.start(turn_rotation_speed)
    
def fullyStop():
    motor1_positive.stop()
    motor1_negative.stop()
    motor2_positive.stop()
    motor2_negative.stop()

pygame.init()
display = pygame.display.set_mode((900, 900))

while True:
       
    # Creating a loop to check events that are occurring
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         
        if event.type == pygame.KEYDOWN: # If a key is pressed
            if event.key == pygame.K_UP: # If the key being pressed is UP
            	goForward()
            	#print("Going Forward") 
            if event.key == pygame.K_DOWN: # If the key being pressed is DOWN
                goBack()
                #print("Going Back")
            if event.key == pygame.K_LEFT: # If the key being pressed is LEFT
                turnLeft()
                #print("Turing Left")
            if event.key == pygame.K_RIGHT: # If the key being pressed is RIGHT
                turnRight()
                #print("Turing Right")
        if event.type == pygame.KEYUP: # IF no key is pressed
            	fullyStop()
            	#print("Motors Stopped")
