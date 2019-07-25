#######################################################################
#####                                                             #####
#####                     Jeferson S. Pazze                       #####
#####                jeferson.pazze@acad.pucrs.br                 #####
#####                       10/08/2018                            #####
#####                      LABIO - PUCRS                          #####
#####                         Colors                              #####
#####                                                             #####
#######################################################################

# import the necessary packages
import numpy as np

#print('colors inicializing...')

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

#definig the range of red color
#red_lower=np.array([136,87,111],np.uint8)
#red_upper=np.array([180,255,255],np.uint8)
red_lower1=np.array([166,170,85],np.uint8)           #calib 01102018
red_upper1=np.array([179,255,200],np.uint8)          #calib 01102018
#red_lower=np.array([156,165,91],np.uint8)           #calib 16102018
#red_upper=np.array([179,255,200],np.uint8)          #calib 16102018
#red_lower=np.array([165,160,70],np.uint8)           #calib 11212018
#red_upper=np.array([179,255,200],np.uint8)          #calib 11212018
#red_lower=np.array([150,80,0],np.uint8)             #calib 26212018
#red_upper=np.array([179,255,255],np.uint8)          #calib 26212018
#red_lower=np.array([160,125,50],np.uint8)           #calib 01282019
#red_upper=np.array([179,255,255],np.uint8)          #calib 01282019
#red_lower=np.array([0,170,100],np.uint8)            #calib 03112019 CHROMA KEY
#red_upper=np.array([10,255,255],np.uint8)           #calib 03112019 CHROMA KEY
#red_lower=np.array([150,140,110],np.uint8)           #calib 03152019 Fundo Grafite
#red_upper=np.array([179,255,255],np.uint8)           #calib 03152019 Fundo Grafite
#red_lower=np.array([0,90,120],np.uint8)           #calib 2852019 Fundo Grafite
#red_upper=np.array([20,225,255],np.uint8)           #calib 2852019 Fundo Grafite
red_lower=np.array([130,60,200],np.uint8)           
red_upper=np.array([179,210,255],np.uint8)

#red_lower=np.array([120,175,120],np.uint8)           
#red_upper=np.array([179,255,255],np.uint8)

#defining the Range of Blue color
#blue_lower=np.array([99,115,150],np.uint8)
#blue_upper=np.array([110,255,255],np.uint8)
#blue_lower=np.array([105,210,77],np.uint8)          #calib 01102018
#blue_upper=np.array([120,255,255],np.uint8)         #calib 01102018
#blue_lower=np.array([115,255,100],np.uint8)         #calib 11212018
#blue_upper=np.array([120,255,215],np.uint8)         #calib 11212018
#blue_lower=np.array([110,110,110],np.uint8)         #calib 26122018
#blue_upper=np.array([140,240,220],np.uint8)         #calib 26122018
#blue_lower=np.array([100,100,100],np.uint8)         #calib 01292019
#blue_upper=np.array([130,230,255],np.uint8)         #calib 01292019
#blue_lower=np.array([105,50,50],np.uint8)           #calib 03112019 CHROMA KEY
#blue_upper=np.array([140,200,215],np.uint8)         #calib 03112019 CHROMA KEY
#blue_lower=np.array([75,60,70],np.uint8)            #calib 03142019 CHROMA KEY 2
#blue_upper=np.array([135,255,240],np.uint8)         #calib 03142019 CHROMA KEY 2
#blue_lower=np.array([105,145,145],np.uint8)          #calib 03152019 Fundo Grafite
#blue_upper=np.array([135,235,240],np.uint8)          #calib 03152019 Fundo Grafite
#blue_lower=np.array([90,90,120],np.uint8)          #calib 14052019 Fundo Grafite
#blue_upper=np.array([130,255,255],np.uint8)          #calib 14052019 Fundo Grafite
blue_lower=np.array([100,110,140],np.uint8)        
blue_upper=np.array([135,255,255],np.uint8)          

#defining the Range of yellow color
#yellow_lower=np.array([22,60,200],np.uint8)    
#yellow_upper=np.array([60,255,255],np.uint8)   
#yellow_lower=np.array([12,177,137],np.uint8)        #calib 01102018
#yellow_upper=np.array([34,255,255],np.uint8)        #calib 01102018
#yellow_lower=np.array([10,200,130],np.uint8)        #calib 11212018
#yellow_upper=np.array([25,255,255],np.uint8)        #calib 11212018
#yellow_lower=np.array([10,200,130],np.uint8)        #calib 26122018
#yellow_upper=np.array([25,255,255],np.uint8)        #calib 26122018
#yellow_lower=np.array([10,160,170],np.uint8)        #calib 01292019
#yellow_upper=np.array([30,255,255],np.uint8)        #calib 01292019
#yellow_lower=np.array([15,185,205],np.uint8)        #calib 03112019 CHROMA KEY 
#yellow_upper=np.array([35,255,255],np.uint8)        #calib 03112019 CHROMA KEY
#yellow_lower=np.array([20,145,200],np.uint8)         #calib 03152019 Fundo Grafite
#yellow_upper=np.array([70,255,255],np.uint8)         #calib 03152019 Fundo Grafite
yellow_lower=np.array([20,170,160],np.uint8)         
yellow_upper=np.array([70,255,255],np.uint8)

#defining the Range of Gray color
#lower_gray = np.array([106, 47, 66],np.uint8)
#upper_gray = np.array([114, 78, 255],np.uint8)
#lower_gray = np.array([105, 80, 71],np.uint8)       #calib 01102018
#upper_gray = np.array([110, 160, 220],np.uint8)     #calib 01102018
#lower_gray = np.array([105, 100, 0],np.uint8)       #calib 31102018
#upper_gray = np.array([110, 210, 105],np.uint8)     #calib 31102018
#lower_gray = np.array([100, 100, 30],np.uint8)      #calib 05112018
#upper_gray = np.array([115, 180, 185],np.uint8)     #calib 05112018
#lower_gray = np.array([105, 105, 45],np.uint8)      #calib 11212018
#upper_gray = np.array([115, 205, 135],np.uint8)     #calib 11212018
#lower_gray = np.array([100, 100, 55],np.uint8)      #calib 19212018
#upper_gray = np.array([115, 170, 130],np.uint8)     #calib 19122018
#lower_gray = np.array([75, 20, 65],np.uint8)        #calib 26122018
#upper_gray = np.array([100, 75, 150],np.uint8)      #calib 26122018
#lower_gray = np.array([90, 10, 60],np.uint8)        #calib 26122019
#upper_gray = np.array([160, 160, 160],np.uint8)     #calib 26122019
#lower_gray = np.array([95, 0, 10],np.uint8)         #calib 25032019
#upper_gray = np.array([120, 80, 190],np.uint8)      #calib 25032019
#lower_gray = np.array([10, 60, 40],np.uint8)        #calib 03112019 CHROMA KEY 
#upper_gray = np.array([30, 100, 180],np.uint8)      #calib 03112019 CHROMA KEY  
lower_gray = np.array([0, 0, 50],np.uint8)           #calib 03112019 teste CHROMA KEY 
upper_gray = np.array([179, 75, 180],np.uint8)       #calib 03112019 teste CHROMA KEY 


#defining the Range of White color
#lower_white = np.array([61, 0, 189],np.uint8)       #calib 01102018
#upper_white = np.array([179, 100, 255],np.uint8)    #calib 01102018
#lower_white = np.array([92, 0, 240],np.uint8)       #calib 08102018
#upper_white = np.array([110, 55, 255],np.uint8)     #calib 08102018
#lower_white = np.array([75, 0, 216],np.uint8)       #calib 08102018
#upper_white = np.array([120, 60, 255],np.uint8)     #calib 08102018
#lower_white = np.array([75, 0, 200],np.uint8)       #calib 11212018
#upper_white = np.array([130, 70, 255],np.uint8)     #calib 11212018
#lower_white = np.array([0, 0, 240],np.uint8)        #calib 11212018
#upper_white = np.array([130, 15, 255],np.uint8)     #calib 11212018
#lower_white = np.array([0, 0, 190],np.uint8)        #calib 26122018
#upper_white = np.array([130, 30, 255],np.uint8)     #calib 26122018
#lower_white = np.array([0, 0, 180],np.uint8)        #calib 26122019
#upper_white = np.array([120, 30, 255],np.uint8)     #calib 26122019
#lower_white = np.array([0, 0, 130],np.uint8)        #calib 25032019
#upper_white = np.array([40, 30, 255],np.uint8)      #calib 25032019
#lower_white = np.array([0, 0, 255],np.uint8)        #calib 03112019 CHROMA KEY
#upper_white = np.array([50, 70, 255],np.uint8)      #calib 03112019 CHROMA KEY
#lower_white = np.array([0, 0, 255],np.uint8)         #calib 03152019 Fundo Grafite
#upper_white = np.array([0, 0, 255],np.uint8)         #calib 03152019 Fundo Grafite
lower_white = np.array([0, 0, 200],np.uint8)        
upper_white = np.array([55, 15, 255],np.uint8)  

#defining the Range of Green color
#lower_green = np.array([60, 100, 30],np.uint8)      #calib 01102018
#upper_green = np.array([90, 255, 115],np.uint8)     #calib 01102018
#lower_green = np.array([45, 100, 70],np.uint8)      #calib 03142019
#upper_green = np.array([70, 220, 215],np.uint8)     #calib 03142019
#lower_green = np.array([50, 50, 110],np.uint8)      #calib 03142019 liga/desl fundo preto
#upper_green = np.array([85, 190, 255],np.uint8)     #calib 03142019 liga/desl fundo preto
#lower_green = np.array([60, 85, 45],np.uint8)        #calib 03152019 Fundo Grafite
#upper_green = np.array([85, 255, 230],np.uint8)      #calib 03152019 Fundo Grafite
#lower_green = np.array([35, 70, 45],np.uint8)        #calib 29152019 Fundo Grafite
#upper_green = np.array([100, 170, 210],np.uint8)      #calib 29152019 Fundo Grafite

lower_green = np.array([70, 60, 160],np.uint8)        #calib 29152019 Fundo Grafite
upper_green = np.array([95, 240, 255],np.uint8)      #calib 29152019 Fundo Grafite


#defining the Range of Black color
lower_black = np.array([105, 80, 71],np.uint8)       #calib 01102018
upper_black = np.array([110, 160, 220],np.uint8)     #calib 01102018

print('colors inicialized')
