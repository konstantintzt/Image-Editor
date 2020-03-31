from PIL import Image, ImageTk
from tkinter import Tk, Label, Button, Canvas, Toplevel, simpledialog
from tkinter.filedialog import askopenfilename
import basic_functions
from export import export

img = None
app_title = "Broksy Image Editor v0.25"
root = None
tk_im = None
color = (255,255,255,255)
first_point = ()
second_point = ()

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
    canvas.create_image(im.size[0]/2, im.size[1]/2, image=tk_im)

def draw_mode():
    global canvas
    canvas.bind("<Button 1>", first_drawing_point)
    canvas.bind("<Button 3>", second_drawing_point)

def text_mode():
    global canvas
    canvas.bind("<Button 1>", add_text)

def color_picker():
    global canvas
    canvas.bind("<Button 1>", pick_color)

def draw_point(event):
    global tk_im
    global img
    global canvas
    global color
    img = basic_functions.draw_point(img, event.x, event.y, color)
    tk_im = ImageTk.PhotoImage(img)
    canvas.delete("all")
    display_image(img, canvas)

def add_text(event):
    global tk_im
    global img
    global canvas
    global color
    content = simpledialog.askstring(title=app_title, prompt="Enter text: ")
    try:
        img = basic_functions.add_text(img, event.x, event.y, content,color)
    except TypeError:
        pass
    tk_im = ImageTk.PhotoImage(img)
    canvas.delete("all")
    display_image(img, canvas)

def first_drawing_point(event):
    global first_point
    first_point = (event.x, event.y)
    print("Point 1:", event.x, event.y)
    if second_point != ():
        draw_line(img)

def second_drawing_point(event):
    global second_point 
    second_point = (event.x, event.y)
    print("Point 2:", event.x, event.y)
    if first_point != ():
        draw_line(img)

def draw_line(im):
    global tk_im
    global img
    global canvas
    global first_point
    global second_point
    global color

    print(first_point[0], first_point[1], "->", second_point[0], second_point[1])
    img = basic_functions.draw_line(img, first_point[0], first_point[1], second_point[0], second_point[1], color)

    first_point = ()
    second_point = ()

    tk_im = ImageTk.PhotoImage(img)
    display_image(img, canvas)
def pick_color(event):
    global tk_im
    global img 
    global canvas
    global color

    color = basic_functions.pick_color(img, event.x, event.y)
    print(color)

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
    new_x = simpledialog.askinteger(title=app_title, prompt="Enter new X size:")
    new_y = simpledialog.askinteger(title=app_title, prompt="Enter new Y size:")
    try:
        img = basic_functions.resize(img, new_x, new_y)
    except TypeError:
        pass
    tk_im = ImageTk.PhotoImage(img)
    canvas.delete("all")
    display_image(img, canvas)

def gaussian_blur():
    global tk_im
    global img
    global canvas
    radius = simpledialog.askinteger(title=app_title, prompt="Enter radius:")
    try:
        img = basic_functions.gaussianBlur(img, radius)
    except TypeError:
        pass
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
    global color
    img = basic_functions.colorToTransparency(img, color)
    tk_im = ImageTk.PhotoImage(img)
    canvas.delete("all")
    display_image(img, canvas)


root = Tk()
root.geometry("400x400")
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
button = Button(master=root, command=draw_mode, text="Draw line")
button.pack()
button = Button(master=root, command=text_mode, text="Text")
button.pack()
button = Button(master=root, command=color_picker, text="Color picker")
button.pack()

# Variables for PIL image and image for Tkinter canvas
img,tk_im = get_image()

image_window = Toplevel()
image_window.title(app_title)
image_window.geometry(str(img.size[0])+"x"+str(img.size[1]))
canvas = Canvas(master=image_window)
display_image(img, canvas)

root.mainloop()