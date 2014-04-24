from socket import *

class Scanner:

    def scan(self, ip, port):
        ping_result = self.isPortOpen(ip, port)
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
    
    def isPortOpen(self, ip, port):
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.settimeout(1)
        try:
            connSkt.connect((ip, int(port)))
            return True
        except:
            return False
        finally:
            connSkt.close()
            
    def getIpAddressesFromRange(self, start_ip_address, end_ip_address):
        start_address_elements = start_ip_address.split('.')
        end_address_elements = end_ip_address.split('.')
        ip_list = []
        for a in range(int(start_address_elements[0]), int(end_address_elements[0])+1):
            for b in range(int(start_address_elements[1]), int(end_address_elements[1])+1):
                for c in range(int(start_address_elements[2]), int(end_address_elements[2])+1):
                    for d in range(int(start_address_elements[3]), int(end_address_elements[3])+1):
                        ip_list.append(str(a)+"."+str(b)+"."+str(c)+"."+str(d))
        return ip_list