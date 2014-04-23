from Tkinter import *


class Gui(object):
    def __init__(self):
        self.root = Tk()
        self.initComponents()
        self.root.mainloop()

    def initComponents(self):
        root = self.root

        #Init Input Frame
        inputFrame = Frame(root)

        #Init Components
        rangeLabel = Label(inputFrame, text="Range:")
        rangeStartEntry = Entry(inputFrame)
        rangeEndEntry = Entry(inputFrame)
        fileLabel = Label(inputFrame, text="Output File:")
        fileEntry = Entry(inputFrame)

        #Set Component Grid Positions
        rangeLabel.grid(row=0, column=0)
        rangeStartEntry.grid(row=0, column=1)
        rangeEndEntry.grid(row=0, column=2)
        fileLabel.grid(row=1, column=0)
        fileEntry.grid(row=1, column=1)

        #Pack Components
        #rangeLabel.pack(in_=inputFrame)
        #rangeStartEntry.pack(in_=inputFrame)
        #rangeEndEntry.pack(in_=inputFrame)
        #fileLabel.pack(in_=inputFrame)
        #fileEntry.pack(in_=inputFrame)

        #Pack Input Frame
        inputFrame.pack(side="top", fill="x")

        print("at least here")