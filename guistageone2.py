#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ck2211
#
# Created:     04/06/2014
# Copyright:   (c) ck2211 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
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

# global variables: teacher_button, student_button, prototype_button, sparx_header, home_button

def main():
##    FrameCreator()
    window =Tk()
    window.geometry("291x300")
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
        self.sparx_head()
        self.create_buttons()

    def sparx_head(self):
        self.grid()
        photo = PhotoImage(file="logosmall.gif")
        global sparx_header
        sparx_header = Label(self, image=photo, bg ="black")
        sparx_header.image = photo # keep a reference!
        sparx_header.grid(column=0, row=0, sticky='NSEW', columnspan=3)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0,weight=1)
##        self.resizable(True, True)

    def create_buttons(self):
        self.grid()
        global teacher_button, student_button, prototype_button
        #teacher button
        teacher_button = Tkinter.Button(self, text="Teacher")
##        teacher_button.place(y=90, height=20)
        teacher_button.grid(column=0, row=1, sticky='EW')
##        self.resizable(True, True)
##        teacher_button.pack()
        # student button
        student_button = Tkinter.Button(self, text="Student")
##        student_button.place(y=110, height=20)
        student_button.grid(column=2, row=1, sticky='EW')
##        self.resizable(True, True)
##        student_button.pack()
        # prototype button
        prototype_button = Tkinter.Button(self, text="Prototype", command=self.OnButtonClick)
##        prototype_button.place(y=130, height=20)
        prototype_button.grid(column=1, row=1, sticky='EW')
##        self.resizable(True, True)
##        prototype_button.pack()

    def OnButtonClick(self):
        sparx_header.grid_forget()
        teacher_button.grid_forget()
        prototype_button.grid_forget()
        student_button.grid_forget()
        app = Prototype(self)

class Prototype(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.createLayout()
##        self.bluetoothRead()

    def createLayout(self):
        self.grid()
        global home_button, thousands, thousands_label, hundreds, hundreds_label, tens, tens_label, units, units_label

        #add the home button
        home_button = Tkinter.Button(self, text="Home", command=self.HomeButtonClick)
        home_button.grid(row=0, column=0, sticky='EW')

        #add the four zones
        thousands = Label(self, text="Thousands (1000s)", bg="red", fg="black", relief="sunken", height=2, width=15)
        thousands.grid(column=0, row=1, columnspan=1, rowspan=2)
        hundreds = Label(self, text="Hundreds (100s)", bg="cyan", fg="black", relief="sunken", height=2, width=15)
        hundreds.grid(column=1, row=1, columnspan=1, rowspan=2)
        tens = Label(self, text="Tens (10s)", bg="green", fg="black", relief="sunken",height=2, width=15)
        tens.grid(column=2, row=1, columnspan=1, rowspan=2)
        units = Label(self, text="Units (1s)", bg="yellow", fg="black", relief="sunken",height=2,width=15)
        units.grid(column=3, row=1, columnspan=1, rowspan=2)

        #create variables to hold the data
        self.thousands_data = Tkinter.StringVar()
        self.thousands_data.set(3)
        self.hundreds_data = Tkinter.StringVar()
        self.tens_data = Tkinter.StringVar()
        self.units_data = Tkinter.StringVar()

        #create labels to display the data
        thousands_label = Label(self, text=self.thousands_data, bg="white", fg="black", relief="raised", height=3, width=15)
        thousands_label.grid(column=0, row=3)
        hundreds_label = Label(self, text=self.hundreds_data, bg="white", fg="black", relief="raised", height=3, width=15)
        hundreds_label.grid(column=1, row=3)
        tens_label = Label(self, text=self.tens_data, bg="white", fg="black", relief="raised", height=3, width=15)
        tens_label.grid(column=2, row=3)
        units_label = Label(self, text=self.units_data, bg="white", fg="black", relief="raised", height=3, width=15)
        units_label.grid(column=3, row=3)


    def HomeButtonClick(self):
        home_button.grid_forget()
        thousands.grid_forget()
        hundreds.grid_forget()
        tens.grid_forget()
        units.grid_forget()
        thousands_label.grid_forget()
        hundreds_label.grid_forget()
        tens_label.grid_forget()
        units_label.grid_forget()
        app = HomeScreen(self)

##    def bluetoothRead(self):

##    def displayValue(self):


if __name__ == "__main__":
    main()