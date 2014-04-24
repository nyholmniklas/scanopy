class IpInfo:
    
    def __init__(self, ip):
        self.ip = ip
        

def getIpAddressesFromRange(start_ip_address, end_ip_address):
    start_address_elements = start_ip_address.split('.')
    end_address_elements = end_ip_address.split('.')
    ip_list = []
    print(start_address_elements[0])
    for a in range(int(start_address_elements[0]), int(end_address_elements[0])+1):
        for b in range(int(start_address_elements[1]), int(end_address_elements[1])+1):
            for c in range(int(start_address_elements[2]), int(end_address_elements[2])+1):
                for d in range(int(start_address_elements[3]), int(end_address_elements[3])+1):
                    print(str(a)+"."+str(b)+"."+str(c)+"."+str(d))
                    ip_list.append(str(a)+"."+str(b)+"."+str(c)+"."+str(d))
    print(len(ip_list))
    
    return ip_list
                    