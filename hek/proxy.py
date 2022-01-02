import urllib.request
from .exceptions import *
class Proxy:
    def Handle(self, proxy: str): # creating proxy handler.
        hand = {
            'http': f'http://{proxy}',
            'https': f'http://{proxy}',
        }
        return urllib.request.ProxyHandler(hand) # return proxy handler


    def checkproxy(self, url: str, proxy: str, user_agent: str, timeout: int = 15):
        try:
            headers = {}  # creating headers dict
            headers["User-Agent"] = str(user_agent) # adding user agent to dict
            request = urllib.request.Request(url, headers=headers) # creating request


            handler = Proxy.Handle(self, proxy) # requisting handler
            opner = urllib.request.build_opener(handler) # creating request creator


            opner.open(request, timeout=timeout) # running request
            return "Working" # if it got to this point it means that the proxy is alive
        except:
            raise ProxyFailed("Proxy failed")

proxy = Proxy()











# old test
'''
file = open("proxy.txt")
text = file.read().splitlines()
o = Proxy()
for ip in text:
    threading.Thread(target=o.checkproxy, args=[
        '',
        ip,
        '',
    ]).start()

url = ""
headers = {}
headers["User-Agent"] = ""
req = urllib.request.Request(url, headers=headers)
req.set_proxy("", "https")
res = urllib.request.urlopen(req)
print(res.read())

url = ""
headers = {}
headers["User-Agent"] = ""
req = urllib.request.Request(url, headers=headers)
proxy = ""
hnd = urllib.request.ProxyHandler({
    'http': f'http://{proxy}',
    'https': f'http://{proxy}',
})
opner = urllib.request.build_opener(hnd)
resp = opner.open(req)
print(resp.read())
'''