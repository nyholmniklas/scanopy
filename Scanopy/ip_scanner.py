#import time
from socket import *
#import sh

class PortScanner:

    def scan(self, ip, port):
        ping_result = self.scanPort(ip, port)
        result = ""
        if (ping_result):
            result= ""
            host = gethostbyaddr(ip)[0]
            if host != None:
                result += "Resolved hostname to " + host + "\n"
            result += str(ip)+":"+str(port)+" >>> OPEN <<<"
        else:
            result = str(ip)+":"+str(port)+" closed"
        return result
    
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