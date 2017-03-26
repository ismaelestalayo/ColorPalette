from PIL import Image, ImageFont, ImageDraw

import random

def rgb2Hex(rgb):
    r=rgb[0]
    g=rgb[1]
    b=rgb[2]

    return '#%02x%02x%02x' % (r,g,b)

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

im = Image.new("RGB", (600, 400), "black");
width, length = im.size

#########################################

x = 0
for i in range (width):
    for j in range (length):
        im.putpixel((i, j), (r, g, b))
    if (i % 100 == 0):
        r -= dr
        g -= dg
        b -= db
	print(i/100)

colors = im.getcolors()
draw = ImageDraw.Draw(im)

for i in range(0, 6):
    color = '#%02x%02x%02x' % colors[i][1]
    draw.text((25+(i*100), length-30), rgb2Hex( im.getpixel((100*i, 0)) ), (0, 0, 0))
    i += 1


im.save("randomPalette.jpg")
