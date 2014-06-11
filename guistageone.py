#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Christos Karpis
#
# Created:     03/06/2014
# Copyright:   (c) Christos Karpis 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import Tkinter
from Tkinter import *
from Tkinter import PhotoImage

from Tkinter import PhotoImage

def main():
##    FrameCreator()
    window =Tk()
    window.geometry("300x300")
    window.title("Dienes Blocks Application")
    window.iconbitmap(default='favicon.ico')
##    w=Tkinter.Label(window,image=photo)
##    w.grid(row=0, column=1)
    app = HomeScreen(window)
    window.mainloop()

##def FrameCreator():
##    window =Tk()
##    window.geometry("300x300")
##    window.title("Dienes Blocks Application")
##    window.iconbitmap(default='favicon.ico')

class HomeScreen(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
<<<<<<< HEAD

       # self.create_buttons()
=======
>>>>>>> origin/master
        self.sparx_head()
        self.create_buttons()

    def sparx_head(self):
        self.grid()
<<<<<<< HEAD

##        gif1 = PhotoImage(file = 'Image.gif')
##
##        label1 = Label(image=gif1)
##        label1.image = gif1
##        label1.grid(row=1, column = 0, columnspan = 2, sticky=NW)

        photo = Tkinter.PhotoImage(file="logosmall.gif")
        sparx_header = Tkinter.Label(self, image=photo)
        sparx_header.image = photo # keep a reference!
        sparx_header.grid(column=0, row=1, columnspan=6, rowspan=2, sticky='NSEW')
        self.grid_columnconfigure(0, weight=1)

        teacher_button = Tkinter.Button(self, text="Teacher")
##        teacher_button.place(y=90, height=20)
        teacher_button.grid(column=0,columnspan=2, rowspan=2, padx=5, pady=5, row=5, sticky=E+W)
##        teacher_button.pack()
        # student button
        student_button = Tkinter.Button(self, text="Student")
##        student_button.place(y=110, height=20)
        student_button.grid(column=3, row=10, sticky='EW')
##        student_button.pack()
        # prototype button
        prototype_button = Tkinter.Button(self, text="Prototype", command=self.OnButtonClick)
##        prototype_button.place(y=130, height=20)
        prototype_button.grid(column=2, row=10, sticky='EW')

        var = StringVar()

        l = Label(self, textvariable=var, anchor=NW, justify=LEFT, wraplength=398)
##        sparx_header.place(y=0, height=90)

##        sparx_header.pack()
=======
        photo = PhotoImage(file="logosmall.gif")
        sparx_header = Label(self, image=photo)
        sparx_header.image = photo # keep a reference!
        sparx_header.grid(column=0, row=0, sticky='NSEW', columnspan=3)
        self.grid_columnconfigure(0, weight=1)
>>>>>>> origin/master

    def create_buttons(self):
        #frame = Tkinter.Frame()
        #frame.grid(row=0, column=0, columnspan=6, rowspan=3, sticky=E+W)
        self.grid()
        #teacher button
        teacher_button = Tkinter.Button(frame, text="Teacher")
##        teacher_button.place(y=90, height=20)
<<<<<<< HEAD
        teacher_button.grid(column=0,columnspan=2, rowspan=2, padx=5, pady=5, row=10, sticky=E+W)
=======
        teacher_button.grid(column=0, row=1, sticky='EW')
>>>>>>> origin/master
##        teacher_button.pack()
        # student button
        student_button = Tkinter.Button(self, text="Student")
##        student_button.place(y=110, height=20)
<<<<<<< HEAD
        student_button.grid(column=3, row=10, sticky='E+W')
=======
        student_button.grid(column=2, row=1, sticky='EW')
>>>>>>> origin/master
##        student_button.pack()
        # prototype button
        prototype_button = Tkinter.Button(self, text="Prototype", command=self.OnButtonClick)
##        prototype_button.place(y=130, height=20)
<<<<<<< HEAD
        prototype_button.grid(column=2, row=10, sticky='E+W')
=======
        prototype_button.grid(column=1, row=1, sticky='EW')
>>>>>>> origin/master
##        prototype_button.pack()

    def OnButtonClick(self):
        app = Prototype(self)

class Prototype(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.createLayout()
##        self.bluetoothRead()

    def createLayout(self):
        self.grid()
        #add the home button
        home_button = Tkinter.Button(self, text="Home")
        home_button.grid(row=0, column=0, sticky='EW')

##    def bluetoothRead(self):

##    def displayValue(self):

if __name__ == "__main__":
    main()