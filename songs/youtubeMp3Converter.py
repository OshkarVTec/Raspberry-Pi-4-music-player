from __future__ import unicode_literals
import eyed3
import youtube_dl

songs = [
'https://www.youtube.com/watch?v=bpXztWUPPFQ'
] #Links de la playlist oficial

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.',
    'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        },
        {
            'key': 'FFmpegMetadata'
        }]
   
}
for i in songs:
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([i])
        ydl.cache.remove()
