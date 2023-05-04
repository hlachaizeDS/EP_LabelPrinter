import socket

class LabelPrinter():
    address = 0
    port = 0
    socket=None

    def __init__( self, address, port):
        self.address=address
        self.port=port

    def send(self,command,rNeeded):

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.address, self.port))
        self.socket.send((command+"\n").encode())

        if rNeeded:
            r = self.socket.recv(1024)
        self.socket.close()

        if rNeeded:
            return r