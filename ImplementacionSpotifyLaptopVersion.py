#Diego García, Oskar Villa
#June 2022
import numbers
import eyed3
import random
import Functions
import createSongs
#import retoOLED
import time
#import retoUART

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QListWidget
from Spotify import *


class Ui_Dialog(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.songs = createSongs.getSongs()
        self.images = createSongs.getImages()
        self.songTitle = ""
        self.songAlbum = ""
        self.songArtist = ""
        self.currentSong = 0
        self.offset = 0
        self.isPaused = False
        self.timer = QtCore.QTimer(self)
        self.timer.start(100)
        self.setupUi(self)
        
        self.timer.timeout.connect(lambda: self.loop())
        self.button_FF.clicked.connect(lambda : self.nextPressed())
        self.button_Play.clicked.connect(lambda :self.playPressed(True))
        self.button_Rewind.clicked.connect(lambda : self.rewindPressed())
        self.button_Random.clicked.connect(lambda : self.randomPressed(True))
        self.button_Repeat.clicked.connect(lambda : self.repeatPressed(True))
        self.slider_MusicDuration.sliderReleased.connect(lambda : self.playTimeChanged())
        self.slider_Volume.valueChanged.connect(lambda : self.changeVolume())
        self.listWidget.itemDoubleClicked.connect(self.songChoose)

        self.listWidget.clear()
        for x in range(len(self.songs)):
            audiofile = eyed3.load(self.songs[x])
            item = "{:02d}".format(x) + " " + str(audiofile.tag.title) + " - " + str(audiofile.tag.artist)
            self.listWidget.insertItem(x, item)  

    def loop(self):
        if Functions.checkMusicEnd():
            if self.button_Repeat.isChecked():
                self.playPressed()
            else:
                self.nextPressed()
        if not self.slider_MusicDuration.isSliderDown():
            self.updateSlider()

    def changeVolume(self):
        Functions.changeVolume(self.slider_Volume.value())d
    # def returnMonitor(self):
    #     retoOLED.showInfo(self.currentSong, self.songTitle, self.songArtist, self.songAlbum)
    def songChoose(self):
        number = self.listWidget.currentRow()
        self.setSong(number)

    def setSong(self, number):
        self.changeList(QtGui.QColor(255,255,255))
        self.currentSong = number
        self.button_Play.setChecked(True)
        self.isPaused = False
        self.isPaused, self.songTitle, self.songArtist, self.songAlbum, albumCover, duration = Functions.play(self.songs[self.currentSong], self.isPaused, self.images)
        self.changeInformation(albumCover, duration)
        
    def playTimeChanged(self):
        self.offset = self.slider_MusicDuration.value()
        Functions.setPlayTime(self.offset, self.isPaused)

    def updateSlider(self):
        playTime = Functions.getPlayTime(self.isPaused)//1000 
        minutes, seconds = divmod(playTime, 60)
        self.slider_MusicDuration.setValue(playTime)
        self.label_SoundStart.setText('{:2d}:{:02d}'.format(minutes, seconds))

    def changeInformation(self, albumCover, duration):
        self.label.setStyleSheet("border-image: url(:/newPrefix/"+albumCover+");\n")
        self.label_2.setText(self.songTitle)
        self.label_3.setText(self.songArtist)
        self.slider_MusicDuration.setMaximum(duration)
        minutes, seconds = divmod(duration, 60)
        self.label_SoundEnd.setText('{:2d}:{:02d}'.format(minutes, seconds))
        self.changeList(QtGui.QColor(119,221,119))


    def changeList(self, color):
        audiofile = eyed3.load(self.songs[self.currentSong])
        item = "{:02d}".format(self.currentSong) + " " + str(audiofile.tag.title) + " - " + str(audiofile.tag.artist)
        i = QtWidgets.QListWidgetItem(item)
        self.listWidget.takeItem(self.currentSong)
        i.setForeground(color)
        self.listWidget.insertItem(self.currentSong, i)

    def nextPressed(self):
        self.changeList(QtGui.QColor(255,255,255))
        self.offset = 0
        if self.button_Random.isChecked() == True:
            self.currentSong = random.randint(0, len(self.songs) - 1)
        else: 
            self.currentSong += 1
            if self.currentSong >= len(self.songs):
                self.currentSong = 0
        self.button_Play.setChecked(True)
        #retoOLED.nextOled()
        self.isPaused = False
        self.isPaused, self.songTitle, self.songArtist, self.songAlbum, albumCover, duration = Functions.play(self.songs[self.currentSong], self.isPaused, self.images)
        self.changeInformation(albumCover, duration)
        #time.sleep(1)
        #self.returnMonitor()

    def playPressed(self, inputGui):
        if  not inputGui:
            self.button_Play.setChecked(not self.button_Play.isChecked())

        if self.button_Play.isChecked() == True:
            #retoOLED.playOled()
            self.isPaused, self.songTitle, self.songArtist, self.songAlbum, albumCover, duration = Functions.play(self.songs[self.currentSong], self.isPaused, self.images)
            self.changeInformation(albumCover, duration)
        else:
            #retoOLED.pauseOled()
            self.isPaused = Functions.pause(self.isPaused)
        #time.sleep(1)
        #self.returnMonitor()
        
    def randomPressed(self, inputGui):
        if not inputGui:
            self.button_Random.setChecked(not self.button_Random.isChecked())
        #retoOLED.randomOled()
        #time.sleep(1)
        #self.returnMonitor()

    def repeatPressed(self, inputGui):
        if not inputGui:
            self.button_Repeat.setChecked(not self.button_Repeat.isChecked())

        #retoOLED.repeatOled()
        #time.sleep(1)
        #self.returnMonitor()
        
    def rewindPressed(self):
        self.offset = 0
        songDuration = Functions.getPlayTime(self.isPaused)//1000
        if songDuration <= 5:
            self.changeList(QtGui.QColor(255,255,255))
            if self.button_Random.isChecked() == True == True:
                self.currentSong = random.randint(0, len(self.songs) - 1)
            else: 
                self.currentSong -= 1
                if self.currentSong < 0:
                    self.currentSong = len(self.songs) - 1
            self.button_Play.setChecked(True)
            #retoOLED.previousOled()
        else:
            self.currentSong = self.currentSong
        self.isPaused = False
        self.isPaused, self.songTitle, self.songArtist, self.songAlbum, albumCover, duration = Functions.play(self.songs[self.currentSong], self.isPaused, self.images)
        self.changeInformation(albumCover, duration)
        ##time.sleep(1)
        #self.returnMonitor()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Ui_Dialog()
    window.show()
    app.exec_()
