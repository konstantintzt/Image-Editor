from PIL import Image, ImageTk
from tkinter import Tk, Label, Button
from tkinter.filedialog import askopenfilename
from basic_functions import *
from export import export

# Tkinter dialog to chose file
def get_image():
    Tk().withdraw()
    filepath = askopenfilename()
    img = Image.open(filepath)
    return img

# Terminal menu
def menu(img):
    print("Welcome to Broksy Image Editor v1.0!\nPlease chose a mode from the list below:\n\n1: Grayscale\n2: Resize\n3: Gaussian blur")
    user_mode = input()
    if user_mode == "1":
        print("Grayscale mode")
        img = grayscale(img)
    elif user_mode == "2":
        print("Resize mode")
        img = resize(img)
    elif user_mode == "3":
        print("Gaussian blur mode")
        radius = int(input("Enter radius: "))
        img = gaussianBlur(img, radius)
    elif user_mode == "4":
        print("TEST MODE")
        invertColors(img)

    img.show()
    export(img)

image = get_image()
menu(image)