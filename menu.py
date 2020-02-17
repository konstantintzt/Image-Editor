from PIL import Image
from tkinter import Tk
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
    print("Welcome to Broksy Image Editor v1.0!\nPlease chose a mode from the list below:\n\n1: Grayscale\n2: Resize")
    user_mode = input()
    if user_mode == "1":
        print("Grayscale mode")
        img = grayscale(img)
    elif user_mode == "2":
        print("Resize mode")
        print("Enter new dimensions")
        x = int(input("X: "))
        y = int(input("Y: "))
        img = resize(img, (x,y))
    img.show()
    export(img)

image = get_image()
menu(image)