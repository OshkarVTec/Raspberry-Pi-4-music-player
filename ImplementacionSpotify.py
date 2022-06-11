#Diego García, Oskar Villa
#June 2022
import eyed3
import os, pygame
import random
import Functions
import createSongs
#import retoOLED
#import retoUART
#import retoOLED

from PyQt5 import QtGui, QtCore
from Spotify import *


class Ui_Dialog(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.songs = createSongs.getSongs()
        self.images = createSongs.getImages()
        self.currentSong = 0
        self.offset = 0
        self.isPaused = False
        self.timer = QtCore.QTimer(self)
        self.timer.start(100)
        self.setupUi(self)
        
        self.timer.timeout.connect(lambda: self.loop())
        self.button_FF.clicked.connect(lambda : self.nextPressed())
        self.button_Play.clicked.connect(lambda :self.playPressed())
        self.button_Random.clicked.connect(lambda : self.randomPressed())
        self.button_Repeat.clicked.connect(lambda : self.repeatPressed())
        self.button_Rewind.clicked.connect(lambda : self.rewindPressed())
        self.slider_MusicDuration.sliderReleased.connect(lambda : self.playTimeChanged())

        self.listWidget.clear()
        for x in range(len(self.songs)):
            pygame.mixer.music.load(self.songs[x])
            audiofile = eyed3.load(self.songs[x])
            item = "{:02d}".format(x) + " " + str(audiofile.tag.title) + " - " + str(audiofile.tag.artist)
            self.listWidget.insertItem(x, item)  

    def loop(self):
        if Functions.checkMusicEnd():
            if self.button_Repeat.isChecked():
                Functions.play(self.songs[self.currentSong], self.isPaused, self.images)
            self.nextPressed()
        
        if not self.slider_MusicDuration.isSliderDown():
            self.updateSlider()

    def playTimeChanged(self):
        self.offset = self.slider_MusicDuration.value()
        Functions.setPlayTime(self.offset, self.isPaused)


    def updateSlider(self):
        playTime = Functions.getPlayTime(self.isPaused)//1000 + self.offset
        minutes, seconds = divmod(playTime, 60)
        self.slider_MusicDuration.setValue(playTime)
        self.label_SoundStart.setText('{:2d}:{:02d}'.format(minutes, seconds))

    def changeInformation(self, songTitle, songArtist, albumCover, duration):
        self.label.setStyleSheet("border-image: url(:/newPrefix/"+albumCover+");\n")
        self.label_2.setText(songTitle)
        self.label_3.setText(songArtist)
        self.slider_MusicDuration.setMaximum(duration)
        minutes, seconds = divmod(duration, 60)
        self.label_SoundEnd.setText('{:2d}:{:02d}'.format(minutes, seconds))

    def nextPressed(self):
        self.offset = 0
        if self.button_Random.isChecked() == True:
            self.currentSong = random.randint(0,99)
        else: 
            self.currentSong += 1
            if self.currentSong >= len(self.songs):
                self.currentSong = 0
        self.button_Play.setChecked(True)
        #retoOLED.nextOled()
        self.isPaused = False
        self.isPaused, songTitle, songArtist, albumCover, duration = Functions.play(self.songs[self.currentSong], self.isPaused, self.images)
        self.changeInformation(songTitle, songArtist, albumCover, duration)

    def playPressed(self):
        if self.button_Play.isChecked() == True:
            #retoOLED.playOled()
            self.isPaused, songTitle, songArtist, albumCover, duration = Functions.play(self.songs[self.currentSong], self.isPaused, self.images)
            self.changeInformation(songTitle, songArtist, albumCover, duration)
        else:
            #retoOLED.pauseOled()
            self.isPaused = Functions.pause(self.isPaused)
        
    def randomPressed(self):
        #retoOLED.randomOled()
        self.currentSong = random.randint(0,99)

    def repeatPressed(self):
        #retoOLED.repeatOled()
        0
        
    def rewindPressed(self):
        self.offset = 0
        songDuration = Functions.getPlayTime(self.isPaused)//1000
        if songDuration <= 5:
            if self.button_Random.isChecked() == True == True:
                self.currentSong = random.randint(0,99)
            else: 
                self.currentSong -= 1
                if self.currentSong <= 0:
                    self.currentSong = len(self.songs) - 1
            self.button_Play.setChecked(True)
            #retoOLED.nextOled()
        else:
            self.currentSong = self.currentSong
        self.isPaused = False
        self.isPaused, songTitle, songArtist, albumCover, duration = Functions.play(self.songs[self.currentSong], self.isPaused, self.images)
        self.changeInformation(songTitle, songArtist, albumCover, duration)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Ui_Dialog()
    window.show()
    app.exec_()
