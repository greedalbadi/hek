import socket
from exceptions import *
class Server:
    def get_banner(self, address: str, port: str, timeout: int=5):
        s = socket.socket()
        s.settimeout(timeout)
        try:
            s.connect((address, port))
            return s.recv(1024).decode()
        except socket.timeout:
            raise SocketConnectionError("Time out")
        except socket.error as exc:
            raise SocketConnectionError(f"connection error: {exc}")


    def portscan(ip: str, port: int, timeout=3):
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
