import struct
from socket import *

class Scanner:

    def scan(self, ip, port):
        ping_result = self.isPortOpen(ip, port)
        result = ""
        if (ping_result):
            result= ""
            result += str(ip)+":"+str(port)+" >>> OPEN <<<"
        else:
            result = str(ip)+":"+str(port)+" closed"
        return result
    
    def isPortOpen(self, ip, port):
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.settimeout(1)
        try:
            #connSkt.connect((ip, int(port)))
            return True
        except:
            return False
        finally:
            connSkt.close()
    
    def getHostByIp(self, ip):
        return gethostbyaddr(ip)[0]
            
    def getIpAddressesFromRange(self, start, end):
        ipstruct = struct.Struct('>I')
        start, = ipstruct.unpack(inet_aton(start))
        end, = ipstruct.unpack(inet_aton(end))
        return [inet_ntoa(ipstruct.pack(i)) for i in range(start, end+1)]