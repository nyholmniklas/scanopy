import time

class IpScanner:

    def scan(self, start_ip, end_ip):
        x = 0
        while (x < 200000):
            gui.outputToConsole(str(x))
            x += 1