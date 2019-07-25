# -*- coding: utf-8 -*-
#!/usr/bin/env python
#######################################################################
#####                                                             #####
#####                     Jeferson S. Pazze                       #####
#####                jeferson.pazze@acad.pucrs.br                 #####
#####                       09/24/2018                            #####
#####                      LABIO - PUCRS                          #####
#####              Real-time "Color Calibrator"                   #####
#####                                                             #####
#######################################################################

# import the necessary packages

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import os
import pygame
import sys
import itertools as it
from contextlib import contextmanager
import numpy as np
import cv2 as cv
import cv2
import tkinter as tk
import RPi.GPIO as gpio
import matplotlib.pyplot as plt

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)

############################ Controller ##############################
cal = 0
pwm = 0
graph = 0
window = 1

def nothing(x):
    pass
 
cv2.namedWindow("Trackbars")
cv2.createTrackbar("L - H", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U - H", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)

#Configuring don’t show warnings 
gpio.setwarnings(False)

#Configuring GPIO
gpio.setmode(gpio.BOARD)
gpio.setup(38,gpio.OUT)
gpio.setup(36,gpio.OUT)
gpio.setup(40,gpio.OUT)

LDR_1 = 7
LDR_2 = 11
LDR_3 = 13

#Configure the pwm objects and initialize its value
pwm36 = gpio.PWM(36,100)
pwm36.start(100)
time.sleep(1)

pwm38 = gpio.PWM(38,100)
pwm38.start(0)
time.sleep(1)

pwm40 = gpio.PWM(40,100)
pwm40.start(0)
time.sleep(1)


pwm38.start(100)
time.sleep(1)

pwm40.start(100)
time.sleep(1)

#Create the dutycycle variables
dc36 = 0
dc38 = 0
dc40 = 0

pygame.mixer.init()
pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/calibrador_ini.mp3")
pygame.mixer.music.play()
print('inicialized')

#######################  LDR 1  ################################
def ldr_1(LDR_1):
    count = 0
  
    #Output on the pin for 
    gpio.setup(LDR_1, gpio.OUT)
    gpio.output(LDR_1, gpio.LOW)
    time.sleep(0.01)

    #Change the pin back to input
    gpio.setup(LDR_1, gpio.IN)

    while (gpio.input(LDR_1) == gpio.LOW):
        
        count += 1
        
    return count

#######################  LDR 2  ################################
def ldr_2(LDR_2):
    
    count = 0
  
    #Output on the pin for 
    gpio.setup(LDR_2, gpio.OUT)
    gpio.output(LDR_2, gpio.LOW)
    time.sleep(0.001)

    #Change the pin back to input
    gpio.setup(LDR_2, gpio.IN)

    while (gpio.input(LDR_2) == gpio.LOW):
        
        count += 1
        
    return count

#######################  LDR 3  ################################
def ldr_3(LDR_3):
    count = 0
  
    #Output on the pin for 
    gpio.setup(LDR_3, gpio.OUT)
    gpio.output(LDR_3, gpio.LOW)
    time.sleep(0.001)

    #Change the pin back to input
    gpio.setup(LDR_3, gpio.IN)

    while (gpio.input(LDR_3) == gpio.LOW):
        
        count += 1

    return count

#######################  LDR  ################################

LDR1 = []
LDR2 = []
LDR3 = []

MED  = []

#######################  MMA  ################################

def med(MED):
    
    n = 9
    soma = []
    somatorio = 0
    MMA = 0 
    
    for i in range(0, n):
        
        soma.append(ldr_1(LDR_1))
        time.sleep(0.0001)
        
    #print ('soma: ',soma)
    somatorio = (sum(soma))
    #print ('soma todos ele: ',somatorio)
    MMA = (somatorio / len(soma))
    #print ('MMA: ',int(MMA))

    #time.sleep(0.004)

    return int(MMA)

#######################  MMA  ################################

def plotNow():
    plt.clf()
    plt.ylim(0,3000)
    plt.title('LDR Sensor')
    plt.grid(True) 
    plt.ylabel('Value')
    plt.xlabel('Time(ms)')
    plt.plot(LDR1, 'r-', label='LDR_1')
    plt.plot(LDR2, 'b-', label='LDR_2')
    plt.plot(LDR3, 'y-', label='LDR_3')
    plt.plot(MED, 'g-', label='MMA_9')
    plt.legend(loc='upper right')
    plt.pause(0.01)
    plt.show()

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	
	image = frame.array
	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

	cal = ldr_1(LDR_1)/1000

	#print(cal)
	#print(int(cal))

	l_h = cv2.getTrackbarPos("L - H", "Trackbars")
	l_s = cv2.getTrackbarPos("L - S", "Trackbars")
	l_v = cv2.getTrackbarPos("L - V", "Trackbars")
	u_h = cv2.getTrackbarPos("U - H", "Trackbars")
	u_s = cv2.getTrackbarPos("U - S", "Trackbars")
	u_v = cv2.getTrackbarPos("U - V", "Trackbars")

	#lower_blue = np.array([l_h, l_s, l_v*int(cal)+1])
	lower_blue = np.array([l_h, l_s, l_v])
	upper_blue = np.array([u_h, u_s, u_v])
 
	#lower_blue = np.array([l_h, l_s, l_v*int(cal)+1])
	#upper_blue = np.array([u_h, u_s, u_v])
	mask = cv2.inRange(hsv, lower_blue, upper_blue)
	result = cv2.bitwise_and(image, image, mask=mask)

	#print ('MMA_1: ',med(MED))

	if pwm == 1 :
            
		'''
		if med(MED) > 2500:
			pwm38.ChangeDutyCycle(0)
			#print('Intensidade 100')

		elif med(MED) < 2500 and med(MED) > 2000:
			pwm38.ChangeDutyCycle(30)
			#print('Intensidade 70')

		elif med(MED) < 2000 and med(MED) > 1500:
			pwm38.ChangeDutyCycle(60)
			#print('Intensidade 40')

		elif med(MED) < 1500 and med(MED) > 1000:
			pwm38.ChangeDutyCycle(90)
			#print('Intensidade 10')

		elif med(MED) < 1000 and med(MED) > 0:
			pwm38.ChangeDutyCycle(100)
			#print('Intensidade 0')
		'''
		
		if ldr_1(LDR_1) > 2500:
			pwm38.ChangeDutyCycle(0)
			print('Intensidade 100')

		elif ldr_1(LDR_1) < 2500 and ldr_1(LDR_1) > 2000:
			pwm38.ChangeDutyCycle(30)
			print('Intensidade 70')

		elif ldr_1(LDR_1) < 2000 and ldr_1(LDR_1) > 1500:
			pwm38.ChangeDutyCycle(60)
			print('Intensidade 40')

		elif ldr_1(LDR_1) < 1500 and ldr_1(LDR_1) > 1000:
			pwm38.ChangeDutyCycle(90)
			print('Intensidade 10')

		elif ldr_1(LDR_1) < 1000 and ldr_1(LDR_1) > 0:
			pwm38.ChangeDutyCycle(100)
			print('Intensidade 0')
		

	if graph == 1:
            
		plt.ion()
	
		osvalue = os.popen('vcgencmd measure_value').readline()
		value = (osvalue.replace("value=", "").replace("'C\n", ""))
	
		LDR1.append(ldr_1(LDR_1))
		#LDR2.append(ldr_2(LDR_2))
		#LDR3.append(ldr_3(LDR_3))
		MED.append(med(MED))
	
		plotNow()

	#cv2.putText(image, "LDR_1: "+str(ldr_1(LDR_1)),(10,30),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),1)
	#cv2.putText(image, "LDR_2: "+str(ldr_2(LDR_2)),(10,60),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),1)
	#cv2.putText(image, "LDR_3: "+str(ldr_3(LDR_3)),(10,90),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),1)

	#cv2.putText(image, "Fator multiplicador: "+str(cal),(10,120),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),1)

	#cv2.putText(image, "LDR_1 compensado: " +str(l_v*int(cal)),(140,60),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),1)
	#cv2.putText(image, "LDR_1 REAL: " +str(l_v),(140,30),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),1)
	#cv2.putText(image, "MMA LDR_1: " +str(med(MED)),(140,90),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),1)

	if window == 1:
            
		cv2.imshow('Real image', image)
		cv2.imshow("mask", mask)
		cv2.imshow("result", result)

	key = cv2.waitKey(1) & 0xFF
	
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
	
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		gpio.cleanup()
		exit()

	if key == ord("t"):
		print('ldr_1 : ' , ldr_1(LDR_1))
		print('ldr_2 : ' , ldr_2(LDR_2))
		print('ldr_3 : ' , ldr_3(LDR_3))
		print('MMA LDR_1 : ' , med(MED))
		print('\n')

	if key == ord("1"):
		print('DC 38 ON')
		pwm38.ChangeDutyCycle(dc38)
		dc38 = 0

	if key == ord("2"):
		print('DC 38 OFF')
		pwm38.start(dc38)
		dc38 = 100

	if key == ord("3"):
		print('DC 40 ON')
		pwm40.start(dc40)
		dc40 = 0

	if key == ord("4"):
		print('DC 40 OFF')
		pwm40.start(dc40)
		dc40 = 100





















	
