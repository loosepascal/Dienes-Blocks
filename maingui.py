#-------------------------------------------------------------------------------
# Name:        Dienes Blocks GUI
# Purpose:
#
# Author:      kieran
#
# Created:     30/05/2014
# Copyright:   (c) kieran 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#from Tkinter import *
import Tkinter as tk

def main():
    window = tk.Tk()

#    app.withdraw()
    window.title("Dienes Blocks Application")
    window.geometry("300x300")
   # window.wm_iconbitmap('logox.ico')
    photo = tk.PhotoImage(file="logosmall.gif")
    w=tk.Label(window,image=photo)
    w.pack()
    app = HomeScreen(window)

    window.mainloop()

class HomeScreen:
    def __init__(self, master):# special Method, which is called class constructor or initialization method that Python calls when you create a new instance of this class.
##        global root
##        root = Tk()
        self.master = master #self is a particular object (unique instance of a data structure that's defined by its class) defined by the attributes of this class
        self.frame = tk.Frame(self.master, height =100, width=300) #The Frame Widget is very important for the process of grouping and organizing other widget.
        #master represents the parent window
        self.frame.grid(row=0, column=0, sticky=tk.E+tk.W)
        self.button1 = tk.Button(self.frame, text = 'Prototype', width = 20, command = self.prototype_window)#.grid(row =3, column=1)#buttons and frames are different types of widgets
        #self.button1.pack(side = tk.LEFT)
        self.button2 = tk.Button(self.frame, text = 'Teacher', width = 25, command = self.teacher_window)#.grid(row =3, column=2)#buttons and frames are different types of widgets
      #  self.button2.pack()
        #self.button1.place(height=100, width=100)

    def prototype_window(self): #this is a method (note we call it with dot notation but need not include the self arguement - python includes for us
        self.newWindow = tk.Toplevel(self.master)#Toplevel widgets work as windows that are directly managed by the window manager.
        self.app = Prototype(self.newWindow)

    def teacher_window(self): #this is a method (note we call it with dot notation but need not include the self arguement - python includes for us
        self.newWindow = tk.Toplevel(self.master)#Toplevel widgets work as windows that are directly managed by the window manager.
        self.app = Prototype(self.newWindow)



class Prototype:
    def __init__(self, master):


        self.master = master
        self.frame = tk.Frame(self.master)
        self.homeButton = tk.Button(self.frame, text = 'Home', width = 25, command = self.close_windows)
        self.homeButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()#destroy the object i.e. the window



if __name__ == '__main__':
    main()