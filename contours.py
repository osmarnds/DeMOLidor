# -*- coding: utf-8 -*-
#!/usr/bin/env python

#######################################################################
#####                                                             #####
#####                     Jeferson S. Pazze                       #####
#####                jeferson.pazze@acad.pucrs.br                 #####
#####                       09/28/2018                            #####
#####                      LABIO - PUCRS                          #####
#####                        contours                             #####
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

from Tkinter import *
from picamera.array import PiRGBArray
from picamera import PiCamera
from contextlib import contextmanager

#                R    G    B
WHITE        = (255, 255, 255)
BLACK        = (  0,   0,   0)
BRIGHTRED    = (255,   0,   0)
RED          = (255,   0,   0)
BRIGHTGREEN  = (  0, 255,   0)
GREEN        = (  0, 155,   0)
BRIGHTBLUE   = (  0,   0, 255)
BLUE         = (  0,   0, 155)
BRIGHTYELLOW = (255, 255,   0)
YELLOW       = (155, 155,   0)
DARKGRAY     = ( 40,  40,  40)

lower_blue = np.array([111,131,54])      #calib 26092018
upper_blue = np.array([140,255,255])     #calib 26092018

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

sift = cv2.xfeatures2d.SIFT_create()
surf = cv2.xfeatures2d.SURF_create()

orb = cv2.ORB_create()

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

	image = frame.array

	blurred_frame = cv2.GaussianBlur(image, (5, 5), 0)
	hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)
	
	mask = cv2.inRange(hsv, lower_blue, upper_blue)
 
	_, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

	for contour in contours:
		area = cv2.contourArea(contour)
 
		if area > 500:
			cv2.drawContours(image, contour, -1, (0, 255, 0), 1)

	cv2.imshow("Frame", image)
	cv2.imshow("Mask", mask)

	key = cv2.waitKey(1) & 0xFF

	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break





















	


