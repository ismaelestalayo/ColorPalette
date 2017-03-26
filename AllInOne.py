from PIL import Image, ImageFont, ImageDraw
import random

import tkinter
from tkinter.filedialog import askopenfilename

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

###############################################################################
def superRandomPalette():

    im = Image.new("RGB", (900, 600), "black");
    width, length = im.size

    def rgbInit(x):
        if(x >= 210):
            x = random.randint(-43, -32)
        elif(x > 170):
            x = random.randint(-32, -25)
        elif(x > 140):
            x = random.randint(-25, -15)
        elif(x > 110):
            x = random.randint(15, 25)
        elif(x > 80):
            x = random.randint(25, 32)
        elif(x >= 0):
            x = random.randint(32, 43)
        return x

    r = random.randint(0, 255)
    dr = rgbInit(r)
    g = random.randint(0, 255)
    dg = rgbInit(g)
    b = random.randint(0, 255)
    db = rgbInit(b)

    x = 0
    for i in range (width):
        for j in range (length):
            im.putpixel((i, j), (r, g, b))

        if (i % 150 == 0):
            r += dr
            g += dg
            b += db


    colors = im.getcolors()
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("arial.ttf", 16)


    for i in range(0, 6):
        color = '#%02x%02x%02x' % colors[i][1]
        draw.text((35+(i*150), length-80), str( colors[i][1]), (0, 0, 0), font=font)
        draw.text((50+(i*150), length-30), rgb2Hex( colors[i][1]), (0, 0, 0), font=font)
        i += 1

    im.show()

def randomPalette():

    r = random.choice( [ random.choice(range(0, 110)), random.choice(range(160, 255)) ] )
    g = random.choice( [ random.choice(range(0, 110)), random.choice(range(160, 255)) ] )
    b = random.choice( [ random.choice(range(0, 110)), random.choice(range(160, 255)) ] )

    dr = randomRGB(r)
    dg = randomRGB(g)
    db = randomRGB(b)

    print(r, g, b)
    print(dr, dg, db)

    im = Image.new("RGB", (900, 600), "black");
    width, length = im.size

    #########################################
    x = 0
    for i in range (width):
        for j in range (length):
            im.putpixel((i, j), (r, g, b))

        if (i % 150 == 0):
            r -= dr
            g -= dg
            b -= db


    colors = im.getcolors()
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("arial.ttf", 16)



    for i in range(0, 6):
        color = '#%02x%02x%02x' % colors[i][1]
        #draw.text((35+(i*150), length-80), str( im.getpixel((150*i, 0)) ), (0, 0, 0), font=font)
        draw.text((50+(i*150), length-30), rgb2Hex( im.getpixel((150*i, 0)) ), (0, 0, 0), font=font)
        i += 1

    im.show()

def randomGradient():

    r0 = random.choice( [ random.choice(range(0, 110)), random.choice(range(160, 255)) ] )
    g0 = random.choice( [ random.choice(range(0, 110)), random.choice(range(160, 255)) ] )
    b0 = random.choice( [ random.choice(range(0, 110)), random.choice(range(160, 255)) ] )

    r1 = r0 - 5*randomRGB(r0)
    g1 = g0 - 5*randomRGB(g0)
    b1 = b0 - 5*randomRGB(b0)

    im = Image.new("RGB", (750, 1334), "black");
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
    #im.save("gradiente.jpg")

def colorsHist():
    root = tkinter.Tk()
    root.withdraw()
    fileName = tkinter.filedialog.askopenfilename()
    im = Image.open(fileName)
    width, length = im.size
    length += 120

    colors = im.getcolors(1080*720)

    im2 = Image.new("RGB", (width, length), "white")
    im2.paste(im)

    z = 0
    for i in range (10, width-10):
        for j in range (length-110, length-10):
            im2.putpixel((i, j), colors[z][1] )

        if(i % 150 == 0):
            for t in range(-5, 5):
                for tt in range(length-110, length-10):
                    im2.putpixel((i+t, tt), (255, 255, 255))
            z += 1

    im2.show()

    #for idx, c in enumerate(colors):
    #    plt.bar(idx, c[0], color = rgb2Hex(c[1]), edgecolor = rgb2Hex(c[1]))
    #plt.show()

execfile("randomPalette.py")
###############################################################################
###############################################################################
###############################################################################


#superRandomPalette()
randomPalette()
#randomGradient()
#colorsHist()
