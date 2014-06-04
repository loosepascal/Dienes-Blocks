

import Tkinter as tk
window = tk.Tk()
   # app = HomeScreen(root)
#    app.withdraw()
window.title("Dienes Blocks Application")
window.geometry("300x300")
#window.wm_iconbitmap('logo2.ico')

photo = tk.PhotoImage(file="logosmall.gif")
w=tk.Label(window,image=photo)
w.pack()

button1 = tk.Button(window, text = 'Prototype', width = 25, command = tk.Toplevel)#buttons and frames are different types of widgets
button1.pack()

window.mainloop()

##
##def prototype_window(self): #this is a method (note we call it with dot notation but need not include the self arguement - python includes for us
##    self.newWindow = tk.Toplevel(self.master)#Toplevel widgets work as windows that are directly managed by the window manager.
##    self.app =    Prototype(self.newWindow)