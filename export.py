import basic_functions
from PIL import Image
from tkinter import filedialog

filetypes = (("PNG image", "*.png"), ("JPG image", "*.jpg"), ("All files", "*.*"))

def export(img):

    file = filedialog.asksaveasfilename(defaultextension=".png", filetypes=filetypes)

    if file:
        img.save(file)
    else:
        pass