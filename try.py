import os 

def getSongs():
    currentPath = os.path.dirname(os.path.abspath(__file__)); # Absolute dir the script is in
    filepath = "..\songs\ "; # The path where the pictures are uploaded
    directory = os.listdir(os.path.join(currentPath, filepath));\
    songs = [ fi for fi in directory if fi.endswith(('.mp3')) ];
    return songs

songs = getSongs()
print (songs)