from gui import *
from scanner import *

if __name__ == '__main__':
    scanner = Scanner()
    gui_thread = Gui(scanner)
    gui_thread.run()
