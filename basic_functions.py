from PIL import ImageFilter
from PIL import Image

# Basic features of the editor

def grayscale(im):
    im = im.convert("L")
    return im

def resize(im):
    x = int(input("Enter new X size: "))
    y = int(input("Enter new Y size: "))
    im = im.resize((x,y))
    return im

def gaussianBlur(im, radius):
    im = im.filter(ImageFilter.GaussianBlur(radius))
    return im

def invertColors(im):

    current_pixel = []

    for x in range(im.size[0]):
        for y in range(im.size[1]):

            current_pixel = list(im.getpixel((x, y)))
            
            current_pixel[0] = abs(255-current_pixel[0])
            current_pixel[1] = abs(255-current_pixel[1])
            current_pixel[2] = abs(255-current_pixel[2])

            im.putpixel((x,y), tuple(current_pixel))

    return im