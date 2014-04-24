#import time
from socket import *
#import sh

class PortScanner:

    def scan(self, ip, port):
        ping_result = self.scanPort(ip, port)
        if (ping_result):
            return str(ip)+":"+str(port)+" >>> OPEN <<<"
        else:
            return str(ip)+":"+str(port)+" closed"
    
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