from PIL import Image, ImageFont, ImageDraw
import random

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

r0 = random.choice( [ random.choice(range(0, 110)), random.choice(range(160, 255)) ] )
g0 = random.choice( [ random.choice(range(0, 110)), random.choice(range(160, 255)) ] )
b0 = random.choice( [ random.choice(range(0, 110)), random.choice(range(160, 255)) ] )

r1 = r0 - 5*randomRGB(r0)
g1 = g0 - 5*randomRGB(g0)
b1 = b0 - 5*randomRGB(b0)

im = Image.new("RGB", (400, 400), "black");
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

im.save("randomGradient.jpg")
#im.show();
