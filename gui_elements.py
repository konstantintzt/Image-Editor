from PIL import Image, ImageTk
from tkinter import Tk, Label, Button, Canvas, Toplevel

class ImageDisplay(Toplevel):

    def __init__(self, master, title, im):

        Toplevel.__init__(self, master)
        self.geometry(str(im.size[0]+20)+"x"+str(im.size[1]+20))
        self.title(title)

        im_tkinter = ImageTk.PhotoImage(master=self, image=im)
        canvas = Canvas()
        canvas.pack(side='top', fill='both', expand="yes")
        canvas.create_image(im.size[0]/2+10, im.size[1]/2+10, image=im_tkinter)
        print(self)

    def refresh(self, im):

        self.geometry(str(im.size[0]+20)+"x"+str(im.size[1]+20))
        im_tkinter = ImageTk.PhotoImage(master=self, image=im)
        canvas = Canvas(master=self)
        canvas.pack(side='top', fill='both', expand="yes")
        canvas.create_image(im.size[0]/2+10, im.size[1]/2+10, image=im_tkinter)



root = Tk()

button = Button(master=root, text="TEST")
button.pack()

root.geometry("800x800")
root.title('Map')

background_image=ImageTk.PhotoImage(file="D:/Pictures/logo2.png")


def toplevel():
    top = Toplevel()
    top.title('Optimized Map')
    top.geometry("800x800")
    optimized_canvas = Canvas(top)
    optimized_canvas.pack(side="top", fill="both", expand=1)
    optimized_image = optimized_canvas.create_image(400,400, image=background_image)

toplevel()

root.mainloop()
