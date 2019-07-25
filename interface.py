# -*- coding: utf-8 -*-
#!/usr/bin/env python

#######################################################################
#####                                                             #####
#####                     Jeferson S. Pazze                       #####
#####                                                             #####
#####                jeferson.pazze@edu.pucrs.br                  #####
#####                                                             #####
#####                       17/06/2019                            #####
#####                                                             #####
#####                      LABIO - PUCRS                          #####
#####                                                             #####
#####                        INTERFACE                            #####
#####                                                             #####
#######################################################################

author__ = 'PAZZE'

import time
import os
import sys
import cv2
import numpy as np
import cv2   as cv


def gui_red(img, x,y, pic_r, x_d, y_d, cx_d, cy_d, raio, area):
    
    cv2.putText(img,"Oxygen",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
    cv2.putText(img, ""+str(pic_r),(x+25,y+25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255),2)

    #cv2.putText(img, "x: "+str(x_d),(x+25,y+45),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255),1)
    #cv2.putText(img, "y: "+str(y_d),(x+25,y+65),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255),1)

    #cv2.putText(res,"Oxygen",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
    #cv2.putText(res, ""+str(pic_r),(x+25,y+25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255),2)
    #cv2.putText(res, "x: "+str(x_d),(x+25,y+45),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255),1)
    #cv2.putText(res, "y: "+str(y_d),(x+25,y+65),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255),1)
    #cv2.putText(res, "cx: "+str(cx_d),(x+25,y+85),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255),1)
    #cv2.putText(res, "cy: "+str(cy_d),(x+25,y+105),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255),1)
    #cv2.putText(res, "Raio: "+str(raio),(x+25,y+125),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255),1)
    #cv2.putText(res, "Area: "+str(area),(x+25,y+145),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255),1)

    #cv2.putText(res, "LDR_1: "+str(ldr_1(LDR_1)),(15,140),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255),1)
    #cv2.putText(img, "LDR: "+str(rc_time(pin_to_circuit)),(25,165),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255),1)


def gui_blue(img, x,y, pic_b, x_d, y_d, cx_d, cy_d, raio, area):

    cv2.putText(img,"Nitrogen",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))
    cv2.putText(img, ""+str(pic_b),(x+25,y+25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255),2)
    #cv2.putText(img, "x: "+str(x_d),(x+25,y+45),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255),1)
    #cv2.putText(img, "y: "+str(y_d),(x+25,y+65),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255),1)


def gui_yellow(img, x,y, pic_y, x_d, y_d, cx_d, cy_d, raio, area):
    
    cv2.putText(img,"Sulfur",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (40,255,255))
    cv2.putText(img, ""+str(pic_y),(x+25,y+25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255),2)
    #cv2.putText(img, "x: "+str(x_d),(x+25,y+45),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255),1)
    #cv2.putText(img, "y: "+str(y_d),(x+25,y+65),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255),1)

    '''
    cv2.putText(res2,"Sulfur",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (40,255,255))
    cv2.putText(res2, ""+str(pic_y),(x+25,y+25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255),2)
    cv2.putText(res2, "x: "+str(x_d),(x+25,y+45),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255),1)
    cv2.putText(res2, "y: "+str(y_d),(x+25,y+65),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255),1)
    cv2.putText(res2, "cx: "+str(cx_d),(x+25,y+85),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255),1)
    cv2.putText(res2, "cy: "+str(cy_d),(x+25,y+105),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255),1)
    cv2.putText(res2, "Raio: "+str(raio),(x+25,y+125),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255),1)
    cv2.putText(res2, "Area: "+str(area),(x+25,y+145),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255),1)
    '''

def gui_green(img, x,y, pic_v, x_d, y_d, cx_d, cy_d, raio, area):

    cv2.putText(img,"Carbon",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0))
    cv2.putText(img, ""+str(pic_v),(x+25,y+25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255),2)
    #cv2.putText(img, "x: "+str(x_d),(x+25,y+45),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255),1)
    #cv2.putText(img, "y: "+str(y_d),(x+25,y+65),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255),1)

    '''
    cv2.putText(res5,"Carbon",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255))
    cv2.putText(res5, ""+str(pic_v),(x+25,y+25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
    cv2.putText(res5, "x: "+str(x_d),(x+25,y+45),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 255, 255), 1)
    cv2.putText(res5, "y: "+str(y_d),(x+25,y+65),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 255, 255), 1)
    cv2.putText(res5, "cx: "+str(cx_d),(x+25,y+85),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 255, 255), 1)
    cv2.putText(res5, "cy: "+str(cy_d),(x+25,y+105),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 255, 255), 1)
    cv2.putText(res5, "Raio: "+str(raio),(x+25,y+125),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 255, 255), 1)
    cv2.putText(res5, "Area: "+str(area),(x+25,y+145),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 255, 255), 1)
    '''

def gui_white(img, x,y, pic_w, x_d, y_d, cx_d, cy_d, raio, area):

    cv2.putText(img,"Hidrogen",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0))
    cv2.putText(img, ""+str(pic_w),(x+25,y+25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0),2)
    #cv2.putText(img, "x: "+str(x_d),(x+25,y+45),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0,0,0),1)
    #cv2.putText(img, "y: "+str(y_d),(x+25,y+65),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0,0,0),1)

    '''		
    cv2.putText(res4,"Hidrogen",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255))
    cv2.putText(res4, ""+str(pic_w),(x+25,y+25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255),2)
    cv2.putText(res4, "x: "+str(x_d),(x+25,y+45),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255, 255, 255),1)
    cv2.putText(res4, "y: "+str(y_d),(x+25,y+65),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255, 255, 255),1)
    cv2.putText(res4, "cx: "+str(cx_d),(x+25,y+85),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255, 255, 255),1)
    cv2.putText(res4, "cy: "+str(cy_d),(x+25,y+105),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255, 255, 255),1)
    cv2.putText(res4, "Raio: "+str(raio),(x+25,y+125),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255, 255, 255),1)
    cv2.putText(res4, "Area: "+str(area),(x+25,y+145),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255, 255, 255),1)
    '''

def gui_black(img, x,y, pic_bb, x_d, y_d, cx_d, cy_d, raio, area):

    print("")

def gui_gray(img, x,y, pic_gg, x_d, y_d, cx_d, cy_d, raio, area):

    print("")

def tela_principal(img, pic_r, pic_b, pic_y, pic_v, pic_w, amino, result, LDR_1):
    	
    cv2.putText(img, "Oxygen: "   +str(pic_r),(15,20),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255),1)
    cv2.putText(img, "Nitrogen: " +str(pic_b),(15,40),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255),1)
    cv2.putText(img, "Sulfur: "   +str(pic_y),(15,60),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255),1)
    cv2.putText(img, "Carbon: "   +str(pic_v),(15,80),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255),1)
    cv2.putText(img, "Hidrogen: " +str(pic_w),(15,100),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255),1)
    cv2.putText(img, "Amino: "    +str(amino), (10,470),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255),1)
    cv2.putText(img, "Acuracia % "+str(int(result)), (220,30),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255),1)

    #cv2.putText(img, "Intensidade LED: " +str(LED_control(LDR_1)),(15,140),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255),1)
    cv2.putText(img, "LDR_1: "+str(LDR_1),(15,160),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255),1)
    #cv2.putText(img, "LDR_2: "+str(ldr_2(LDR_2)),(15,160),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255),1)
    #cv2.putText(img, "LDR_3: "+str(ldr_3(LDR_3)),(15,180),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255),1)

    #cv2.putText(img, "Fator multiplicador: "+str(cal),(15,200),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255),1)
    #cv2.putText(img, "MMA LDR_1: " +str(med(MED)),(15,220),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255),1)
    #cv2.putText(img, "LDR_1 compensado: " +str(l_v*int(cal)),(15,200),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255),1)
    #cv2.putText(img, "LDR_1 REAL: " +str(l_v),(15,220),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255),1)


print('interface inicialized')
