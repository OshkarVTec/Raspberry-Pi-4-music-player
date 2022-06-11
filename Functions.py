import eyed3
import os, pygame
import re
import random
from PyQt5 import QtGui, QtCore

from pygame import mixer
MUSIC_END = pygame.USEREVENT+1

pygame.mixer.init()
pygame.init()

if not pygame.font: print ('Warning, fonts disabled')
if not pygame.mixer: print ('Warning, sound disabled')

def play(songPath, isPaused, images):
   audiofile = eyed3.load(songPath)

   for x in range (len(images)):
      if (str(audiofile.tag.album)+".jpg") == images[x]:
         albumCover = images[x]
   songTitle = str(audiofile.tag.title)
   songArtist = str(audiofile.tag.artist)
   if (isPaused):
      pygame.mixer.music.unpause()
   else:
      pygame.mixer.music.load(songPath)
      pygame.mixer.music.play()
      pygame.mixer.music.set_endevent(MUSIC_END)
   isPaused = False
   return isPaused, songTitle, songArtist, albumCover

def pause(isPaused):
   pygame.mixer.music.pause()
   isPaused = True
   return isPaused

def checkMusicEnd():
   for event in pygame.event.get():
            if event.type == MUSIC_END:
                return True
            return False









