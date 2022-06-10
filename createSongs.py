import os 

def getImages():
    currentPath = os.path.dirname(os.path.abspath(__file__)); # Absolute dir the script is in
    filepath = "Album_images/"; 
    directory = os.listdir(os.path.join(currentPath, filepath));
    songs = [ fi for fi in directory if fi.endswith(('.jpg')) ];
    return songs

def getSongs():
    currentPath = os.path.dirname(os.path.abspath(__file__)); # Absolute dir the script is in
    filepath = "songs/"
    directory = os.listdir(os.path.join(currentPath, filepath));\
    songs = [ fi for fi in directory if fi.endswith(('.mp3')) ];
    return songs
