import os
import socket
from .exceptions import *
import subprocess



class DefaultInfo:
    stdout = subprocess.DEVNULL
    stderr = subprocess.DEVNULL

class ipstuffclass:

    def siteip(url: str):
        try:
            if len(url) != 0: # check url length if not 0
                hostname = socket.gethostbyname(url) # grab host url
                return hostname
            else:
                raise LengthError("Invalid url length") # Invalid url length error.
        except:
            raise SiteHostNameRequestError("Request host name error") # Request host name error


    def portscan(ip: str, port: int, timeout=3):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create socket
        s.settimeout(int(timeout)) # set timeout
        conn = s.connect_ex((ip, port)) #connect to ip/port
        if (conn == 0): # if conn not 0 connection closed
            return True
        else:
            return False


    def checkrdp(ip: str, timeout=3):
        port = 3389 # the specific port for rdp
        return ipstuffclass.portscan(ip, port, timeout) # checking if port is open


    def checkssh(ip: str, timeout=3):
        port = 22 # the specific port for ssh
        return ipstuffclass.portscan(ip, port, timeout) # checking if port is open


    def checkip(ip: str):
        if os.name == "nt": # checking if windows os or else..
            command = f"ping {ip} -n 1"
        else:
            command = f"ping {ip} -c 1"
        res = subprocess.Popen(command, stdout=DefaultInfo.stdout, stderr=DefaultInfo.stderr) # run the command
        res.wait()
        if res.returncode == 0: # if return code is 0 there was no error on the ping else there is an error
            return True
        else:
            return False

ipstuff = ipstuffclass