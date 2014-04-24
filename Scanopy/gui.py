from Tkinter import *
import threading
import internet_protocol

class Gui(threading.Thread):
    def __init__(self, scanner):
        threading.Thread.__init__(self)
        self.root = Tk()
        self.scanner = scanner
        self.initComponents()

    def run(self):
        self.root.mainloop()

    def outputToConsole(self, new_text):
        labelText = self.consoleLabel.cget("text") + new_text
        self.consoleLabel.pack_forget()
        self.consoleLabel = Label(self.consoleFrame, text=labelText)
        self.consoleLabel.pack()

    def initComponents(self):
        root = self.root

        #Input Frame
        inputFrame = Frame(root)
        inputFrame.pack(expand=1, pady=15, padx=15)

        #Init Components
        rangeLabel = Label(inputFrame, text="Range:")
        self.rangeStartEntry = Entry(inputFrame)
        self.rangeStartEntry.insert(0, "0.0.0.0")
        self.rangeEndEntry = Entry(inputFrame)
        self.rangeEndEntry.insert(0, "1.15.10.5")
        fileLabel = Label(inputFrame, text="Output File:")
        fileEntry = Entry(inputFrame)
        fileBrowserButton = Button(inputFrame, text="Browse")
        scanButton = Button(inputFrame, text="Scan", command=self.scan)

        #Set Component Grid Positions
        rangeLabel.grid(row=0, column=0, padx=5, pady=5)
        self.rangeStartEntry.grid(row=0, column=1, padx=5, pady=5)
        self.rangeEndEntry.grid(row=0, column=2, padx=5, pady=5)
        fileLabel.grid(row=1, column=0, padx=5, pady=5)
        fileEntry.grid(row=1, column=1, padx=5, pady=5)
        fileBrowserButton.grid(row=1, column=2, padx=5, pady=5)
        scanButton.grid(row=2, column=2, padx=10, pady=10)

        #Console Frame
        self.consoleFrame = Frame(root)
        self.consoleFrame.pack(expand=1, pady=15, padx=15)
        self.consoleLabel = Label(self.consoleFrame, text="")
        self.consoleLabel.pack()

    

    def scan(self):
        #This is where you need to make the root.after calls so the gui doesnt freeze!!
        start_ip = self.rangeStartEntry.get()
        end_ip = self.rangeEndEntry.get()
        ip_list = internet_protocol.getIpAddressesFromRange(start_ip, end_ip)
        #self.scanner.scan(start_ip, end_ip)
        