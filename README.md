# Raspberry-Pi-4-music-player
This repository presents the final project of the Chip Systems Design course. The project consists of an MP3 music player implemented on Raspberry Pi. The program features a user interface developed in QtDesigner. Song information is displayed on an OLED screen, which communicates with the Raspberry Pi through I2C. The program utilizes buttons and sliders within the user interface and can also be operated using a matrix keyboard, controlled by an Arduino Uno connected to the Raspberry Pi via UART. The OLED screen provides feedback when buttons are pressed, both on the screen and the matrix keyboard. The main program is built in Python, using the VLC library as the player and incorporating eyed3 for obtaining song data.

You can view a demo of the project [here](https://youtu.be/yUWd6B4QuGk).

As an additional function, a program was developed to download MP3 files from YouTube using a playlist link or a song link, wich can be found in the file youtubeMp3Converter.py
