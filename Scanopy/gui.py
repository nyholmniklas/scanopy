from Tkinter import *

class Gui(object):

    def __init__(self):
        self.root = Tk()
        self.initComponents()
        self.root.mainloop()

    def initComponents(self):
        root = self.root

        #Create Range label
        w = Label(root, text="Hello, World!")
        w.pack()