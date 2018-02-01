#!/usr/bin/python

import serial
import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption('Change Color!')

s = serial.Serial("/dev/ttyACM1")

while(True):
	try:
		l = s.readline()
		x = l.rstrip().split(",")
		
		rgb = [ int(val) for val in x]
		print(rgb)
		DISPLAYSURF.fill(rgb) 
		pygame.display.update()
	except ValueError:
		pass
	



