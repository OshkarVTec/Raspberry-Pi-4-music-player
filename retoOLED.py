from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
from pathlib import Path
from demo_opts import get_device
from time import sleep
i2c = busio.I2C(SCL, SDA)
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
disp.fill(0)
disp.show()
image = Image.new('1', (128, 64))
draw = ImageDraw.Draw(image)

def showInfo(number, name, artist, album):
    disp.fill(0)
    disp.show()
    draw.rectangle(((0, 00), (128, 64)), fill="black")
    fontSize2= 15
    fontSize1= 10
    font1 = ImageFont.truetype("/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",fontSize1)
    font2 = ImageFont.truetype("/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",fontSize2)
    if len(name) > 17:
        font2 = font1
    title = str(number) + " " + name
    draw.text((1, 10), title, font = font2, fill = 255)
    draw.text((1, 35), artist, font = font1, fill = 255)
    draw.text((1, 50), album, font = font1, fill = 255)
    disp.image(image)
    disp.show()

def showNumber(number):
    disp.fill(0)
    disp.show()
    draw.rectangle(((0, 00), (128, 64)), fill="black")
    fontSize1= 40
    font1 = ImageFont.truetype("/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",fontSize1)
    draw.text((40, 10), str(number), font = font1, fill = 255)
    disp.image(image)
    disp.show()

def randomOled():
    device = get_device()
    img_path = str(Path(__file__).resolve().parent.joinpath('images', 'pi_logo.png'))
    logo = Image.open(img_path).convert("RGBA")

    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def continuosOled():
    device = get_device()
    img_path = str(Path(__file__).resolve().parent.joinpath('images', 'pi_logo.png'))
    logo = Image.open(img_path).convert("RGBA")

    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def playOled():
    device = get_device()
    img_path = str(Path(__file__).resolve().parent.joinpath('images', 'pi_logo.png'))
    logo = Image.open(img_path).convert("RGBA")

    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def pauseOled():
    device = get_device()
    img_path = str(Path(__file__).resolve().parent.joinpath('images', 'pi_logo.png'))
    logo = Image.open(img_path).convert("RGBA")

    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def nextOled():
    device = get_device()
    img_path = str(Path(__file__).resolve().parent.joinpath('images', 'pi_logo.png'))
    logo = Image.open(img_path).convert("RGBA")

    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def previousOled():
    device = get_device()
    img_path = str(Path(__file__).resolve().parent.joinpath('images', 'pi_logo.png'))
    logo = Image.open(img_path).convert("RGBA")

    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

