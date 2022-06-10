

import os, pygame
import random
import Functions
import createSongs
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
        self.isPaused = False
        self.setupUi(self)
        

        self.button_FF.clicked.connect(self.nextPressed(False))
        self.button_Play.clicked.connect(self.playPressed(False))
        self.button_Random.clicked.connect(self.randomPressed(False))
        self.button_Repeat.clicked.connect(self.repeatPressed(False))
        self.button_Rewind.clicked.connect(self.rewindPressed(False))

    def nextPressed(self, gui):
        self.current =+ 1
        self.playPressed(False)
        self.button_Play.setChecked(True)
    def playPressed(self, gui):
        self.isPaused = Functions.play(self.songs[self.current], self.isPaused)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Ui_Dialog()
    window.show()
    app.exec_()
