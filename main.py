# -*- coding: utf-8 -*-
#!/usr/bin/env python
#######################################################################
#####                                                             #####
#####                     Jeferson S. Pazze                       #####
#####                jeferson.pazze@acad.pucrs.br                 #####
#####                       09/27/2018                            #####
#####                      LABIO - PUCRS                          #####
#####       Real-time ,Color tracking and matchesTheshold         #####
#####                                                             #####
#######################################################################

# import the necessary packages

from picamera.array import PiRGBArray
from picamera import PiCamera
from contextlib import contextmanager
from tkinter import *

import time
import os
import pygame
import sys
import itertools as it
import numpy as np
import cv2 as cv
import cv2
import matplotlib.pyplot as plt

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

# define range of red color in HSV
#lower_red = np.array([150, 30, 30])     
#upper_red = np.array([200, 255, 255])
#lower_red = np.array([151, 136, 91])     #calib 25092018
#upper_red = np.array([179, 255, 255])    #calib 25092018
lower_red = np.array([172, 61, 57])       #calib 26092018
upper_red = np.array([179, 255, 255])     #calib 26092018

# define range of blue color in HSV
#lower_blue = np.array([112,173,60])     #calib 24092018
#upper_blue = np.array([128,255,214])    #calib 24092018
lower_blue = np.array([111,131,54])      #calib 26092018
upper_blue = np.array([140,255,255])     #calib 26092018

#lower_blue = np.array([115,150,80]) 
#upper_blue = np.array([125,255,255]) 

# define range of yellow color in HSV
lower_yellow = np.array([10,100,100])
upper_yellow = np.array([40,255,255])
#lower_yellow = np.array([17,150,194])    #calib 25092018
#upper_yellow = np.array([28,255,255])    #calib 25092018

# define range of gray color in HSV
lower_gray = np.array([106, 47, 66])
upper_gray = np.array([114, 78, 255])
#lower_gray = np.array([98, 90, 30])      #calib 26092018
#upper_gray = np.array([108, 220, 255])   #calib 26092018
#lower_gray = np.array([120, 15, 40])
#upper_gray = np.array([255, 90, 128])

PY3 = sys.version_info[0] == 3
if PY3:
    xrange = range

################### interface ################### 
'''    
class Application:
    def __init__(self, master=None):
        
        pygame.mixer.init()
        pygame.mixer.music.load("ini_software.mp3")
        pygame.mixer.music.play()
        
        self.widget1 = Frame(master)
        self.widget1.pack(side=RIGHT)
        self.msg = Label(self.widget1, text="Iniciar Software ?")
        self.msg["font"] = ("Verdana", "12", "italic", "bold")
        
        self.msg.pack ()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Sim"
        self.sair["font"] = ("Verdana", "10")
        self.sair["width"] = 15
        self.sair["command"] = self.widget1.quit
        self.sair.pack (side=RIGHT)
        
        self.msg.pack ()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Nao"
        self.sair["font"] = ("Verdana", "10")
        self.sair["width"] = 15
        self.sair["command"] = self.widget1.quit
        self.sair.pack (side=RIGHT)

root = Tk()
Application(root)
root.mainloop()

# audio payback test
pygame.mixer.init()
pygame.mixer.music.load("welcome_demolidor.mp3")
pygame.mixer.music.play()


'''

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
  
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
  
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
  
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()
  
        self.titulo = Label(self.primeiroContainer, text="Dados do usuário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
  
        self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
  
        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)
  
        self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)
  
        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)
  
        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()
  
        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()
  
    #Método verificar senha
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "labio" and senha == "labio":
            self.mensagem["text"] = "Autenticado"
            
        else:
            self.mensagem["text"] = "Erro na autenticação"
  
root = Tk()
Application(root)
root.mainloop()
################### end interface ################### 

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

sift = cv2.xfeatures2d.SIFT_create()
surf = cv2.xfeatures2d.SURF_create()

##### teste 26092018 ###########

cv2.ocl.setUseOpenCL(False)
CV_LOAD_IMAGE_COLOR = 1
subsamplingRatio = 0.5
matchesTheshold = 0.5

orb = cv2.ORB_create()
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

##### teste 26092018 ###########

img = cv2.imread('/home/pi/image.jpg',1)
#img = cv2.imread('/home/pi/image_editada.jpg',1)
orb = cv2.ORB_create()
#detector = cv2.SIFT()
#extrator = cv2.DescriptorExtrator_create("SIFT")
#detector = cv2.FeatureDetector_create("SIFT")

# allow the camera to warmup
time.sleep(0.1)

#r,h,c,w = 120,85,45,60
r,h,c,w = 250,90,500,125
rr,hr,cr,wr = 60,90,500,125
ry,hy,cy,wy = 120,120,45,200
rg,hg,cg,wg = 120,80,120,80

track_window = (c,r,w,h)
track_window_red = (cr,rr,wr,hr)
track_window_yellow = (cy,ry,wy,hy)
track_window_gray = (cg,rg,wg,hg)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text

	image = frame.array
	ret = image
	ret_red = image
	ret_yellow = image
	ret_gray = image

	kp1, des1 = orb.detectAndCompute(img, None)
	kp2, des2 = orb.detectAndCompute(image, None)

	bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

	matches = bf.match(des1, des2)
	matches = sorted(matches, key = lambda x:x.distance)

	# apply ratio test
	good = []
	
	'''for m,n in matches:
	    if m.distance < 0.75*n.distance:
                 good.append([m])
        '''       
	img3 = cv2.drawMatches(img, kp1, image, kp2, matches[:15], None, flags=2)

        # ROI image
	roi = image[r:r+h, c:c+w]
	roi_red = image[rr:rr+hr, cr:cr+wr]
	roi_yellow = image[ry:ry+hy, cy:cy+wy]
	roi_gray = image[rg:rg+hg, cg:cg+wg]

	# Convert BGR to HSV
	hsv_blue = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	hsv_red = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	hsv_yellow = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	hsv_gray = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

	# Threshold the HSV image
	mask_blue = cv2.inRange(hsv_blue, lower_blue, upper_blue,) # Threshold the HSV image to get only blue colors
	mask_red = cv2.inRange(hsv_red, lower_red, upper_red,) # Threshold the HSV image to get only red colors
	mask_yellow = cv2.inRange(hsv_yellow, lower_yellow, upper_yellow,) # Threshold the HSV image to get only red colors
	mask_gray = cv2.inRange(hsv_gray, lower_gray, upper_gray,) # Threshold the HSV image to get only red colors

	# Bitwise-AND mask and original image
	res_blue = cv2.bitwise_and(image,image, mask= mask_blue)
	res_red = cv2.bitwise_and(image,image, mask= mask_red)
	res_yellow = cv2.bitwise_and(image,image, mask= mask_yellow)
	res_gray = cv2.bitwise_and(image,image, mask= mask_gray)

	# Convert BGR to HSV
	hsv_roi = cv2.cvtColor(res_blue, cv2.COLOR_BGR2HSV) 
	hsv_roi_red = cv2.cvtColor(res_red, cv2.COLOR_BGR2HSV) ### teste
	hsv_roi_yellow = cv2.cvtColor(res_yellow, cv2.COLOR_BGR2HSV) ### teste
	hsv_roi_gray = cv2.cvtColor(res_gray, cv2.COLOR_BGR2HSV) ### teste

	####################### Blue ####################
	roi_hist = cv2.calcHist([hsv_roi],[0],mask_blue,[180],[0,180])
	cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
	####################### Blue ####################
	
        ####################### RED #####################
	roi_hist_red = cv2.calcHist([hsv_roi_red],[0],mask_red,[180],[0,255])
	cv2.normalize(roi_hist_red,roi_hist_red,0,255,cv2.NORM_MINMAX)
	####################### RED #####################

	####################### YELLOW ##################
	roi_hist_yellow = cv2.calcHist([hsv_roi_yellow],[0],mask_yellow,[180],[0,180])
	cv2.normalize(roi_hist_yellow,roi_hist_yellow,0,255,cv2.NORM_MINMAX)
        ####################### YELLOW ##################

	####################### GRAY ####################
	roi_hist_gray = cv2.calcHist([hsv_roi_gray],[0],mask_gray,[180],[0,180])
	cv2.normalize(roi_hist_gray,roi_hist_gray,0,180,cv2.NORM_MINMAX)
        ####################### GRAY ####################
	
	# Setup the termination criteria, either 10 iteration or move by atleast 1 pt
	term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

	dst = cv2.calcBackProject([hsv_blue],[0],roi_hist,[0,180],100)
	#dst_red = cv2.calcBackProject([hsv_red],[0],roi_hist,[0,255],5)
	dst_red = cv2.calcBackProject([hsv_red],[0],roi_hist_red,[0,255],100)
	dst_yellow = cv2.calcBackProject([hsv_yellow],[0],roi_hist_yellow,[0,255],5)#########
	dst_gray = cv2.calcBackProject([hsv_gray],[0],roi_hist_gray,[0,255],5)#########

	te = cv2.findContours(mask_blue.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
	'''
	cv2.drawContours(ret, te, (255,0,0),3)
	for i in range(len(te)):
		xx,yy,ww,hh=cv2.boundingRect(conts[i])
		cv2.rectangle(ret, (xx,yy), (xx+ww,yy+hh), (0,0,255),2)
        '''

        # Draw it on images
	x,y,w,h = track_window
	xr,yr,wr,hr = track_window_red
	xy,yy,wy,hy = track_window_yellow
	xg,yg,wg,hg = track_window_gray
	
	font = cv2.FONT_HERSHEY_SIMPLEX

	#apply meanshift to get the new location
	ret, track_window = cv2.meanShift(dst, track_window, term_crit)
	ret, track_window_red = cv2.meanShift(dst_red, track_window_red, term_crit)#########
	ret, track_window_yellow = cv2.meanShift(dst_yellow, track_window_yellow, term_crit)#########
	ret, track_window_gray = cv2.meanShift(dst_gray, track_window_gray, term_crit)#########

	#circles = cv.HoughCircles(image, cv.HOUGH_GRADIENT, 1, 10, np.array([]), 100, 30, 1, 30)
	
	img2 = cv2.rectangle(image, (x,y), (x+w,y+h), 255,2) # largura da linha e cor
	img2 = cv2.rectangle(res_blue, (x,y), (x+w,y+h), (255,0,0), 2) # largura da linha e cor
	img2 = cv2.putText(res_blue, 'Nitrogen', (x,y), font, 0.9, (255,0), 2)

	img5 = cv2.rectangle(image, (x,y), (x+w,y+h), 255,2) # largura da linha e cor
	img5 = cv2.rectangle(res_red, (xr,yr), (xr+wr,yr+hr), (0,0,255),2) # largura da linha e cor
	img5 = cv2.putText(res_red, 'Oxygen', (xr,yr), font, 0.9, (0,0,255), 2)

	img6 = cv2.rectangle(image, (x,y), (x+w,y+h), 255,2) # largura da linha e cor
	img6 = cv2.rectangle(res_yellow, (xy,yy), (xy+wy,yy+hy), (40,255,255),2) # largura da linha e cor
	img6 = cv2.putText(res_yellow, 'Phosphorus', (xy,yy), font, 0.9, (40,255,255), 2)

	img7 = cv2.rectangle(image, (x,y), (x+w,y+h), 255,2) # largura da linha e cor
	img7 = cv2.rectangle(res_gray, (xg,yg), (xg+wg,yg+hg), DARKGRAY, 2) # largura da linha e cor
	img7 = cv2.putText(res_gray, 'Carbon', (xg,yg), font, 0.9, DARKGRAY, 2)
	
        #########################################################################################
	img4 = cv2.rectangle(image, (x,y), (x+w,y+h), 255,2) # testando impressao da mask
	img4 = cv2.putText(image, 'Nitrogen', (x,y), font, 0.9, (255,0), 2)
	
	img4 = cv2.rectangle(image, (xr,yr), (xr+wr,yr+hr), (0,0,255),2) # largura da linha e cor
	img4 = cv2.putText(image, 'Oxygen', (xr,yr), font, 0.9, (0,0,255), 2)
	
	img4 = cv2.rectangle(image, (xy,yy), (xy+wy,yy+hy), (40,255,255),2) # largura da linha e cor
	img4 = cv2.putText(image, 'Phosphorus', (xy,yy), font, 0.9, (40,255,255), 2)

	img4 = cv2.rectangle(image, (xg,yg), (xg+wg,yg+hg), WHITE, 2) # largura da linha e cor
	img4 = cv2.putText(image, 'Carbon', (xg,yg), font, 0.9, WHITE, 2)
        #########################################################################################
	
	# show the frame
	cv2.imshow('Real image', img4)
	cv2.imshow('GRAY',res_gray) 
	cv2.imshow('RED',res_red)
	cv2.imshow('BLUE',res_blue)
	cv2.imshow('YELLOW',res_yellow)

	cv2.imshow('matches', img3)
	#cv2.imshow('res_red',res_red)

	key = cv2.waitKey(1) & 0xFF

	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break


