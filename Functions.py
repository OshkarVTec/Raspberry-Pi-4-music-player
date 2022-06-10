import os, pygame
import re
import random
from PyQt5 import QtGui, QtCore

from pygame import mixer

pygame.mixer.init()
if not pygame.font: print ('Warning, fonts disabled')
if not pygame.mixer: print ('Warning, sound disabled')

def play(songPath, isPaused):
   if (isPaused):

      pygame.mixer.music.unpause()
   else:
      pygame.mixer.music.load(songPath)
      pygame.mixer.music.play()
   isPaused = False
   return isPaused

def pause(isPaused):
   pygame.mixer.music.pause()
   isPaused = True
   return isPaused











