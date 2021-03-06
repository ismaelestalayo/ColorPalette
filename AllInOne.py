from PIL import Image, ImageFont, ImageDraw
import random

from colorthief import ColorThief

import tkinter
from tkinter.filedialog import askopenfilename

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


###############################################################################
def randomPalette():

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
    font = ImageFont.truetype("arial.ttf", 32)

    for i in range(0, 6):
        draw.rectangle([(i*z, 0),(z+i*z, length)], fill=(r, g, b) )
        draw.text((80+(i*z), length-50), rgb2Hex( im.getpixel((z*i, 0)) ), (0, 0, 0), font=font)
        i += 1

        r -= dr
        g -= dg
        b -= db

    im.show()
    #im.save("randomPalette.jpg")

def randomGradient():

    r0 = random.choice( [ random.choice(range(0, 110)), random.choice(range(160, 255)) ] )
    g0 = random.choice( [ random.choice(range(0, 110)), random.choice(range(160, 255)) ] )
    b0 = random.choice( [ random.choice(range(0, 110)), random.choice(range(160, 255)) ] )
    #print(r0)
    #print(g0)
    #print(b0)
    r1 = r0 - 5*randomRGB(r0)
    g1 = g0 - 5*randomRGB(g0)
    b1 = b0 - 5*randomRGB(b0)
    #print(r1)
    #print(g1)
    #print(b1)

    im = Image.new("RGB", (600, 600), "black");
    width, length = im.size

    r = r0
    g = g0
    b = b0
    for i in range (width):
        for j in range (length):
            im.putpixel((i, j), ( int(r), int(g), int(b) ))

        r -= (r0-r1)/width
        g -= (g0-g1)/width
        b -= (b0-b1)/width

    im.show()
    #im.save("randomGradient.jpg")

def mainColors():
    root = tkinter.Tk()
    root.withdraw()
    fileName = tkinter.filedialog.askopenfilename()
    im = Image.open(fileName)
    width, length = im.size

    zz = int(length/8)
    dx = int(width*0.15)
    width += dx

    #colors = im.getcolors(width*length)
    #if ((X-X1)^2 + (Y-Y1)^2 + (Z-Z1)^2) <= (Tol^2) then
    cf = ColorThief(fileName)
    colors = cf.get_palette(9)

    im2 = Image.new("RGB", (width, length), "white")
    im2.paste(im)
    draw = ImageDraw.Draw(im2)
    font = ImageFont.truetype("arial.ttf", 30)

    for i in range(0, 8):
        draw.rectangle( [(width-dx+10, i*zz), (width-10, (i+1)*zz)], fill=colors[i], outline="white")
        draw.text((width-dx+(dx*0.05), i*(length/8)+length*0.01), rgb2Hex(colors[i]), (0, 0, 0), font=font)

    im2.show()
    #im2.save("mainColors.jpg")

def test():
    root = tkinter.Tk()
    root.withdraw()
    fileName = tkinter.filedialog.askopenfilename()
    im = Image.open(fileName)
    width, length = im.size

    z = im.getcolors(width * length)
    z.sort(reverse=True)

    print(z)

    #im.show()
    #im.save("test.jpg")

###############################################################################
###############################################################################
###############################################################################

#randomPalette()
randomGradient()
#mainColors()
#test()
