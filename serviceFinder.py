import socket

def getServicesTCP(ports):
    protocolname = 'tcp'
    for port in ports:
        print("Port: %s => service name: %s" % (port, socket.getservbyport(port, protocolname)))



def getServicesUDP(ports):
    protocolname = 'udp'