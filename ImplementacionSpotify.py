      #  for event in pygame.event.get():
       #     if event.type == MUSIC_END:
        #        if(not repeatFlag):
         #           pygame.mixer.music.play(songs[i])
          #      else:
           #         pygame.mixer.music.play(songs[i+1])


import os, pygame
import random
import Functions
#import retoUART
#import retoOLED

from PyQt5 import QtGui, QtCore
from Spotify import *

from pygame import mixer

pygame.mixer.init()
if not pygame.font: print ('Warning, fonts disabled')
if not pygame.mixer: print ('Warning, sound disabled')

def getSongs():
    currentPath = os.path.dirname(os.path.abspath(__file__)); # Absolute dir the script is in
    filepath = "../songs/"; # The path where the pictures are uploaded
    directory = os.listdir(os.path.join(currentPath, filepath));
    songs = [ fi for fi in directory if fi.endswith(('.mp3')) ];
    return songs;

def getImages():
    currentPath = os.path.dirname(os.path.abspath(__file__)); # Absolute dir the script is in
    filepath = "../Album_images/"; # The path where the pictures are uploaded
    directory = os.listdir(os.path.join(currentPath, filepath));
    songs = [ fi for fi in directory if fi.endswith(('.jpg')) ];
    return songs;


class Ui_Dialog(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        isRepeat = 0 ;
        self.setupUi(self)

        self.button_FF.clicked.connect(self.buttonYes)
        self.button_Play.clicked.connect(self on_click)
        self.button_Random.clicked.connect(self.buttonNo)
        self.button_Repeat.clicked.connect(Functions.repeat())
        self.button_Rewind.clicked.connect(self.buttonNo)
        

def repeat(repeatFlag):
   repeatFlag = not repeatFlag
   return repeatFlag

def random(randomFlag):
    randomFlag = not randomFlag
    return randomFlag


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Ui_Dialog()
    window.show()
    app.exec_()
