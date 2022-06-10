

import os, pygame
import random
import Functions
import createSongs
import retoOLED
#import retoUART
#import retoOLED

from PyQt5 import QtGui, QtCore
from Spotify import *

from pygame import mixer

pygame.mixer.init()
if not pygame.font: print ('Warning, fonts disabled')
if not pygame.mixer: print ('Warning, sound disabled')


class Ui_Dialog(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.songs = createSongs.getSongs()
        self.current = 0
        #Flags 
        self.random = False
        self.repeat = False
        self.isPaused = False
        self.setupUi(self)
        
        self.button_FF.clicked.connect(lambda : self.nextPressed(False))
        self.button_Play.clicked.connect(lambda :self.playPressed(False))
        self.button_Random.clicked.connect(lambda : self.randomPressed(False))
        self.button_Repeat.clicked.connect(lambda : self.repeatPressed(False))
        self.button_Rewind.clicked.connect(lambda : self.rewindPressed(False))

    def nextPressed(self, gui):
        if self.random == True:
            self.current = random.randint(0,99)
        else: 
            self.current += 1
        self.button_Play.setChecked(True)
        retoOLED.nextOled()
        self.isPaused = Functions.play(self.songs[self.current], self.isPaused)

    def playPressed(self, gui):
        if self.button_Play.isChecked() == False:
            retoOLED.playOled()
            self.isPaused = Functions.play(self.songs[self.current], self.isPaused)
        else:
            retoOLED.pauseOled()
            self.isPaused = Functions.pause(self.isPaused)
        
    def randomPressed(self, gui):
        retoOLED.randomOled()
        self.random = not self.random
        self.current = random.randint(0,99)

    def repeatPressed(self, gui):
        retoOLED.repeatOled()
        self.repeat = not self.repeat
        
    def rewindPressed(self, gui):
        if self.random == True:
            self.current = random.randint(0,99)
        else: 
            self.current -= 1
        self.button_Play.setChecked(True)
        retoOLED.nextOled()
        self.isPaused = Functions.play(self.songs[self.current], self.isPaused)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Ui_Dialog()
    window.show()
    app.exec_()
