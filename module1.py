import sys
from Tkinter import *

def main():
    app = App()
    app.master.title("Sample application")
    app.mainloop()

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid(sticky=N+S+E+W)

        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)

        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.__createWidgets()

    def __createWidgets(self):
        self.f1 = Frame(self, height=100, width=200,
            bg='green')
        self.f1.grid(row=0, column=0, sticky=E+W)

        self.f2 = Frame( self, bg= "yellow", height=100, width=200 ) ############################# CHANGE to self.f2 = myTestFrame( self )
        self.f2.grid(row=1, sticky = N+S+E+W)

        self.f3 = Frame( self, bg = "cyan", height = 100, width = 200 )
        self.f3.grid(row=2, sticky = E+W)

        self.quitButton = Button ( self, text="Quit", command=self.quit )
        self.quitButton.grid(row=4, column=0, columnspan=100,
            sticky=E+W)

class myTestFrame( Frame ):
    def __init__( self, parent):
        Frame.__init__(self, None)

        self.myText = Text( self )
        self.myText.grid()

        #self.testFrame = Frame ( self, bg = "white", height = 100, width = 300 )
        #self.testFrame.grid()

if __name__ == "__main__":
    main()