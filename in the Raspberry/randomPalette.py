from PIL import Image, ImageFont, ImageDraw

import random

def rgb2Hex(rgb):
    r=rgb[0]
    g=rgb[1]
    b=rgb[2]

    return ('#%02x%02x%02x' % (r,g,b)).upper()

def randomRGB(x):
    if(x >= 210):
        x = random.randint(4, 41)
    elif(x > 190):
        x = random.randint(4, 38)
    elif(x > 159):
        x = random.randint(4, 33)

    elif(x > 90):
        x = random.randint(-41, -4)
    elif(x > 80):
        x = random.randint(-38, -4)
    elif(x >= 0):
        x = random.randint(-33, -4)

    return x


r = random.choice( [ random.choice(range(0, 110)), random.choice(range(160, 255)) ] )
g = random.choice( [ random.choice(range(0, 110)), random.choice(range(160, 255)) ] )
b = random.choice( [ random.choice(range(0, 110)), random.choice(range(160, 255)) ] )

dr = randomRGB(r)
dg = randomRGB(g)
db = randomRGB(b)

im = Image.new("RGB", (1920, 1080), "white");
width, length = im.size
z = width/6

#########################################
draw = ImageDraw.Draw(im)
font = ImageFont.truetype("DejaVuSans.ttf", 32)

for i in range(0, 6):
    draw.rectangle([(i*z, 0),(z+i*z, length)], fill=(r, g, b) )
    draw.text((80+(i*z), length-50), rgb2Hex( im.getpixel((z*i, 0)) ), (0, 0, 0), font=font)
    i += 1

    r -= dr
    g -= dg
    b -= db

im.save("randomPalette.jpg")
