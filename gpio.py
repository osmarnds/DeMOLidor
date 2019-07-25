# -*- coding: utf-8 -*-
#!/usr/bin/env python

#######################################################################
#####                                                             #####
#####                     Jeferson S. Pazze                       #####
#####                                                             #####
#####                jeferson.pazze@edu.pucrs.br                  #####
#####                                                             #####
#####                       09/06/2019                            #####
#####                                                             #####
#####                      LABIO - PUCRS                          #####
#####                                                             #####
#####                          GPIO                               #####
#####                                                             #####
#######################################################################

import time
import os
import sys
import RPi.GPIO as gpio
import matplotlib.pyplot as plt
import pygame

pygame.mixer.init()

author__ = 'J.PAZZE'

#Configuring don’t show warnings 
gpio.setwarnings(False)

#Configuring GPIO
gpio.setmode(gpio.BOARD)
gpio.setup(38,gpio.OUT)
gpio.setup(36,gpio.OUT)
gpio.setup(40,gpio.OUT)

gpio.setup(37 , gpio.IN)
gpio.setup(35 , gpio.IN)

#Configuring don’t show warnings 
gpio.setwarnings(False)

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

pwm36.start(0)
time.sleep(1)

pwm38.start(100)
time.sleep(1)

pwm40.start(100)
time.sleep(1)

#Create the dutycycle variables
dc36 = 0
dc38 = 0
dc40 = 0

LDR_1 = 7
LDR_2 = 11
LDR_3 = 13

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
    plt.title('LDR Sensor')
    plt.grid(True)
    plt.ylabel('Value')
    plt.xlabel('Time(ms)')
    plt.plot(LDR1, 'r-', label='LDR_1')
    #plt.plot(LDR2, 'b-', label='LDR_2')
    #plt.plot(LDR3, 'y-', label='LDR_3')
    plt.legend(loc='upper right')
    #plt.plot(LDR1)
    plt.pause(0.001)
    plt.show()

    return int(MMA)

#######################  MMA  ################################

plt.ion()

def plotNow():

    plt.figure(2)
    plt.clf()
    plt.ylim(0,10000)
    plt.xlim(0,1000)
    plt.title('LDR Sensor')
    plt.grid(True)
    plt.ylabel('Value')
    plt.xlabel('Time(ms)')
    plt.plot(LDR1, 'r-', label='LDR_1')
    #plt.plot(LDR2, 'b-', label='LDR_2')
    #plt.plot(LDR3, 'y-', label='LDR_3')
    plt.legend(loc='upper right')
    #plt.plot(LDR1)

    plt.figure(1)
    plt.clf()
    plt.ylim(0,10000)
    plt.xlim(0,1000)
    plt.title('xxxx')
    plt.grid(True)
    plt.ylabel('Value')
    plt.xlabel('Time(ms)')
    plt.plot(LDR1, 'b-', label='LDR_1')
    #plt.plot(LDR2, 'b-', label='LDR_2')
    #plt.plot(LDR3, 'y-', label='LDR_3')
    plt.legend(loc='upper right')
    #plt.plot(LDR1)
    plt.pause(0.001)
    plt.show()

def read_botton(botao_1, botao_2):

	if gpio.input(botao_1) == 0:
		
		#time.sleep(1)
		#print("Botao 1 BAIXO")
		print("")

	if gpio.input(botao_1) == 1:
		
		#time.sleep(1)
		print("Botao 1 ALTO")
		#pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/botao_1.mp3")
		#pygame.mixer.music.play()
		print("")
	    
	if gpio.input(botao_2) == 0:
		
		#time.sleep(1)
		#print("Botao 2 BAIXO")
		print("")

	if gpio.input(botao_2) == 1:
		
		#time.sleep(1)
		#pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/botao_2.mp3")
		#pygame.mixer.music.play()
		print("Botao 2 ALTO")
		print("")

	if gpio.input(botao_2) == 1 and gpio.input(botao_1) == 1:
		
		print("Botao 1 e 2 ALTOS")
		#pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/botao_1_2.mp3")
		#pygame.mixer.music.play()
		print("")

	return gpio.input(botao_1), gpio.input(botao_2)

def LED_control(LDR_1):

	intensidade = 0
	
	if ldr_1(LDR_1) > 4000:

		pwm38.ChangeDutyCycle(0)
		pwm40.ChangeDutyCycle(0)
		#print('Intensidade 100')
		intensidade = 100

		
	if ldr_1(LDR_1) > 3400 and ldr_1(LDR_1) < 4000:

		pwm38.ChangeDutyCycle(0)
		pwm40.ChangeDutyCycle(50)
		#print('Intensidade 90')
		intensidade = 90

	elif ldr_1(LDR_1) < 3100 and ldr_1(LDR_1) > 3400:
						
		pwm38.ChangeDutyCycle(20)
		pwm40.ChangeDutyCycle(60)
		#print('Intensidade 80')
		intensidade = 80

	elif ldr_1(LDR_1) < 2800 and ldr_1(LDR_1) > 3100:
						
		pwm38.ChangeDutyCycle(30)
		pwm40.ChangeDutyCycle(70)
		#print('Intensidade 70')
		intensidade = 70

	elif ldr_1(LDR_1) < 2500 and ldr_1(LDR_1) > 2800:
						
		pwm38.ChangeDutyCycle(40)
		pwm40.ChangeDutyCycle(100)
		#print('Intensidade 60')
		intensidade = 60

	elif ldr_1(LDR_1) < 2200 and ldr_1(LDR_1) > 2500:
						
		pwm38.ChangeDutyCycle(50)
		pwm40.ChangeDutyCycle(100)
		#print('Intensidade 50')
		intensidade = 50

	elif ldr_1(LDR_1) < 1900 and ldr_1(LDR_1) > 2200:
						
		pwm38.ChangeDutyCycle(60)
		pwm40.ChangeDutyCycle(100)
		#print('Intensidade 40')
		intensidade = 40

	elif ldr_1(LDR_1) < 1900 and ldr_1(LDR_1) > 1600:
						
		pwm38.ChangeDutyCycle(70)
		pwm40.ChangeDutyCycle(100)
		#print('Intensidade 30')
		intensidade = 30

	elif ldr_1(LDR_1) < 1600 and ldr_1(LDR_1) > 1300:
						
		pwm38.ChangeDutyCycle(80)
		pwm40.ChangeDutyCycle(100)
		#print('Intensidade 20')
		intensidade = 20

	elif ldr_1(LDR_1) < 1300 and ldr_1(LDR_1) > 1000:
	    				
		pwm38.ChangeDutyCycle(90)
		pwm40.ChangeDutyCycle(100)
		#print('Intensidade 10')
		intensidade = 10

	elif ldr_1(LDR_1) < 1000 and ldr_1(LDR_1) > 0:
						
		pwm38.ChangeDutyCycle(100)
		pwm40.ChangeDutyCycle(100)
		#print('Intensidade 0')
		intensidade = 10

	return intensidade

print('gpio inicialized')
