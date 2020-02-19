from PIL import ImageFilter

# Basic features of the editor

def grayscale(im):
    im = im.convert("L")
    return im

def resize(im, new_size):
    im = im.resize(new_size)
    return im

def gaussianBlur(im, radius):
    im = im.filter(ImageFilter.GaussianBlur(radius))
    return im