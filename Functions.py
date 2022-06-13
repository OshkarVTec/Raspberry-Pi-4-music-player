import eyed3
import vlc
from PyQt5 import QtGui, QtCore
from pygame import mixer

instance = vlc.Instance()
player = instance.media_player_new()
#events = player.event_manager()
#events.event_attach(vlc.EventType.MediaPlayerEndReached, SongFinished)

def play(songPath, isPaused, images):
   audiofile = eyed3.load(songPath)
   for x in range (len(images)):
      if (str(audiofile.tag.album)+".jpg") == images[x]:
         albumCover = images[x]
   songTitle = str(audiofile.tag.title)
   songArtist = str(audiofile.tag.artist)
   songAlbum = str(audiofile.tag.album)
   duration = int(audiofile.info.time_secs)
   if (isPaused):
      player.set_pause(0)
   else:
      media = instance.media_new_path(songPath) #Your audio file here
      player.set_media(media)
      player.play()
   isPaused = False
   
   return isPaused, songTitle, songArtist, songAlbum, albumCover, duration

def pause(isPaused):
   player.set_pause(1)
   isPaused = True
   return isPaused

def checkMusicEnd():
    if player.get_state() == 6:
       return True
    return False

def setPlayTime(playTime, isPaused):
    player.play()
    player.set_time(playTime * 1000) 
    if isPaused:
        pause(isPaused)

def getPlayTime(isPaused):
   if player.is_playing() or isPaused:
      return player.get_time()
   return 0

def changeVolume(volume):
   player.audio_set_volume(volume)










