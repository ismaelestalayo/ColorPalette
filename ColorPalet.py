from PIL import Image, ImageFont, ImageDraw
import random
#from matplotlib import pyplot as plt

def rgb2Hex(rgb):
    r=rgb[0]
    g=rgb[1]
    b=rgb[2]
    return '#%02x%02x%02x' % (r,g,b)


def main():

    r = random.randint(90, 200)
    g = random.randint(90, 200)
    b = random.randint(90, 200)

    rx = random.randint(-1, 1)
    gx = random.randint(-1, 1)
    bx = random.randint(-1, 1)

    dr = random.choice( (0, 5, 10, 15, 20, 25) )
    dg = random.choice( (0, 5, 10, 15, 20, 25) )
    db = random.choice( (0, 5, 10, 15, 20, 25) )

    x = 0
    for i in range(0, width):
        for j in range(0, length):
            im.putpixel((i, j), (r+rx, g+gx, b+bx))

        if (i % 180 == 0):
            if(rx >= 0):
                rx += dr
            if(rx < 0):
                rx -= dr
            if(gx >= 0):
                gx += dg
            if(gx < 0):
                gx -= dg
            if(bx >= 0):
                bx += db
            if(bx < 0):
                bx -= db


    colors = im.getcolors()
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("arial.ttf", 16)


    for i in range(0, 5):
        color = '#%02x%02x%02x' % colors[i][1]
        draw.text((50+(i*180), length-20), rgb2Hex( colors[i][1]), (0, 0, 0), font=font)
        i += 1

    im.show()

def colorsHist():
    for idx, c in enumerate(colors):
        plt.bar(idx, c[0], color = rgb2Hex(c[1]), edgecolor = rgb2Hex(c[1]))
    plt.show()

###############################################################################
im = Image.new("RGB", (900, 512), "black");
width, length = im.size

main()
