#import time
from socket import *
#import sh

class PortScanner:

    def scan(self, ip, port):
        ping_result = self.scanPort(ip, port)
        if (ping_result):
            return "Ping on "+str(ip)+":"+str(port)+" SUCCESS."
        else:
            return "Ping on "+str(ip)+":"+str(port)+" failed."
    
    def scanPort(self, ip, port):
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.settimeout(1)
        try:
            connSkt.connect((ip, int(port)))
            return True
        except:
            return False
        finally:
            connSkt.close()