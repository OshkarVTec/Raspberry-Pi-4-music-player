from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
from pathlib import Path
import os
i2c = busio.I2C(SCL, SDA)
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
disp.fill(0)
disp.show()
image = Image.new('1', (128, 64))
draw = ImageDraw.Draw(image)



def showInfo(name, artist, album):
    fontSize2= 15
    fontSize1= 10
    font1 = ImageFont.truetype("/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",fontSize1)
    font2 = ImageFont.truetype("/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",fontSize2)
    if len(name) > 19:
        font2 = font1
    draw.text((1, 10), name, font = font2, fill = 255)
    draw.text((1, 35), artist, font = font1, fill = 255)
    draw.text((1, 50), album, font = font1, fill = 255)
    disp.image(image)
    disp.show()
