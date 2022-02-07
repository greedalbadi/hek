import socket
from .exceptions import *








class _Server_info:
    # server connect timeout
    CONNECT_TIMOUT = 9





class Server:
    def __init__(self):

        self.set_socket = set_socket

    def get_banner(self, address: str, port: str, timeout: int = 5):
        s = socket.socket()
        s.settimeout(timeout)
        try:
            s.connect((address, port))
            return s.recv(1024).decode()
        except socket.timeout:
            raise SocketConnectionError("Time out")
        except socket.error as exc:
            raise SocketConnectionError(f"connection error: {exc}")


    def portscan(self, ip: str, port: int, timeout=3):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create socket
        s.settimeout(int(timeout)) # set timeout
        try:
            conn = s.connect_ex((ip, port)) #connect to ip/port
            if (conn == 0): # if conn not 0 connection closed
                return True
            else:
                return False
        except socket.timeout:
            raise SocketConnectionError("Time out")
        except socket.error as exc:
            raise SocketConnectionError(f"connection error: {exc}")


class set_socket:
    def __init__(self, host: str, port: int, sock_arg1=socket.AF_INET, sock_arg2=socket.SOCK_STREAM):
        # set values
        self.host = host
        self.port = port
        # set server socket
        self.server = socket.socket(sock_arg1, sock_arg2)


    def connect(self, host: int=None, port: int=None, timeout = int(_Server_info.CONNECT_TIMOUT)):
        # check if new host and port are given
        if host != None:
            address = (str(host), int(port))
        else:
            address = (str(self.host), int(self.port))
        try:
            self.server.settimeout(int(timeout))  # set timeout
            # connect to server
            self.server.connect(address)
            return True
        except:
            raise SocketConnectionError("Error: connection error")



    def sendpacket(self, packet, host: str=None, port: int=None, connected=True, auto_close=False, encoding = "utf-8"):

        # check if new host and port are given
        if host != None:
            address = (host, port)

            # checking if user already connected
            if connected == False:
                set_socket.connect(self, host, port)
        else:
            address = (str(self.host), int(self.port))
            # checking if user already connected
            if connected == False:
                set_socket.connect(self)

        # check if packet is bytes
        if not isinstance(packet, bytes):
            # if packet is not bytes encode it into bytes
            packet = packet.encode(encoding)

        #checking if auto close enabled


        # send packet
        if self.server.sendto(packet, address):
            if auto_close == True:
                set_socket.close(self)
            return True
        else:
            if auto_close == True:
                set_socket.close(self)
            return False



    def close(self):
        # terminate connection
        return self.server.close()

    def recv(self, bufsize):
        # receive data
        return self.server.recv(bufsize)

server = Server()