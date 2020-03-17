from PIL import ImageFilter

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