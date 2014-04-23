from Tkinter import *
import threading


class Gui(threading.Thread):
    def __init__(self, scanner):
        threading.Thread.__init__(self)
        self.root = Tk()
        self.scanner = scanner
        self.initComponents()

    def run(self):
        self.root.mainloop()

    def sayHi(self):
        print("hi")

    def initComponents(self):
        root = self.root

        #Input Frame
        inputFrame = Frame(root)
        inputFrame.pack(expand=1, pady=15, padx=15)

        #Init Components
        rangeLabel = Label(inputFrame, text="Range:")
        rangeStartEntry = Entry(inputFrame)
        rangeEndEntry = Entry(inputFrame)
        fileLabel = Label(inputFrame, text="Output File:")
        fileEntry = Entry(inputFrame)
        fileBrowserButton = Button(inputFrame, text="Browse")
        scanButton = Button(inputFrame, text="Scan", command=self.scan)

        #Set Component Grid Positions
        rangeLabel.grid(row=0, column=0, padx=5, pady=5)
        rangeStartEntry.grid(row=0, column=1, padx=5, pady=5)
        rangeEndEntry.grid(row=0, column=2, padx=5, pady=5)
        fileLabel.grid(row=1, column=0, padx=5, pady=5)
        fileEntry.grid(row=1, column=1, padx=5, pady=5)
        fileBrowserButton.grid(row=1, column=2, padx=5, pady=5)
        scanButton.grid(row=2, column=2, padx=10, pady=10)

    def scan(self):
        self.scanner.testCallback(self)