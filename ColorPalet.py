from PIL import Image, ImageFont, ImageDraw
import random
from matplotlib import pyplot as plt

import tkinter
from tkinter.filedialog import askopenfilename

def rgb2Hex(rgb):
    r=rgb[0]
    g=rgb[1]
    b=rgb[2]
    return '#%02x%02x%02x' % (r,g,b)

def rgbInit(x):
    if(x >= 210):
        x = random.randint(-43, -32)
    elif(x > 170):
        x = random.randint(-32, -25)
    elif(x > 140):
        x = random.randint(-25, 0)
    elif(x > 110):
        x = random.randint(0, 25)
    elif(x > 80):
        x = random.randint(25, 32)
    elif(x >= 0):
        x = random.randint(32, 43)
    return x

def main():

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
        draw.text((50+(i*150), length-20), rgb2Hex( colors[i][1]), (0, 0, 0), font=font)
        i += 1

    im.show()

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


###############################################################################
im = Image.new("RGB", (900, 500), "black");
width, length = im.size

#main()
colorsHist()


'''
root = tkinter.Tk()
root.withdraw()
fileName = tkinter.filedialog.askopenfilename()
jpg = Image.open(fileName)
jpg.show()
'''
