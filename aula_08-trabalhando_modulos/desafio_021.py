import pygame
'''
Faça um programa em Python que abra e reproduza o áudio de arquivo em MP3.
'''
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('fdgp.mp3') #incluir um arquivo MP3 aqui.
pygame.mixer.music.play()
# pygame.event.wait()
# input('Agora você escuta?')
while(pygame.mixer.music.get_busy()): pass
