from Tkinter import *


class Gui(object):
    def __init__(self):
        self.root = Tk()
        self.initComponents()
        self.root.mainloop()

    def initComponents(self):
        root = self.root

        #Main Frame
        #mainFrame = Frame(root)
        #mainFrame.pack(side=LEFT, expand=1)

        #Input Frame
        inputFrame = Frame(root)
        inputFrame.pack(expand=1, pady=50, padx=50)

        #Init Components
        rangeLabel = Label(inputFrame, text="Range:")
        rangeStartEntry = Entry(inputFrame)
        rangeEndEntry = Entry(inputFrame)
        fileLabel = Label(inputFrame, text="Output File:")
        fileEntry = Entry(inputFrame)

        #Set Component Grid Positions
        rangeLabel.grid(row=0, column=0, padx=5, pady=5)
        rangeStartEntry.grid(row=0, column=1, padx=5, pady=5)
        rangeEndEntry.grid(row=0, column=2, padx=5, pady=5)
        fileLabel.grid(row=1, column=0, padx=5, pady=5)
        fileEntry.grid(row=1, column=1, padx=5, pady=5)