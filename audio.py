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
#####                         AUDIO V2                            #####
#####                                                             #####
#######################################################################

author__ = 'J.PAZZE'

# import the necessary packages

import time
import os
import pygame
import datetime as dt
from datetime import datetime

'''

dt = datetime.today()

print(dt)

seconds = dt.timestamp()

print(seconds)

value = 0

for seconds in range(0,2800):
        
        print(seconds)

        print("saiu")

        value += 1

        print("value", value)

'''

pygame.mixer.init()


def conta_aminoacidos(value):
        
        conta = 0

        while (conta < 3 ):
        
                dt = datetime.today()

                seconds = dt.timestamp()

                print("SEGUNDOS:",seconds)

                for seconds in range(0,3):
        
                        print("seconds", seconds)

                        print("saiu")
        
                        value += 1

                        print("value", value)

                        time.sleep(1)
                
                print("CONTOU 3")

                conta += 1


#value = 0

#conta_aminoacidos(value)

        

def audio(amino, result):
				
	if(amino == 'Cadeia Principal' ):

		print('00 Cadeia Principal \n')
		pygame.mixer.init()
		pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/aminoacidos/01_cadeia_principal.mp3")
		pygame.mixer.music.play()
		time.sleep(3)

		acuracia(result)

	elif(amino == 'Metilamina' ):

		print('01 Metilamina \n')
		pygame.mixer.init()
		pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/aminoacidos/1_metilamina.mp3")
		pygame.mixer.music.play()
		time.sleep(2)
		
		acuracia(result)
			
	elif(amino == 'Glicina' ):

		print('01 Glicina \n')
		pygame.mixer.init()
		pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/aminoacidos/1_glicina.mp3")
		pygame.mixer.music.play()
		time.sleep(2)
		
		acuracia(result)

	elif(amino == 'Alanina' ):

		print('02 Alanina \n')
		pygame.mixer.init()
		pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/aminoacidos/1_alanina.mp3")
		pygame.mixer.music.play()
		time.sleep(2)
		
		acuracia(result)

	elif(amino == 'Leucina' ):

		print('03 Leucina \n')
		pygame.mixer.init()
		pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/aminoacidos/1_leucina.mp3")
		pygame.mixer.music.play()
		time.sleep(2)
		
		acuracia(result)

	elif(amino == 'Valina' ):

		print('04 Valina \n')
		pygame.mixer.init()
		pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/aminoacidos/1_valina.mp3")
		pygame.mixer.music.play()
		time.sleep(2)

		acuracia(result)

	elif(amino == 'Isoleucina' ):

		print('05 Isoleucina \n')
		pygame.mixer.init()
		pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/aminoacidos/1_isoleucina.mp3")
		pygame.mixer.music.play()
		time.sleep(2)

		acuracia(result)

	elif(amino == 'Prolina' ):

		print('06 Prolina \n')
		pygame.mixer.init()
		pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/aminoacidos/1_prolina.mp3")
		pygame.mixer.music.play()
		time.sleep(2)

		acuracia(result)

	elif(amino == 'Fenilalanina' ):

		print('07 Fenilalanina \n')
		pygame.mixer.init()
		pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/aminoacidos/1_fenilalanina.mp3")
		pygame.mixer.music.play()
		time.sleep(2)

		acuracia(result)

	elif(amino == 'Serina' ):

		print('08 Serina \n')
		pygame.mixer.init()
		pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/aminoacidos/1_serina.mp3")
		pygame.mixer.music.play()
		time.sleep(2)

		acuracia(result)

	elif(amino == 'Treonina' ):

		print('09 Treonina \n')
		pygame.mixer.init()
		pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/aminoacidos/1_treonina.mp3")
		pygame.mixer.music.play()
		time.sleep(2)

		acuracia(result)

	elif(amino == 'Cisteina' ):

		print('10 Cisteina \n')
		pygame.mixer.init()
		pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/aminoacidos/1_cisteina.mp3")
		pygame.mixer.music.play()
		time.sleep(2)

		acuracia(result)

	elif(amino == 'Tirosina' ):

		print('11 Tirosina \n')
		pygame.mixer.init()
		pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/aminoacidos/1_tirosina.mp3")
		pygame.mixer.music.play()
		time.sleep(2)

		acuracia(result)

	elif(amino == 'Asparagina' ):

		print('12 Asparagina \n')
		pygame.mixer.init()
		pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/aminoacidos/1_asparagina.mp3")
		pygame.mixer.music.play()
		time.sleep(2)

		acuracia(result)

	elif(amino == 'Glutamina' ):

		print('13 Glutamina \n')
		pygame.mixer.init()
		pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/aminoacidos/1_glutamina.mp3")
		pygame.mixer.music.play()
		time.sleep(2)

		acuracia(result)

	elif(amino == 'Aspartato' ):

		print('14 Aspartato \n')
		pygame.mixer.init()
		pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/aminoacidos/1_aspartato.mp3")
		pygame.mixer.music.play()
		time.sleep(2)

		acuracia(result)

	elif(amino == 'Glutamato' ):

		print('15 Glutamato \n')
		pygame.mixer.init()
		pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/aminoacidos/1_glutamato.mp3")
		pygame.mixer.music.play()
		time.sleep(2)

		acuracia(result)

	elif(amino == 'Arginina' ):

		print('16 Arginina \n')
		pygame.mixer.init()
		pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/aminoacidos/1_arginina.mp3")
		pygame.mixer.music.play()
		time.sleep(2)

		acuracia(result)

	elif(amino == 'Lisina' ):

		print('17 Lisina \n')
		pygame.mixer.init()
		pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/aminoacidos/1_lisina.mp3")
		pygame.mixer.music.play()
		time.sleep(2)

		acuracia(result)

	elif(amino == 'Histidina' ):

		print('18 Histidina \n')
		pygame.mixer.init()
		pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/aminoacidos/1_histidina.mp3")
		pygame.mixer.music.play()
		time.sleep(2)

		acuracia(result)

	elif(amino == 'Triptofano' ):

		print('19 Triptofano \n')
		pygame.mixer.init()
		pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/aminoacidos/1_triptofano.mp3")
		pygame.mixer.music.play()
		time.sleep(2)

		acuracia(result)

	elif(amino == 'Metionina' ):

		print('20 Metionina \n')
		pygame.mixer.init()
		pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/aminoacidos/1_metionina.mp3")
		pygame.mixer.music.play()
		time.sleep(2)

		acuracia(result)

	elif(amino == 'Agrupamento_Amina' ):

		print('21 Agrupamento Amina \n')
		pygame.mixer.init()
		pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/1_amina.mp3")
		pygame.mixer.music.play()
		time.sleep(3)

		acuracia(result)

	elif(amino == 'Agrupamento_carboxilico' ):

		print('22 Agrupamento Carboxilico \n')
		pygame.mixer.init()
		pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/1_carboxilico.mp3")
		pygame.mixer.music.play()
		time.sleep(3)

		acuracia(result)

	elif(amino == 'Molecula_agua' ):

		print('23 Molecula_agua \n')
		pygame.mixer.init()
		pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/1_agua.mp3")
		pygame.mixer.music.play()
		time.sleep(3)

		acuracia(result)

def acuracia(result):
	
	if (result == 100):
								
		pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/100_acuracia.mp3")
		pygame.mixer.music.play()

	elif (result >= 90 and result <99 ):
												
		pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/90_acuracia.mp3")
		pygame.mixer.music.play()

	elif (result >= 80 and result <89):
												
		pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/80_acuracia.mp3")
		pygame.mixer.music.play()

	elif (result >= 70 and result <79):
												
		pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/70_acuracia.mp3")
		pygame.mixer.music.play()

	elif (result >= 60 and result <69):
												
		pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/60_acuracia.mp3")
		pygame.mixer.music.play()

	elif (result <= 59):
												
		pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/acuracia_inferior.mp3")
		pygame.mixer.music.play()

def audio_info(aud):

	if (aud == 1):

		print("\nBoas vindas e informacoes basicas")
								
		pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/bem_vindo.mp3")
		pygame.mixer.music.play()

		time.sleep(3)

		pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/info_1.mp3")
		pygame.mixer.music.play()

		time.sleep(8)

		pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/info_2.mp3")
		pygame.mixer.music.play()

		time.sleep(12)

		print("Lendo botao...")

		print ("\nPasso a passo")
		pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/info_3.mp3")
		pygame.mixer.music.play()
		time.sleep(14)

		pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/info_4.mp3")
		pygame.mixer.music.play()
		time.sleep(12)

def botton_control(botao_1, botao_2):

		if (botao_1 == 1) :
					
			print("\nInicializa direto")

		elif (botao_2 == 1):
					
			print ("\nPasso a passo")
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/info_3.mp3")
			pygame.mixer.music.play()
			time.sleep(14)

			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/info_4.mp3")
			pygame.mixer.music.play()
			time.sleep(12)

def aguarda_key(key, pic_r, pic_b, pic_y, pic_v, pic_w, pwm38, pwm40, amino, result):

	if key == ord("t"):
		print("\n###### Resumo global ######\n")
		print('Nitrogen',pic_b)
		print('Sulfur',pic_y)
		print('Carbon',pic_v)
		print('Hidrogen',pic_w)
		print("\n###### Resumo globaL ######\n")

		audio(amino, result) # chama funcao audio

	if key == ord("w"):
				
		audio(amino, result) # chama funcao audio
						
	if key == ord("l"):
				
		print('ldr_1 : ' , ldr_1(LDR_1))
		print('ldr_2 : ' , ldr_2(LDR_2))
		print('ldr_3 : ' , ldr_3(LDR_3))
		print('\n')

	if key == ord("1"):
				
		print('DC 38 ON')
		pwm38.start(0)

	if key == ord("2"):
				
		print('DC 38 OFF')
		pwm38.start(100)

	if key == ord("3"):
				
		print('DC 40 ON')
		pwm40.start(0)

	if key == ord("4"):
				
		print('DC 40 OFF')
		pwm40.start(100)

	if key == ord("o"):
				
		print("Oxygen:" +str(pic_r))
		
		if pic_r == 1:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/1_oxigenio.mp3")
			pygame.mixer.music.play()
			
		elif pic_r == 2:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/2_oxigenio.mp3")
			pygame.mixer.music.play()
			
		elif pic_r == 3:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/3_oxigenio.mp3")
			pygame.mixer.music.play()
			
		elif pic_r == 4:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/4_oxigenio.mp3")
			pygame.mixer.music.play()
			
		elif pic_r == 5:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/5_oxigenio.mp3")
			pygame.mixer.music.play()

		else:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/fora_intervalo.mp3")
			pygame.mixer.music.play()
		
		'''
		if pic_r == 1:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Demolidor/Testes/audio/1_oxygen.mp3")
			pygame.mixer.music.play()
		elif pic_r == 2:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Demolidor/Testes/audio/2_oxygen.mp3")
			pygame.mixer.music.play()
		elif pic_r == 3:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Demolidor/Testes/audio/3_oxygen.mp3")
			pygame.mixer.music.play()
		elif pic_r == 4:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Demolidor/Testes/audio/4_oxygen.mp3")
			pygame.mixer.music.play()
		elif pic_r == 5:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Demolidor/Testes/audio/5_oxygen.mp3")
			pygame.mixer.music.play()
		'''
	if key == ord("n"):

		print("Nitrogen:" +str(pic_b))
		
		if pic_b == 1:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/1_nitrogenio.mp3")
			pygame.mixer.music.play()
			
		elif pic_b == 2:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/2_nitrogenio.mp3")
			pygame.mixer.music.play()
			
		elif pic_b == 3:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/3_nitrogenio.mp3")
			pygame.mixer.music.play()
			
		elif pic_b == 4:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/4_nitrogenio.mp3")
			pygame.mixer.music.play()
			
		elif pic_b == 5:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/5_nitrogenio.mp3")
			pygame.mixer.music.play()
		
		else:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/fora_intervalo.mp3")
			pygame.mixer.music.play()
		
		'''
		if pic_b == 1:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Demolidor/Testes/audio/1_nitrogen.mp3")
			pygame.mixer.music.play()
		elif pic_b == 2:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Demolidor/Testes/audio/2_nitrogen.mp3")
			pygame.mixer.music.play()
		elif pic_b == 3:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Demolidor/Testes/audio/3_nitrogen.mp3")
			pygame.mixer.music.play()
		elif pic_b == 4:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Demolidor/Testes/audio/4_nitrogen.mp3")
			pygame.mixer.music.play()
		elif pic_b == 5:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Demolidor/Testes/audio/5_nitrogen.mp3")
			pygame.mixer.music.play()
		'''

	if key == ord("s"):

		print("Sulfur:" +str(pic_y))
				
		if pic_y == 1:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/1_enxofre.mp3")
			pygame.mixer.music.play()
			
		elif pic_y == 2:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/2_enxofre.mp3")
			pygame.mixer.music.play()
			
		elif pic_y == 3:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/3_enxofre.mp3")
			pygame.mixer.music.play()
			
		elif pic_y == 4:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/4_enxofre.mp3")
			pygame.mixer.music.play()
			
		elif pic_y == 5:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/5_enxofre.mp3")
			pygame.mixer.music.play()

		else:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/fora_intervalo.mp3")
			pygame.mixer.music.play()
		
		'''
		
		if pic_y == 1:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Demolidor/Testes/audio/1_sulfur.mp3")
			pygame.mixer.music.play()
		elif pic_y == 2:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Demolidor/Testes/audio/2_sulfur.mp3")
			pygame.mixer.music.play()
		elif pic_y == 3:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Demolidor/Testes/audio/3_sulfur.mp3")
			pygame.mixer.music.play()
		elif pic_y == 4:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Demolidor/Testes/audio/4_sulfur.mp3")
			pygame.mixer.music.play()
		elif pic_y == 5:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Demolidor/Testes/audio/5_sulfur.smp3")
			pygame.mixer.music.play()
		'''

	if key == ord("c"):

		print("Carbon:" +str(pic_v))
				
		if pic_v == 1:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/1_carbono.mp3")
			pygame.mixer.music.play()
			
		elif pic_v == 2:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/2_carbono.mp3")
			pygame.mixer.music.play()
			
		elif pic_v == 3:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/3_carbono.mp3")
			pygame.mixer.music.play()
			
		elif pic_v == 4:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/4_carbono.mp3")
			pygame.mixer.music.play()
			
		elif pic_v == 5:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/5_carbono.mp3")
			pygame.mixer.music.play()

		else:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/fora_intervalo.mp3")
			pygame.mixer.music.play()
		
		'''

		if pic_g == 1:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Demolidor/Testes/audio/1_carbon.mp3")
			pygame.mixer.music.play()
		elif pic_g == 2:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Demolidor/Testes/audio/2_carbon.mp3")
			pygame.mixer.music.play()
		elif pic_g == 3:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Demolidor/Testes/audio/3_carbon.mp3")
			pygame.mixer.music.play()
		elif pic_g == 4:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Demolidor/Testes/audio/4_carbon.mp3")
			pygame.mixer.music.play()
		elif pic_g == 5:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Demolidor/Testes/audio/5_carbon.mp3")
			pygame.mixer.music.play()
		'''	

	if key == ord("h"):

		print("Hidrogen:" +str(pic_w))
				
		if pic_w == 1:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/1_hidrogenio.mp3")
			pygame.mixer.music.play()
			
		elif pic_w == 2:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/2_hidrogenio.mp3")
			pygame.mixer.music.play()
			
		elif pic_w == 3:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/3_hidrogenio.mp3")
			pygame.mixer.music.play()
			
		elif pic_w == 4:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/4_hidrogenio.mp3")
			pygame.mixer.music.play()
			
		elif pic_w == 5:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/5_hidrogenio.mp3")
			pygame.mixer.music.play()

		elif pic_w == 6:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/6_hidrogenio.mp3")
			pygame.mixer.music.play()

		elif pic_w == 7:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/7_hidrogenio.mp3")
			pygame.mixer.music.play()

		elif pic_w == 8:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/8_hidrogenio.mp3")
			pygame.mixer.music.play()

		elif pic_w == 9:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/9_hidrogenio.mp3")
			pygame.mixer.music.play()

		elif pic_w == 10:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/10_hidrogenio.mp3")
			pygame.mixer.music.play()

		elif pic_w == 11:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/11_hidrogenio.mp3")
			pygame.mixer.music.play()

		elif pic_w == 12:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/12_hidrogenio.mp3")
			pygame.mixer.music.play()

		elif pic_w == 13:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/13_hidrogenio.mp3")
			pygame.mixer.music.play()

		elif pic_w == 14:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/14_hidrogenio.mp3")
			pygame.mixer.music.play()

		elif pic_w == 15:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/15_hidrogenio.mp3")
			pygame.mixer.music.play()
			
		else:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Documents/Demolidor/Testes/audio/fora_intervalo.mp3")
			pygame.mixer.music.play()
			
		'''
		if pic_w == 1:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Demolidor/Testes/audio/1_hydrogen.mp3")
			pygame.mixer.music.play()
		elif pic_w == 2:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Demolidor/Testes/audio/2_hydrogen.mp3")
			pygame.mixer.music.play()
		elif pic_w == 3:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Demolidor/Testes/audio/3_hydrogen.mp3")
			pygame.mixer.music.play()
		elif pic_w == 4:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Demolidor/Testes/audio/4_hydrogen.mp3")
			pygame.mixer.music.play()
		elif pic_w == 5:
			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Demolidor/Testes/audio/5_hydrogen.mp3")
			pygame.mixer.music.play()
		'''


		


print("audio inicialized")

