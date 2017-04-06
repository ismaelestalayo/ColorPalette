from PIL import Image, ImageFont, ImageDraw
from colorthief import ColorThief
import sys

file_name = sys.argv[1]
print("   >mainColors.py " + sys.argv[1])



def rgb2Hex(rgb):
    r=rgb[0]
    g=rgb[1]
    b=rgb[2]
    return ('#%02x%02x%02x' % (r,g,b)).upper()

try:
    im = Image.open(file_name)

    width, length = im.size
    zz = int(length/8)
    dx = int(width*0.20)
    width += dx

    print("   >Calculando colores principales...")

    cf = ColorThief(file_name)

    colors = cf.get_palette(10)

    im2 = Image.new("RGB", (width, length), "white")
    im2.paste(im)

    print("   >Dibujando colores principales...")

    x = 0

    for j in range (5, length-5):
        for i in range (width-dx+10, width-10):
            im2.putpixel((i, j), colors[x] )

        if(j % zz == 0):
            for t in range(-5, 5):
                for tt in range(width-dx+10, width-10):
                    im2.putpixel((tt, j+t), (255, 255, 255))

            x += 1

        draw = ImageDraw.Draw(im2)
        font = ImageFont.truetype("DejaVuSans.ttf", 32)

        for i in range (0, 8):
            draw.text((width-dx+(dx*0.05), i*(length/8)+length*0.01), rgb2Hex(colors[i]), (0,  0, 0), font=font)

    im2.save("mainColors.png")
    im2.close()
    im.close()
except:
    print("   >Fallo en mainColors.py")
