import json
import os
import socket
from .exceptions import *
import subprocess
import urllib.request
from .info import (
    API,
    sock,
    request
)
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


    def checkrdp(ip: str, timeout=int(sock.DEFAULT_SOCKET_TIMEOUT)):
        port = int(sock.RDP_PORT) # the specific port for rdp
        return ipstuffclass.portscan(ip, port, timeout) # checking if port is open


    def checkssh(ip: str, timeout=int(sock.DEFAULT_SOCKET_TIMEOUT)):
        port = int(sock.SSH_PORT) # the specific port for ssh
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

    def ipinfo(ip: str, timeout: int= request.DEFAULT_REQUEST_TIMEOUT):
        if len(ip) == 0: # if input ip length is equal o 0
            raise LengthError("IP length error")
        url = API.IPINFO_API + "/" + ip # process request url
        try:
            request = urllib.request.urlopen(url, timeout=timeout) # preform request

            encode = request.info().get_content_charset('utf-8') # encode content

            data = json.loads(request.read().decode(encode)) # load content to json
            return data
        except Exception as error:
            raise error

ipstuff = ipstuffclass