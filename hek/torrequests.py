import requests
import urllib.request
from .exceptions import *
from .info import httpbin
import json
import socket
from .ipstuff import ipstuff
import socks


class _torinfo:
    # 9050 is the default tor proxy port
    default_port = "9050"
    # 127.0.0.1's is the default ip for tor proxy
    default_ip = "127.0.0.1"
    # combine the default port and the default ip
    default_host = f"{default_ip}:{default_port}"

class _session:

    # function to return your tor proxy identity
    def identity(self, host: str=_torinfo.default_host):

        # extract host ip from host string
        ip = host.split(":")[0]
        # extract host port from host string
        port = int(host.split(":")[1])

        # setting default proxy
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, ip, port)

        # setting socket
        socket.socket = socks.socksocket

        # get httpbin url to return ip
        url = httpbin.IP
        # request data
        req = urllib.request.urlopen(url)
        # encode data
        encode = req.info().get_content_charset('utf-8')

        # load data as json
        data = json.loads(req.read().decode(encode))
        # extract ip from data
        identity_ip = data["origin"]
        # lookup ip info
        ip_info = ipstuff.ipinfo(ip=identity_ip)

        # add new data into data dictionary
        data["country"] = ip_info["country"]
        data["city"] = ip_info["city"]
        data["timezone"] = ip_info["timezone"]

        # return data
        return data

class _Tor:


    # request session and adding tor proxy
    def get_session(self, host: str = _torinfo.default_host):

        # request session
        session = requests.session()
        # add tor proxy
        session.proxies = {'http': f'socks5://{host}',
                           'https': f'socks5://{host}'}

        _sess = _session()
        # return session to use
        setattr(session, "identity", _sess.identity)
        return session

    # end sesssion function
    def close_session(self, session):
        # close session
        session.close()


    # checking if proxy tor proxy is running
    def check(self, ip: str=_torinfo.default_ip, port: int=_torinfo.default_port):

        # configure socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # connect to server
        connect = sock.connect_ex((ip, int(port)))

        # checking if It's alie
        if (connect == 0):

            sock.close()
            return "Alive"

        else:
            # else exception
            raise SocketConnectionError("Socket connection error")
tor = _Tor()
