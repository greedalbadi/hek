import socket
from .exceptions import *








class _Server_info:
    # server connect timeout
    CONNECT_TIMOUT = 9





class Server:
    def __init__(self):
        self.socket = _Socket
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



class _Socket:

    def socket(self, sock_arg1=socket.AF_INET, sock_arg2=socket.SOCK_STREAM):

        return socket.socket(sock_arg1, sock_arg2)


    def connect(self,sock, host: str=None, port: int=None, timeout = int(_Server_info.CONNECT_TIMOUT)):
        # check if new host and port are given

        address = (str(host), int(port))
        try:
            sock.settimeout(int(timeout))  # set timeout
            # connect to server
            sock.connect(address)
            return True
        except:
            raise SocketConnectionError("Error: connection error")


    def sendpacket(self, sock, packet, host: str=None, port: int=None, connected=True, auto_close=False, encoding = "utf-8"):

        # tuple the host and port
        address = (host, port)

        # checking if user already connected
        if connected == False:
            _Socket.connect(self, sock, host=host, port=port)

        # check if packet is bytes
        if not isinstance(packet, bytes):
            # if packet is not bytes encode it into bytes
            packet = packet.encode(encoding)

        # send packet
        if sock.sendto(packet, address):
            if auto_close == True:
                sock.close()
            return True
        else:
            if auto_close == True:
                sock.close()
            return False
    def close(self, sock):
        # terminate connection
        return sock.close()

    def recv(self,sock, bufsize=1048):
        # receive data
        return sock.recv(bufsize)


class set_socket:
    def __init__(self, host: str, port: int, sock_arg1=socket.AF_INET, sock_arg2=socket.SOCK_STREAM):
        # set values
        self.host = host
        self.port = port
        self.socket = _Socket()
        # set server socket
        self.server = socket.socket(sock_arg1, sock_arg2)


    def connect(self, host: str=None, port: int=None, timeout = int(_Server_info.CONNECT_TIMOUT)):
        if host and port == None:
            return self.socket.connect(self.server, host=self.host, port=self.port, timeout=timeout)
        else:
            return self.socket.connect(self.server, host=host, port=port, timeout=timeout)


    def sendpacket(self, packet, host: str=None, port: int=None, connected=True, auto_close=False, encoding = "utf-8"):
        if host and port == None:
            return self.socket.sendpacket(self.server, packet=packet, host=self.host, port=self.port, connected=connected, auto_close=auto_close, encoding=encoding)
        else:
            return self.socket.sendpacket(self.server, packet=packet, host=host, port=port, connected=connected, auto_close=auto_close, encoding=encoding)


    def close(self):
        # terminate connection
        return self.socket.close(self.socket)

    def recv(self, bufsize):
        # receive data
        return self.socket.recv(self.socket, bufsize=bufsize)

server = Server()