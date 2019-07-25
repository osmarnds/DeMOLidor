#######################################################################
#####                                                             #####
#####                     Jeferson S. Pazze                       #####
#####                jeferson.pazze@acad.pucrs.br                 #####
#####                       01/16/2019                            #####
#####                      LABIO - PUCRS                          #####
#####                        Histogram                            #####
#####                                                             #####
#######################################################################

# import the necessary packages
import numpy as np
import matplotlib.pyplot as plt
import imutils
import argparse

######################### historogram ####################
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
    ax.set_xlabel('Bin')
    ax.set_ylabel('Frequency')
    
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
######################### end historogram ####################

print('histogram inicialized')
