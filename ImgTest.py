import numpy as np
import scipy.misc as smp
from PIL import Image

im = Image.open("Skyline.jpg")
pix = im.load()

#    for y in range(0, im.height):
#for x in range(0, im.width):
#        pix[x, y] = pix[x,y][0], 0, 0

#im.save("TESTT.jpg")
#print("> File saved.")

img = smp.toimage(im)
img.show()
