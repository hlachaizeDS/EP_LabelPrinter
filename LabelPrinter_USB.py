import usb.core
import usb.util

class LabelPrinter():
    address = 0
    port = 0
    socket=None

    def __init__( self, address, port):
        self.address=address
        self.port=port