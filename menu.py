from PIL import Image, ImageTk
from tkinter import Tk, Label, Button, Canvas
from tkinter.filedialog import askopenfilename
from basic_functions import *
from export import export

img = None
app_title = "Broksy Image Editor v0.1"


# Tkinter dialog to chose file
def get_image(ok):
    global img
    Tk().withdraw()
    filepath = askopenfilename()
    img = Image.open(filepath)
    ok.quit()
    ok.destroy()

# Terminal menu
def terminal_menu():
    #img = get_image()
    global img
    print("Welcome to Broksy Image Editor v1.0!\nPlease chose a mode from the list below:\n\n1: Grayscale\n2: Resize\n3: Gaussian blur\n4: Color inversion\n5: Color to transparency")
    user_mode = input()
    if user_mode == "1":
        print("Grayscale mode")
        img = grayscale(img)
    elif user_mode == "2":
        print("Resize mode")
        img = resize(img)
    elif user_mode == "3":
        print("Gaussian blur mode")
        img = gaussianBlur(img)
    elif user_mode == "4":
        print("Color inversion mode")
        img = invertColors(img)
    elif user_mode == "5":
        print("Color to transparency mode")
        img = colorToTransparency(img)
    else:
        print("Invalid mode!")
        exit()
    img.show()
    export(img)
    
def image_selection_menu():

    root = Tk()
    root.geometry('500x500')
    root.title(app_title)

    image_button = Button(root, command= lambda: get_image(root), font="Arial", text="Open image")
    image_button.pack()
    root.mainloop()

def image_actions_menu(im):

    root = Tk()
    root.geometry(str(im.size[0]+20)+"x"+str(im.size[1]+20))
    root.resizable(False, False)
    root.title(app_title)

    im_tkinter = ImageTk.PhotoImage(im)

    canvas = Canvas()
    canvas.pack()
    canvas.create_image(im.size[0]/2+10, im.size[1]/2+10, image=im_tkinter,)

    root.mainloop()

image_selection_menu()
image_actions_menu(img)
#terminal_menu()
