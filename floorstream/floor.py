import socket

class Floor:
    _sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connected = False

    def connect(self):
        self._sock.connect((self.host, self.port))
        self.connected = True

    # data must be list of integers of length 64 or 192 (8-bit or 24-bit color)
    def send(self, data):
        cmd_data = list('DANCEFLOOR') + [1] + list(data)
        self._sock.sendto(bytearray(cmd_data), (self.host, self.port))
        cmd_end = list('DANCEFLOOR') + [2]
        self._sock.sendto(bytearray(cmd_end), (self.host, self.port))
