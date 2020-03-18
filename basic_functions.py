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

def gaussianBlur(im):
    radius = int(input("Enter radius: "))
    im = im.filter(ImageFilter.GaussianBlur(radius))
    return im

def invertColors(im):
    current_pixel = []

    for x in range(im.size[0]):
        for y in range(im.size[1]):
            current_pixel = list(im.getpixel((x, y)))
            #Invert colors of the pixel
            current_pixel[0] = abs(255-current_pixel[0])
            current_pixel[1] = abs(255-current_pixel[1])
            current_pixel[2] = abs(255-current_pixel[2])
            im.putpixel((x,y), tuple(current_pixel))
            
    return im

def colorToTransparency(im):

    im = im.convert("RGBA")
    
    color_to_change = tuple(map(int,input("Enter color to be changed to transparency: [R,G,B]").split(",")))
    print("Color to change is:", color_to_change)

    print(im.getpixel((20,20)))

    for x in range(im.size[0]):
        for y in range(im.size[1]):
            current_pixel = im.getpixel((x, y))
            if current_pixel[0] == color_to_change[0] and current_pixel[1] == color_to_change[1] and current_pixel[2] == color_to_change[2]:
                im.putpixel((x,y), (0,0,0,0))
    
    return im