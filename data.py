#######################################################################
#####                                                             #####
#####                     Jeferson S. Pazze                       #####
#####                jeferson.pazze@acad.pucrs.br                 #####
#####                        02/04/2019                           #####
#####                      LABIO - PUCRS                          #####
#####                         DATA RNA                            #####
#####                                                             #####
#######################################################################

# import the necessary packages
import numpy as np
import matplotlib.pyplot as plt

import os
import sys
import pygame


plt.ion()

print('DATA inicialized')
print('\n')

file = open("/home/pi/Documents/Demolidor/Testes/data.txt", "r") 
texto = file.readlines()
for linha in texto :
    linha = linha.rstrip()
    print(linha)

#print("linhas", len(texto))
file.close()

#         C   H   N   O   S  Label
data = [ [2,  5,  1,  2,  0,  0],
         [3,  7,  1,  2,  0,  1],
         [6,  11, 1,  2,  0,  2],
         [5,  11, 1,  2,  0,  3],
         [6,  13, 1,  2,  0,  4],
         [5,  9,  1,  2,  0,  5],
         [9,  11, 1,  2,  0,  6],
         [3,  7,  1,  3,  1,  7],
         [4,  9,  1,  3,  0,  8],
         [3,  7,  1,  2,  1,  9],
         [9,  11, 1,  3,  0, 10],
         [4,  8,  1,  3,  0, 11],
         [6,  11, 1,  2,  0, 12],
         [4,  7,  1,  4,  0, 13],
         [5,  9,  1,  4,  0, 14],
         [6,  14, 4,  2,  0, 15],
         [6,  14, 2,  2,  0, 16],
         [6,  9,  3,  2,  0, 17],
         [11, 12, 2,  2,  0, 18],
         [5,  11, 1,  2,  1, 19],
         [1,  5,  1,  0,  0, 20]]

carbono    = [2, 3, 6,  5,  6,  5, 9,  3, 4, 3, 9,  4, 6,  4, 5, 6,  6,  6, 11, 5,  1]
hidrogenio = [5, 7, 11, 11, 13, 9, 11, 7, 9, 7, 11, 8, 11, 7, 9, 14, 14, 9, 12, 11, 5]
nitrogenio = [1, 1, 1,  1,  1,  1, 1,  1, 1, 1, 1,  1, 1,  1, 1, 4,  2,  3, 2,  1,  1]
oxigenio   = [2, 2, 2,  2,  2,  2, 2,  3, 3, 2, 3,  3, 2,  4, 4, 2,  2,  2, 2,  2,  0]
enxofre    = [0, 0, 0,  0,  0,  0, 0,  1, 0, 1, 0,  0, 0,  0, 0, 0,  0,  0, 0,  1,  0]

output     = []


#########################  RNA  ###########################

w1 = np.random.randn()
w2 = np.random.randn()
w3 = np.random.randn()
w4 = np.random.randn()
w5 = np.random.randn()
b  = np.random.randn()

m1 = 1
m2 = 1
m3 = 1
m4 = 1
m5 = 1

x=0

def NN(m1, m2, m3, m4, m5, w1, w2, w3, w4, w5, b):
    z = m1 * w1 + m2 * w2 + m3 * w3 + m4 * w4 + m5 * w5 + b
    return sigmoid(z)

def sigmoid(x):
    value = 1/(1 + np.exp(-x))
    print("value",value)
    return value

#print("value",value)

sigmoid(x)

print("NN:" , NN(m1, m2, m3, m4, m5, w1, w2, w3, w4, w5, b))

#print("sigmoid", sigmoid(x))


#########################  RNA  ###########################

mystery_flower = [4, 1, 5, 3, 2]


#def sigmoid(x):
#    return 1/(1 + np.exp(-x))


def sigmoid_p(x):
    return sigmoid(x)*(1 -sigmoid(x))

def which_flower(length, width):
    z = lenght * w1 + width * w2 + b
    pred = sigmoid(z)
    if pred < .5 :
        print('blue')
    else :
        print('red')

'''
T = np.linspace(-5, 5, 10)
Y = sigmoid(T)

T = np.linspace(-6, 6, 100)
Y = sigmoid_p(T)

plt.figure(1)

#plt.axis([0, 6, 0 ,6])
plt.grid()
plt.xlabel('x')
plt.ylabel('value')
plt.legend()
plt.title('Sigmoid')

plt.plot(T, sigmoid(T), c = 'r')
plt.plot(T, sigmoid_p(T), c = 'b')

'''

###################################### training loop  #########################################


learning_rate = 0.2
costs = []
preds = []


for i in range(15): #generations
    ri = np.random.randint(len(data))
    point = data[ri]
    
    #print(point)
    
    z = point[0] * w1 + point[1] * w2 +  point[2] * w3 + point[3] * w4 + point[4] * w5 + b
    pred = sigmoid(z)

    print('pred:', pred)

    target = point[2]
    cost = np.square(pred - target)

    print('point', point)
    print('cost', cost)


    #costs.append(cost)
    preds.append(cost)
    
    dcost_pred = 2 * (pred - target)
    dpred_dz = sigmoid_p(z)
    
    dz_dw1 = point[0]
    dz_dw2 = point[1]
    dz_dw3 = point[2]
    dz_dw4 = point[3]
    dz_dw5 = point[4]
    
    dz_db = 1

    dcost_dz = dcost_pred * dpred_dz

    dcost_dw1 = dcost_dz * dz_dw1
    dcost_dw2 = dcost_dz * dz_dw2
    dcost_dw3 = dcost_dz * dz_dw3
    dcost_dw4 = dcost_dz * dz_dw4
    dcost_dw5 = dcost_dz * dz_dw5
    
    dcost_db = dcost_dz* dz_db

    w1 = w1 - learning_rate * dcost_dw1
    w2 = w2 - learning_rate * dcost_dw2
    w3 = w3 - learning_rate * dcost_dw3
    w4 = w4 - learning_rate * dcost_dw4
    w5 = w5 - learning_rate * dcost_dw5
	
    b  =b - learning_rate * dcost_db
    
    
    if i % 100 == 0:
        
        cost_sum = 0
        
        for j in range(len(data)):
            
            point = data[ri]

            z = point[0] * w1 + point[1] * w2 +  point[2] * w3 + point[3] * w4 + point[4] * w5 + b
            pred = sigmoid(z)

            target = point[2]
            cost_sum += np.square(pred - target)
            
    costs.append(cost_sum/len(data))
		
    #print(costs)

    '''

    plt.figure(2)

    plt.plot(costs)
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('value')
    plt.legend(['costs'])
    plt.title('Costs')
    
    plt.figure(3)

    plt.plot(preds)
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('value')
    plt.legend(['preds'])
    plt.title('Preds')


for i in range(len(data)):
    point = data[i]
    ################3
    print(point)
      
    z = point[0] * w1 + point[1] * w2 +  point[2] * w3 + point[3] * w4 + point[4] * w5 + b
    pred = sigmoid(z)
    
    print("pred: {}".format(pred))
    
    
    color = "r"
    
    if point[0] > 5:
        color = "b"
        
    if point[1] > 10:
        color = "g"

    if point[2] > 5:
        color = "b"

    if point[3] > 3 :
        color = "c"

    if point[4] > 2 :
        color = "y"

    plt.figure(5)

    #plt.plot(point[0], label = 'A')
    #plt.plot(point[1], label = 'B', c = 'g')
    #plt.plot(point[2], label = 'C', c = 'r')
    #plt.plot(data[17], label = 'Histidina',  c = 'c')
    #plt.plot(data[18], label = 'Triptofano', c = 'm')
    #plt.plot(data[19], label = 'Metionina', c = 'y')
    #plt.plot(data[20], label = 'Metilamina', c = 'k')

    plt.scatter(point[0], point[1], c=color)
    
    plt.xlabel('x')
    plt.ylabel('value')
    plt.legend('data')
    plt.title('Training DATA')
    plt.grid()
    
'''
    
z1 = mystery_flower[0] * w1 + mystery_flower[1] * w2 + b
pred_final = sigmoid(z1)
print('\n')
print('pred_final:',pred_final)

pygame.mixer.init()
pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/rna.mp3")
pygame.mixer.music.play()


plt.show()
 

