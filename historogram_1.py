# -*- coding: utf-8 -*-
#!/usr/bin/env python

#######################################################################
#####                                                             #####
#####                     Jeferson S. Pazze                       #####
#####                jeferson.pazze@acad.pucrs.br                 #####
#####                       11/30/2018                            #####
#####                      LABIO - PUCRS                          #####
#####                      Historograma                           #####
#####                                                             #####
#######################################################################

# import the necessary packages
import time
import os
import pygame
import sys
import itertools as it
import numpy as np
import cv2 as cv
import cv2
import matplotlib.pyplot as plt
import math
import imutils

from tkinter import *
from picamera.array import PiRGBArray
from picamera import PiCamera
from contextlib import contextmanager
from colors import *

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file',help='Path to video file (if not using camera)')
parser.add_argument('-c', '--color', type=str, default='rgb', help='Color space: "gray" (default) or "rgb"')
parser.add_argument('-b', '--bins', type=int, default=16, help='Number of bins per channel (default 16)')
parser.add_argument('-w', '--width', type=int, default=0, help='Resize video to specified width in pixels (maintains aspect)')
args = vars(parser.parse_args())

# Configure VideoCapture class instance for using camera or file input.

color = args['color']
bins = args['bins']
resizeWidth = args['width']

# Initialize plot.
fig, ax = plt.subplots()

if color == 'rgb':
    ax.set_title('Histogram (RGB)')
    
else:
    ax.set_title('Histogram (grayscale)')
    ax.set_xlabel('Bin')
    ax.set_ylabel('Frequency')

# Initialize plot line object(s). Turn on interactive plotting and show plot.
lw = 3
alpha = 0.5

if color == 'rgb':
        
    lineR, = ax.plot(np.arange(bins), np.zeros((bins,)), c='r', lw=lw, alpha=alpha)
    lineG, = ax.plot(np.arange(bins), np.zeros((bins,)), c='g', lw=lw, alpha=alpha)
    lineB, = ax.plot(np.arange(bins), np.zeros((bins,)), c='b', lw=lw, alpha=alpha)
    
else:
        
    lineGray, = ax.plot(np.arange(bins), np.zeros((bins,1)), c='k', lw=lw)
    
ax.set_xlim(0, bins-1)
ax.set_ylim(0, 1)
plt.ion()
plt.show()

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 16
rawCapture = PiRGBArray(camera, size=(640, 480))

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

	img = frame.array
   
	# Resize frame to width, if specified.
	if resizeWidth > 0:
		(height, width) = frame.array.shape[:2]
		resizeHeight = int(float(resizeWidth / width) * height)
		frame.array = cv2.resize(frame.array, (resizeWidth, resizeHeight),interpolation=cv2.INTER_AREA)

	# Normalize histograms based on number of pixels per frame.
	numPixels = np.prod(frame.array.shape[:2])
	
	if color == 'rgb':
		cv2.imshow('RGB', frame.array)
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

	
	########### canny  ###########
	gris = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	gauss = cv2.GaussianBlur(gris, (5,5),0)
	canny = cv2.Canny(gauss, 50, 150)
	cv2.imshow("canny",canny)
	########### canny  ###########


	################# center line ########################################################
	def drawBasicGrid(img, pxstep, midX, midY):
		
		x = pxstep
		y = pxstep
		#Draw all x lines
		
		while x < img.shape[1]:
			#cv2.line(img, (x, 0), (x, img.shape[0]), color=(255, 0, 255), thickness = 1)
			x += pxstep
			
		while y < img.shape[0]:
			#cv2.line(img, (0, y), (img.shape[1], y), color=(255, 0, 255),thickness = 1)
			y += pxstep

	def makeBoundingBox(h,w, step):
		
		#BBox is 100*100 square or step which is defied
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
	
	#Create bounding boxes for the image
	midY = H//2 
	midX = W//2    
	
	#Draw center line
	cv2.line(img, (0, midY), (W, midY), (0, 255, 0), thickness = 1)
	cv2.line(img, (midX, 0), (midX, H), (0, 255, 0), thickness = 1)
	
	drawBasicGrid(img, 40, midX,midY)
	bbox = makeBoundingBox(H, W, 40)
	################# center line ######################################################
	
	cv2.imshow("Color Tracking",img)

	#cv2.imshow("Histogram",hist)

	key = cv2.waitKey(10) & 0xFF

	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

capture.release()
cv2.destroyAllWindows()

	

