#makes a program that opens an audio in MP3 format.
import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()



