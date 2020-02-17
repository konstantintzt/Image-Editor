from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename

#List of supported file formats
file_formats = ["png", "jpg"]

#Basic functions of the image editor

def get_image():
    Tk().withdraw()
    filepath = askopenfilename()
    img = Image.open(filepath)
    return img

def grayscale(im):
    im = im.convert("L")
    return im

def resize(im, new_size):
    im = im.resize(new_size)
    return im

def export(img, name, format=""):
    if format.lower() == "png":
        img.save(name + ".png")
    elif format.lower() == "jpg":
        img.save(name + ".jpg")
    else:
        img.save(name)

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
    save(img)
        

def save(img):

    save_decision = input("Would you like to save the file? (Y/N)").upper()

    if save_decision == "Y":
        user_name = input("Enter file name for export: ")

        for i in file_formats:
            if user_name.lower().endswith(i):
                export(img, user_name)
                break
            else:
                user_format = input("Enter export format: ")
                export(img, user_name, user_format)
    elif save_decision == "N":
        exit()
    else:
        print("Answer with Y or N")
        save(img)

image = get_image()

menu(image)