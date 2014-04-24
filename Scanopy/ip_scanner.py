#import time
from socket import *
#import sh

class IpScanner:

    def scan(self, ip):
        port = 80
        ping_result = self.ping(ip, port)
        if (ping_result):
            return "Ping on "+str(ip)+":"+str(port)+" SUCCESS."
        else:
            return "Ping on "+str(ip)+":"+str(port)+" failed."
    
    def ping(self, ip, port):
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.settimeout(1)
        try:
            connSkt.connect((ip, port))
            return True
        except:
            return False
        finally:
            connSkt.close()