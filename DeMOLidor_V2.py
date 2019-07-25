# -*- coding: utf-8 -*-
#!/usr/bin/env python

#######################################################################
#####                                                             #####
#####                     Jeferson S. Pazze                       #####
#####                                                             #####
#####                jeferson.pazze@edu.pucrs.br                  #####
#####                                                             #####
#####                       05/06/2019                            #####
#####                                                             #####
#####                      LABIO - PUCRS                          #####
#####                                                             #####
#####                      DeM0Lidor V2                           #####
#####                                                             #####
#######################################################################

author__ = 'PAZZE'

import time
import os
import pygame
import sys
import math
import imutils
import argparse
import cv2
import itertools         as it
import numpy             as np
import cv2               as cv
import matplotlib.pyplot as plt
import tkinter           as tk
import RPi.GPIO          as gpio

from picamera.array      import PiRGBArray
from picamera            import PiCamera
from contextlib          import contextmanager
from colors              import *
from control             import *
from gpio                import *
from histogram           import *
from tree                import *
from audio               import *
from interface           import *

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)

botao_1 = 37
botao_2 = 35

#audio_info(1)

#time.sleep(1)

#read_botton(botao_1, botao_2)

#ime.sleep(5)

#botao_1, botao_2 = read_botton(botao_1, botao_2)

#print(" 1 ",botao_1 )
#print(" 2 ",botao_2 )

botton_control(botao_1, botao_2)

frame = []

hsv   = []

lineThickness = 2

amino = 0

cont = 0

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

	img     = []

	img     = frame.array
	
	blurred = cv2.GaussianBlur(img, (5, 5) , 0)

	hsv     = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

	#cv2.imshow("HSV",hsv)
	
	red    = cv2.inRange(hsv, red_lower,    red_upper)
	blue   = cv2.inRange(hsv, blue_lower,   blue_upper)
	yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)
	gray   = cv2.inRange(hsv, lower_gray,   upper_gray)
	green  = cv2.inRange(hsv, lower_green,  upper_green)
	white  = cv2.inRange(hsv, lower_white,  upper_white)
	black  = cv2.inRange(hsv, lower_black,  upper_black)
	
	kernal = np.ones((7,7), "uint16") #Morphological transformation

	res  = cv2.bitwise_and(img, img, mask = red)
	res1 = cv2.bitwise_and(img, img, mask = blue)
	res2 = cv2.bitwise_and(img, img, mask = yellow)
	res3 = cv2.bitwise_and(img, img, mask = gray)
	res4 = cv2.bitwise_and(img, img, mask = white)
	res5 = cv2.bitwise_and(img, img, mask = green)
	res6 = cv2.bitwise_and(img, img, mask = black)
	
	centers=[]
	
	pic_r  = 0
	pic_b  = 0
	pic_y  = 0
	pic_g  = 0
	pic_w  = 0
	pic_v  = 0
	
	teste     = 0
	contador  = 0
	somatorio = 0

	angle1 = 0
	angle2 = 0

	test_angle = 0

	cxr1 = 0
	cxr2 = 0
	cxr3 = 0
	cxr4 = 0
	
	cyr1 = 0
	cyr2 = 0
	cyr3 = 0
	cyr4 = 0

	cxr = 0
	cyr = 0

	cxb1 = 0
	cxb2 = 0
	cxb3 = 0

	cyb1 = 0
	cyb2 = 0
	cyb3 = 0

	botao_1 = 0
	botao_2 = 0

	read_botton(37, 35)

	######################## canny ########################
	
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	#cv2.imshow("gray",gray)
	gauss = cv2.GaussianBlur(gray, (5,5),0)
	#cv2.imshow("gauss",gauss)
	canny = cv2.Canny(gauss, 50, 150)
	cv2.imshow("canny",canny)
	
	######################## canny ########################

	'''
	# definicao ponto de referencia
	def find_marker(res5):
		gray = cv2.cvtColor(res5, cv2.COLOR_BGR2GRAY)
		gray = cv2.GaussianBlur(res5, (5,5), 0)
		edged = cv2.Canny(gray, 35, 125)

		cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
		cnts = cnts[0] if imutils.is_cv2() else cnts[1]
		c = max(cnts, key = cv2.contourArea)
		
		return cv2.minAreaRect(c)

	def distance_to_camera(knownWidth, focalLength, perWidth):
		return (knownWidth * focalLength) / perWidth

	# definicao ponto de referencia
	'''

	########################## center line ##########################
	def drawBasicGrid(img, pxstep, midX, midY):
		
		x = pxstep
		y = pxstep
		
		while x < img.shape[1]:
                        
			#cv2.line(img, (x, 0), (x, img.shape[0]), color=(255, 0, 255), thickness = 1) #Linhas verticais de referencia
			x += pxstep
			
		while y < img.shape[0]:
                        
			#cv2.line(img, (0, y), (img.shape[1], y),color=(255, 0, 255),thickness = 1) #Linhas verticais de referencia
			y += pxstep
 
	def makeBoundingBox(h,w, step):

		y = 0
		bbox = []
		
		while y < h:
                        
			x=0
			
			while x < w:
                                
			    bbox.append([(x,y), (x+step, y+step)])
			    x += step
			y += step
			
		return bbox
	
	(H,W) = img.shape[:2]

	midY = H//2
	midX = W//2
	
	# Draw center line
	cv2.line(img, (0, midY), (W, midY), (0, 255, 0), thickness = 1)
	cv2.line(img, (midX, 0), (midX, H), (0, 255, 0), thickness = 1)
	
	drawBasicGrid(img, 40, midX,midY)
	bbox = makeBoundingBox(H, W, 40)
        ########################## center line ##########################
	
	#################### definicao ponto de referencia ##################
	'''
	KNOWN_DISTANCE = 24.4
	KNOWN_WIDTH = 11.0

	marker = find_marker(res5)
	focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH
	inches = distance_to_camera(KNOWN_WIDTH, focalLength, marker[1][0])
	box = cv2.cv.BoxPoints(marker) if imutils.is_cv2() else cv2.boxPoints(marker)
	box = np.int0(box)

	cv2.drawContours(res5, [box], -1, (0, 255, 0), 2)
	cv2.drawContours(img, [box], -1, (0, 255, 0), 2)
	cv2.putText(res5, "%.2f ft" % focalLength, (res5.shape[1] - 200, res5.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 2)
	cv2.putText(img, "%.2f ft" % focalLength, (res5.shape[1] - 200, res5.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 2)

	#print ('focalLength: ' +str(focalLength))
	'''
	################### definicao ponto de referencia ################

	######################### LDR GRAPH ############################
	if graph == 1:
			
		osvalue = os.popen('vcgencmd measure_value').readline()
		value = (osvalue.replace("value=", "").replace("'C\n", ""))
	
		LDR1.append(ldr_1(LDR_1))
		#LDR2.append(ldr_2(LDR_2))
		#LDR3.append(ldr_3(LDR_3))
			
		plotNow()

	######################### Historogram ############################
	if histogram == 1:
			
		if resizeWidth > 0:
                        
			    (height, width) = frame.array.shape[:2]
			    resizeHeight = int(float(resizeWidth / width) * height)
			    frame.array = cv2.resize(frame.array, (resizeWidth, resizeHeight),interpolation=cv2.INTER_AREA)

		numPixels = np.prod(frame.array.shape[:2])


		if color == 'rgb':
                        
				(b, g, r) = cv2.split(frame.array)
				histogramR = cv2.calcHist([r], [0], None, [bins], [0, 255]) / numPixels
				histogramG = cv2.calcHist([g], [0], None, [bins], [0, 255]) / numPixels
				histogramB = cv2.calcHist([b], [0], None, [bins], [0, 255]) / numPixels
				lineR.set_ydata(histogramR)
				lineG.set_ydata(histogramG)
				lineB.set_ydata(histogramB)

		else:
				gray = cv2.cvtColor(frame.array, cv2.COLOR_BGR2GRAY)
				cv2.imshow('Grayscale', gray)
				histogram = cv2.calcHist([gray], [0], None, [bins], [0, 255]) / numPixels
				lineGray.set_ydata(histogram)

		fig.canvas.draw()

	######################### LED Control ################################
		
	if pwm == 1 :
                
		LED_control(LDR_1)

	#Tracking the Red Color
	(_,contours,hierarchy)=cv2.findContours(red.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	for picr, contour in enumerate(contours):
                
		area = cv2.contourArea(contour)

		if(area>1000 and area<7000):

			pic_r += 1

			M1 = []

			cxr = []
			cyr = []
			
			M1 = cv2.moments(contour)
			
			cxr = int(M1['m10'] / M1['m00'])
			cyr = int(M1['m01'] / M1['m00'])
			
			centers.append([cxr, cyr])
			
			k = cv2.circle(img, (cxr, cyr), 2, (0,0,0), 2 )
			
			D = np.linalg.norm(cxr-cyr)

			x,y,w,h = cv2.boundingRect(contour)

			x_d  = x/11,82
			y_d  = y/11,82
			cx_d = cxr/11,82
			cy_d = cyr/11,82

			if pic_r == 1:

				cxr1  = cxr
				cyr1  = cyr

			if pic_r == 2:

				cxr2  = cxr
				cyr2  = cyr

			if pic_r == 3:

				cxr3  = cxr
				cyr3  = cyr

			if pic_r == 4:

				cxr4  = cxr
				cyr4  = cyr

			raio = math.sqrt(area/math.pi)
			
			cv2.drawContours(img, contour, -1, (0, 0, 255), 2)
			cv2.drawContours(res, contour, -1, (255, 255, 255), 2)

			gui_red(img, x,y, pic_r, x_d, y_d, cx_d, cy_d, raio, area)


	#Tracking the Blue Color
	(_,contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	for picb, contour in enumerate(contours):
                
		area = cv2.contourArea(contour)
		
		if(area>800 and area<15000):
                        
			pic_b += 1
			
			M2 = cv2.moments(contour)
			
			cx = int(M2['m10'] / M2['m00'])
			cy = int(M2['m01'] / M2['m00'])
			
			centers.append([cx, cy])

			k = cv2.circle(img, (cx, cy), 2, (0,0,0), 2 )
			w = cv2.circle(res1, (cx, cy), 2, (0,0,0), 2 )
			
			D = np.linalg.norm(cx-cy)

			x,y,w,h = cv2.boundingRect(contour)

			x_d = x/11,82
			y_d = y/11,82
			cx_d = cx/11,82
			cy_d = cy/11,82

			raio = math.sqrt(area/math.pi)
			
			cv2.drawContours(img, contour, -1, (255, 0, 0), 2)
			cv2.drawContours(res1, contour, -1, (255, 255, 255), 2)

			gui_blue(img, x,y, pic_b, x_d, y_d, cx_d, cy_d, raio, area)

			if pic_b == 1:

				cxb1  = cx
				cyb1  = cy

			if pic_b == 2:
                                
				cxb2  = cx
				cyb2  = cy

			############################## angulo de Oxigenio em relacao a Nitrogenio ##############################
			'''

			
			if cxr1 != 0:

				cv2.line(img, (cxb1, cyb1) , (cxr1, cyr1), (0,255,0), lineThickness)
				cv2.line(img, (cxb1, cyb1) , (cxr1, cyb1), (0,255,0), lineThickness)
				cv2.line(img, (cxr1, cyr1) , (cxr1, cyb1), (0,255,0), lineThickness)

				hypotenuse = distance(cxb1, cyb1, cxr1, cyr1)
				horizontal = distance(cxb1, cyb1, cxr1, cyb1)
				thirdline  = distance(cxr1, cyr1, cxr1, cyb1)

				angle = np.arcsin((thirdline/hypotenuse))*180/math.pi

				cv2.putText(img,"'" +str(int(angle)), (cxr1-50, cyr1) ,cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0))
				#cv2.putText(img,"'" +str(int(hypotenuse)), (cyr1, cyr1) ,cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0))
				#cv2.putText(img,"'" +str(int(horizontal)), (cxr1, cyr1+70) ,cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0))

				if cxr2 != 0:

					cv2.line(img, (cxb1, cyb1) , (cxr2, cyr2), (0,255,255), lineThickness)
					cv2.line(img, (cxb1, cyb1) , (cxr2, cyb1), (0,255,255), lineThickness)
					cv2.line(img, (cxr2, cyr2) , (cxr2, cyb1), (0,255,255), lineThickness)

					hypotenuse = distance(cxb1, cyb1, cxr2, cyr2)
					horizontal = distance(cxb1, cyb1, cxr2, cyb1)
					thirdline  = distance(cxr2, cyr2, cxr2, cyb1)

					angle = np.arcsin((thirdline/hypotenuse))*180/math.pi

					cv2.putText(img,"'" +str(int(angle)), (cxr2-50, cyr2) ,cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255))

					if cxr3 != 0:

						cv2.line(img, (cxb1, cyb1) , (cxr3, cyr3), (255,0,0), lineThickness)
						cv2.line(img, (cxb1, cyb1) , (cxr3, cyb1), (255,0,0), lineThickness)
						cv2.line(img, (cxr3, cyr3) , (cxr3, cyb1), (255,0,0), lineThickness)

						hypotenuse = distance(cxb1, cyb1, cxr3, cyr3)
						horizontal = distance(cxb1, cyb1, cxr3, cyb1)
						thirdline  = distance(cxr3, cyr3, cxr3, cyb1)

						angle = np.arcsin((thirdline/hypotenuse))*180/math.pi

						cv2.putText(img,"'" +str(int(angle)), (cxr3-50, cyr3) ,cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))

						if cxr4 != 0:

							cv2.line(img, (cxb1, cyb1) , (cxr4, cyr4), (0,0,0), lineThickness)
							cv2.line(img, (cxb1, cyb1) , (cxr4, cyb1), (0,0,0), lineThickness)
							cv2.line(img, (cxr4, cyr4) , (cxr4, cyb1), (0,0,0), lineThickness)

							hypotenuse = distance(cxb1, cyb1, cxr4, cyr4)
							horizontal = distance(cxb1, cyb1, cxr4, cyb1)
							thirdline  = distance(cxr4, cyr4, cxr4, cyb1)

							angle = np.arcsin((thirdline/hypotenuse))*180/math.pi

							cv2.putText(img,"'" +str(int(angle)), (cxr4-50, cyr4) ,cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0))

			############################## angulo de Oxigenio em relacao a Nitrogenio ##############################			
			'''

			'''

			if cxr1 != 0:

				cv2.line(img, (cxb1, cyb1) , (cxr1, cyr1), (0,255,0), lineThickness)
				cv2.line(img, (cxb1, cyb1) , (cxr1, cyb1), (0,255,0), lineThickness)
				cv2.line(img, (cxr1, cyr1) , (cxr1, cyb1), (0,255,0), lineThickness)

				hypotenuse = distance(cxb1, cyb1, cxr1, cyr1)
				horizontal = distance(cxb1, cyb1, cxr1, cyb1)
				thirdline  = distance(cxr1, cyr1, cxr1, cyb1)

				angle = np.arcsin((thirdline/hypotenuse))*180/math.pi

				cv2.putText(img,"'" +str(int(angle)), (cxr1-50, cyr1) ,cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0))
				#cv2.putText(img,"'" +str(int(hypotenuse)), (cyr1, cyr1) ,cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0))
				#cv2.putText(img,"'" +str(int(horizontal)), (cxr1, cyr1+70) ,cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0))

				if cxr2 != 0:

					cv2.line(img, (cxb1, cyb1) , (cxr2, cyr2), (0,255,255), lineThickness)
					cv2.line(img, (cxb1, cyb1) , (cxr2, cyb1), (0,255,255), lineThickness)
					cv2.line(img, (cxr2, cyr2) , (cxr2, cyb1), (0,255,255), lineThickness)

					hypotenuse = distance(cxb1, cyb1, cxr2, cyr2)
					horizontal = distance(cxb1, cyb1, cxr2, cyb1)
					thirdline  = distance(cxr2, cyr2, cxr2, cyb1)

					angle = np.arcsin((thirdline/hypotenuse))*180/math.pi

					cv2.putText(img,"'" +str(int(angle)), (cxr2-50, cyr2) ,cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255))

					if cxr3 != 0:

						cv2.line(img, (cxb1, cyb1) , (cxr3, cyr3), (255,0,0), lineThickness)
						cv2.line(img, (cxb1, cyb1) , (cxr3, cyb1), (255,0,0), lineThickness)
						cv2.line(img, (cxr3, cyr3) , (cxr3, cyb1), (255,0,0), lineThickness)

						hypotenuse = distance(cxb1, cyb1, cxr3, cyr3)
						horizontal = distance(cxb1, cyb1, cxr3, cyb1)
						thirdline  = distance(cxr3, cyr3, cxr3, cyb1)

						angle = np.arcsin((thirdline/hypotenuse))*180/math.pi

						cv2.putText(img,"'" +str(int(angle)), (cxr3-50, cyr3) ,cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))

						if cxr4 != 0:

							cv2.line(img, (cxb1, cyb1) , (cxr4, cyr4), (0,0,0), lineThickness)
							cv2.line(img, (cxb1, cyb1) , (cxr4, cyb1), (0,0,0), lineThickness)
							cv2.line(img, (cxr4, cyr4) , (cxr4, cyb1), (0,0,0), lineThickness)

							hypotenuse = distance(cxb1, cyb1, cxr4, cyr4)
							horizontal = distance(cxb1, cyb1, cxr4, cyb1)
							thirdline  = distance(cxr4, cyr4, cxr4, cyb1)

							angle = np.arcsin((thirdline/hypotenuse))*180/math.pi

							cv2.putText(img,"'" +str(int(angle)), (cxr4-50, cyr4) ,cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0))

			############################## angulo de Oxigenio em relacao a Nitrogenio ##############################
							
'''
	#Tracking the yellow Color
	(_,contours,hierarchy)=cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	for picy, contour in enumerate(contours):
                
		area = cv2.contourArea(contour)
		
		if(area>500 and area<30000):
		#if(area>5000 and area<30000):

			pic_y += 1
			
			M3 = cv2.moments(contour)
			
			cx = int(M3['m10'] / M3['m00'])
			cy = int(M3['m01'] / M3['m00'])
			
			centers.append([cx, cy])

			k = cv2.circle(img, (cx, cy), 2, (0,0,0), 2 )
			w = cv2.circle(res2, (cx, cy), 2, (0,0,0), 2 )
			
			D = np.linalg.norm(cx-cy)

			x,y,w,h = cv2.boundingRect(contour)

			x_d = x/11,82
			y_d = y/11,82
			cx_d = cx/11,82
			cy_d = cy/11,82

			raio = math.sqrt(area/math.pi)
			
			cv2.drawContours(img, contour, -1, (40, 255, 255), 2)
			cv2.drawContours(res2, contour, -1, (255, 255, 255), 2)

			gui_yellow(img, x,y, pic_y, x_d, y_d, cx_d, cy_d, raio, area)

	#Tracking the Green Color
	(_,contours,hierarchy)=cv2.findContours(green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	for picg, contour in enumerate(contours):

		area = cv2.contourArea(contour)
		if(area>800 and area <15000):
                        
			pic_v+= 1

			M4 = cv2.moments(contour)
			
			cx = int(M4['m10'] / M4['m00'])
			cy = int(M4['m01'] / M4['m00'])
			
			centers.append([cx, cy])
			
			k = cv2.circle(img, (cx, cy), 2, (0,0,0), 2 )
			w = cv2.circle(res5, (cx, cy), 2, (0,0,0), 2 )
			
			D = np.linalg.norm(cx-cy)
			
			x,y,w,h = cv2.boundingRect(contour)

			x_d = x/11,82
			y_d = y/11,82
			cx_d = cx/11,82
			cy_d = cy/11,82

			raio = math.sqrt(area/math.pi)

			cv2.drawContours(img, contour, -1, (0, 255, 255), 2)
			cv2.drawContours(res5, contour, -1, (0, 255, 255), 2)

			gui_green(img, x,y, pic_v, x_d, y_d, cx_d, cy_d, raio, area)


	#Tracking the White Color

	(_,contours,hierarchy)=cv2.findContours(white,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	for picw, contour in enumerate(contours):
                
		#white_color(picw,contour,contours)
				
		area = cv2.contourArea(contour)
		
		if(area>100 and area <8000):
                        
			pic_w+= 1
			
			M5 = cv2.moments(contour)
			
			cx = int(M5['m10'] / M5['m00'])
			cy = int(M5['m01'] / M5['m00'])
			
			centers.append([cx, cy])
			
			k = cv2.circle(img, (cx, cy), 2, (0,0,0), 2 )
			w = cv2.circle(res4, (cx, cy), 2, (0,0,0), 2 )
			
			D = np.linalg.norm(cx-cy)
			
			x,y,w,h = cv2.boundingRect(contour)

			x_d = x/11,82
			y_d = y/11,82
			cx_d = cx/11,82
			cy_d = cy/11,82

			raio = math.sqrt(area/math.pi)
			
			cv2.drawContours(img, contour, -1, (0, 0, 0), 2)
			cv2.drawContours(res4, contour, -1, (0,0,255), 2)

			gui_white(img, x,y, pic_w, x_d, y_d, cx_d, cy_d, raio, area)

	'''
	#Tracking the Black Color
	(_,contours,hierarchy)=cv2.findContours(black,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	for picbb, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>300):
			x,y,w,h = cv2.boundingRect(contour)
			#img = cv2.drawContours(img, contour, -1, (255, 255, 255), 2)

			gui_black(img, x,y, pic_bb, x_d, y_d, cx_d, cy_d, raio, area)
			

	#Tracking the Gray Color
	(_,contours,hierarchy)=cv2.findContours(gray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	for picgg, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		
		if(area>500 and area <15000):
                        
			pic_g += 1

			gui_gray(img, x,y, pic_gg, x_d, y_d, cx_d, cy_d, raio, area)

	'''

  
	############## teste de identificacao automatica #################

	'''

	if (amino == 'Cadeia Principal'):
			
			#audio(amino, result)
			
			cv2.putText(img, "Cadeia Principal",(220,60),cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255),3)

			dt = datetime.today()

			seconds = dt.timestamp()

			print("SEGUNDOS:",seconds)

			for seconds in range(0,350):
		
				print("seconds", seconds)
				print("saiu")

			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/aminoacidos/01_cadeia_principal.mp3")
			pygame.mixer.music.play()
				
		
				#value += 1

				#print("value", value)

				#time.sleep(1)

	'''


	amino , result = tree(pic_r, pic_b, pic_v, pic_y, pic_w)

	#conta_aminoacidos(amino)

	#LED_control(LDR_1)

	tela_principal(img, pic_r, pic_b, pic_y, pic_v, pic_w, amino, result, ldr_1(LDR_1))
			
	######################################## Tela #######################################################
	
	cv2.imshow("DeMOLidor",img)
	#cv2.imshow("RED",res)
	#cv2.imshow("BLUE",res1)
	#cv2.imshow("YELLOW",res2)
	#cv2.imshow("GRAY",res3)
	#cv2.imshow("WHITE",res4)
	#cv2.imshow("GREEN",res5)
	
	######################################## Tela #######################################################

	key = cv2.waitKey(10) & 0xFF # Leitura do teclado quando a imagem criada pelo OpenCv é exibida na tela

	rawCapture.truncate(0) # Limpa o frame para que o proximo possa iniciar

	aguarda_key(key, pic_r, pic_b, pic_y, pic_v, pic_w, pwm38, pwm40, amino, result) # funcao de leitura de teclado 

	if key == ord("q"):
		break

cap.release()
out.release()

cv2.destroyAllWindows() 

