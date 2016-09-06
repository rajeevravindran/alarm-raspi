import pygame
from time import strftime, localtime
from sys import argv

H = int(argv[1])
M = int(argv[2])
S = int(argv[3])
file = argv[4]

while True:
    cH = int(strftime("%H",localtime()))
    cM = int(strftime("%M",localtime()))
    cS = int(strftime("%S",localtime()))
    if H == cH and M == cM and S == cS:
        break

pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue