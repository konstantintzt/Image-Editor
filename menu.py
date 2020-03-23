from PIL import Image, ImageTk
from tkinter import Tk, Label, Button, Canvas, Toplevel
from tkinter.filedialog import askopenfilename
import basic_functions
from export import export

img = None
app_title = "Broksy Image Editor v0.1"
root = None
tk_im = None

# Tkinter dialog to chose file
def get_image():
    Tk().withdraw()
    filepath = askopenfilename()
    img = Image.open(filepath)
    tk_im = ImageTk.PhotoImage(img)
    return img, tk_im

def display_image(im, canvas):

    global tk_im
    global image_window
    canvas.pack(side="top",fill="both",expand="yes")
    canvas.create_image(im.size[0]/2+10, im.size[1]/2+10, image=tk_im)


def grayscale():

    global tk_im
    global img
    global canvas
    img = basic_functions.grayscale(img)
    tk_im = ImageTk.PhotoImage(img)
    canvas.delete("all")
    display_image(img, canvas)

def resize():
    global tk_im
    global img
    global canvas
    img = basic_functions.resize(img)
    tk_im = ImageTk.PhotoImage(img)
    canvas.delete("all")
    display_image(img, canvas)

def gaussian_blur():
    global tk_im
    global img
    global canvas
    img = basic_functions.gaussianBlur(img)
    tk_im = ImageTk.PhotoImage(img)
    canvas.delete("all")
    display_image(img, canvas)

def invert_colors():

    global tk_im
    global img
    global canvas
    img = basic_functions.invertColors(img)
    tk_im = ImageTk.PhotoImage(img)
    canvas.delete("all")
    display_image(img, canvas)

def color_to_transparency():
    global tk_im
    global img
    global canvas
    img = basic_functions.colorToTransparency(img)
    tk_im = ImageTk.PhotoImage(img)
    canvas.delete("all")
    display_image(img, canvas)


root = Tk()
root.geometry("200x200")
root.title(app_title)

button = Button(master=root, command=grayscale, text="Grayscale")
button.pack()
button = Button(master=root, command=resize, text="Resize")
button.pack()
button = Button(master=root, command=gaussian_blur, text="Gaussian blur")
button.pack()
button = Button(master=root, command=invert_colors, text="Color inversion")
button.pack()
button = Button(master=root, command=color_to_transparency, text="Color to transparency")
button.pack()
button = Button(master=root, command= lambda: export(img), text="Save")
button.pack()

# Variables for PIL image and image for Tkinter canvas
img,tk_im = get_image()

image_window = Toplevel()
image_window.title(app_title)
image_window.geometry(str(img.size[0]+20)+"x"+str(img.size[1]+20))
canvas = Canvas(master=image_window)
display_image(img, canvas)

root.mainloop()