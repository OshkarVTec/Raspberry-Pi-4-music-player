import os 

def getImages():
    currentPath = os.path.dirname(os.path.abspath(__file__)); # Absolute dir the script is in
    filepath = "Album_images/"; 
    directory = os.listdir(os.path.join(currentPath, filepath))
    images =  []
    for fi in directory:
        if fi.endswith('.jpg'):
            images.append(os.path.join(currentPath, filepath, fi))
    return images

def getSongs():
    currentPath = os.path.dirname(os.path.abspath(__file__)); # Absolute dir the script is in
    filepath = "songs/"
    directory = os.listdir(os.path.join(currentPath, filepath))
    songs =  []
    for fi in directory:
        if fi.endswith('.mp3'):
            songs.append(os.path.join(currentPath, filepath, fi))
    return songs
