from Tkinter import *
import threading
import internet_protocol
import time

class Gui(threading.Thread):
    def __init__(self, scanner):
        threading.Thread.__init__(self)
        self.root = Tk()
        self.root.title("Scanopy - IP Scanner")
        self.scanner = scanner
        self.initComponents()
        self.console_rows = 0
        self.max_console_rows = 20

    def run(self):
        self.root.mainloop()

    def output_console(self, new_text):
        self.consoleText.config(state=NORMAL)
        self.consoleText.insert(END, "\n" + new_text)
        self.consoleText.see(END)
        self.consoleText.config(state=DISABLED)

    def initComponents(self):
        root = self.root

        # Input Frame
        inputFrame = Frame(root)
        inputFrame.pack(expand=1, pady=15, padx=15)

        # Init Components
        rangeLabel = Label(inputFrame, text="Range:")
        self.rangeStartEntry = Entry(inputFrame)
        self.rangeStartEntry.insert(0, "173.194.40.241")
        self.rangeEndEntry = Entry(inputFrame)
        self.rangeEndEntry.insert(0, "173.194.40.249")
        fileLabel = Label(inputFrame, text="Output File:")
        fileEntry = Entry(inputFrame)
        fileBrowserButton = Button(inputFrame, text="Browse")
        scanButton = Button(inputFrame, text="Scan", command=self.scan)

        # Set Component Grid Positions
        rangeLabel.grid(row=0, column=0, padx=5, pady=5)
        self.rangeStartEntry.grid(row=0, column=1, padx=5, pady=5)
        self.rangeEndEntry.grid(row=0, column=2, padx=5, pady=5)
        fileLabel.grid(row=1, column=0, padx=5, pady=5)
        fileEntry.grid(row=1, column=1, padx=5, pady=5)
        fileBrowserButton.grid(row=1, column=2, padx=5, pady=5)
        scanButton.grid(row=2, column=2, padx=10, pady=10)

        # Console Frame
        self.consoleFrame = Frame(root)
        self.consoleFrame.pack(expand=1, pady=15, padx=15)
        self.consoleText = Text(self.consoleFrame, fg="green", bg="black", width=70, state=DISABLED)
        self.consoleText.pack()

    def scan(self):
        start_ip = self.rangeStartEntry.get()
        end_ip = self.rangeEndEntry.get()
        ip_list = internet_protocol.getIpAddressesFromRange(start_ip, end_ip)
        self.ip_scan_index = 0
        # Kindof recursive function with call to root.after() to keep gui from freezing
        def scanIp():
            result = self.scanner.scan(ip_list[self.ip_scan_index])
            self.output_console(result)
            self.ip_scan_index += 1
            if self.ip_scan_index < len(ip_list):
                self.root.after(1000, scanIp)
        scanIp()
