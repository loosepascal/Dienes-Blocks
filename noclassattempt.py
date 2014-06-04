#-------------------------------------------------------------------------------
# Name:        GUI attempt with no classes
# Purpose:
#
# Author:      Christos Karpis
#
# Created:     04/06/2014
# Copyright:   (c) Christos Karpis 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import Tkinter
from Tkinter import *

##def main():
window = Tk()
window.geometry("300x300")
window.title("Dienes Blocks Application")
window.iconbitmap(default='favicon.ico')
photo = tk.PhotoImage(file="logosmall.gif")
sparx_header = Tkinter.Label(window,image=photo)
sparx_header.pack()
window.mainloop()