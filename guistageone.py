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

        self.create_buttons()
        self.sparx_head()

    def sparx_head(self):
        self.grid()
        photo = Tkinter.PhotoImage(file="logosmall.gif")
        sparx_header = Tkinter.Label(image=photo)
        sparx_header.image = photo # keep a reference!
        sparx_header.grid(column=0, row=1, columnspan=2, rowspan=2, sticky='NSEW')
        self.grid_columnconfigure(0, weight=1)
##        sparx_header.place(y=0, height=90)
##        sparx_header.pack()

    def create_buttons(self):
        self.grid()
        #teacher button
        teacher_button = Tkinter.Button(self, text="Teacher")
##        teacher_button.place(y=90, height=20)
        teacher_button.grid(column=0, row=10, sticky='EW')
##        teacher_button.pack()
        # student button
        student_button = Tkinter.Button(self, text="Student")
##        student_button.place(y=110, height=20)
        student_button.grid(column=2, row=10, sticky='EW')
##        student_button.pack()
        # prototype button
        prototype_button = Tkinter.Button(self, text="Prototype", command=self.OnButtonClick)
##        prototype_button.place(y=130, height=20)
        prototype_button.grid(column=1, row=10, sticky='EW')
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