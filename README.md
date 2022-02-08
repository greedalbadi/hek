[![logo](hek-logo.png)](https://pepy.tech/project/hek)

# Hek
[![Downloads](https://pepy.tech/badge/hek)](https://pepy.tech/project/hek)
[![LICENSE](https://img.shields.io/badge/LICENSE-MIT-g)](https://pepy.tech/project/hek)
[![Python](https://img.shields.io/badge/Python-3.9-blue)](https://pepy.tech/project/hek)
###### A python library mostly used for pentesting and automation some tasks.

###### Hek library is not near to be completed It's under constant updates. 

### Installation.

```bash
pip install hek
```





# System.



#### Get device current username.

```python
import hek

# get device current username
user = hek.system.username()

# print username
print(user)
```

#### Request device os name.

```python
import hek

os_name = hek.system.oname()
print(os_name)
```

#### Download content.

###### You could not add any path and It'll extract the file name from the url.

```python
from hek import system

# new file path
path = "dog.jpg"
# file url
url = "https://example/dog_picure.jpg"
# download content
result = system.download_content(url=url, path=path)
# print result
print(result)
```

## System - process.

#### kill process

###### You could change the name argument to process pid like (pid="1234"), also you could disable kill with force using force=False.

```python
import hek

# process name
name = "chrome.exe"

# kill process
res = hek.system.process.kill_process(name=name)

print(res)
```

### Get process PID by process name.

```python
from hek import system

# targeted process name\user
name = "chrome.exe"
# will return process PID\ID
name = system.process.getnamebypid(name=pid)
# print process PID\ID
print(name)
```

### Get process name by PID.

```python
from hek import system

# targeted process PID\id
pid = "2779"
# will return process name
name = system.process.getnamebypid(pid=pid)
# print process name
print(name)
```







# Proxy usages.





#### Doing http request using tor proxy

###### With this way you can do all kinds of requests like post/get/options, before using the function you need to setup and run tor bundle you could download it from tor official site

```python
import hek

# request tor session
tor_session = hek.tor.get_session()

# tor get request
result = tor_session.get("http://httpbin.org/ip").text

# print result
print(result)
```

##### You may add your host/proxy manually using this way, Identity is your proxy location contain some other info. 

```python
import hek

# adding host manually
host = "127.0.0.1:9050"

# request session
session = hek.tor.get_session(host=host)
# request your proxy identity..
identity = session.identity(host=host)
# print proxy identity
print(identity)
```

###### This code result your proxy identity.



#### Simple function to check if proxy is working.

```python
import hek


result = hek.proxy.checkproxy( # function to check if proxy is working
    url="https://github.com/", # targeted url
    user_agent="Mozilla/5.0", # user agent
    proxy="185.61.94.65:61616" #  HTTP/HTTPS proxy
    )
if "Working" in result: # It'll return Working if It's alive end exception if not
    print("Alive proxy")
```

It'll return Working if It's alive end exception if not





# Ip stuff.



#### Code to grab site ip address.

```python
import hek

url = "github.com" # targeted url

ip = hek.ipstuff.siteip(url) # grap ip by url

print(ip)
```



#### Code to check if opened port.

```python
import hek

ip = "192.168.0.1" # targeted device ip address

port = 80 # targeted port

result = hek.ipstuff.portscan(ip=ip, port=port, timeout=3) # checking if opened port or not


if result == True:
    print("Opened port.")
elif result == False:
    print("Closed port.")
```



#### Checking if device SSH by device ip.

```python
import hek

ip = "192.168.0.1" # targeted device ip address

result = hek.ipstuff.checkssh(ip) # checking if device is shh by the device ip

if result == True:
    print("is ssh")
elif result == False:
    print("isn't ssh")
```



#### Simple code to check if device is rdp by device ip address.

```python
import hek

ip = "192.168.0.1" # targeted device ip address

result = hek.ipstuff.checkrdp(ip) # checking if device is rdp by the device ip.

if result == True:
    print("is rdp")
elif result == False:
    print("isn't rdp")
```



#### Simple code to check if ip does exist or not.

```python
import hek

ip = "192.168.0.1" # targeted ip address

result = hek.ipstuff.checkip(ip) # checking if ip exist, It'll return True is exist and False if not.

if result == True:
    print("ip exist")
elif result == False:
    print("ip doesn't exist")
```

It'll return True is exist and False if not.

#### Get public ip.

```python
import hek

# get ip 
ip = hek.ipstuff.myip(find="query")

# print ip
print(ip)
```

you could get your ip information by removing find="query"  also you can change query and get other info about your ip.



# Server.





#### Check if server port is open.

```python
import hek

# server ip
ip = "192.168.0.1"
# targeted port
port = 80
# check
result = hek.server.portscan(ip=ip, port=port)
print(result)
```



#### Retrieve server banner.

```python
import hek

# server ip
ip = "192.168.0.1"
# targeted port
port = 430
# check
result = hek.server.get_banner(address=ip, port=port)
print(result)
```





## server.set_socket.

##### server.set_socket is a static way like a session that you only need to add the server info once to start sending and receiving data, unlike server.socket which is not static at all.

### Connect to a server.

```python
import hek

# server ip
ip = "192.168.0.1"
# server port
port = 80
# set server data
server = hek.server.set_socket(host=ip, port=port)

# connect to server
r = server.connect()
print(f"connected: {r}")
```



### Send packet to a server.

```python
import hek
# server ip
ip = "192.168.0.1"
# server port
port = 80
# set server data
server = hek.server.set_socket(host=ip, port=port)
# connect to server
r = server.connect()
print(f"connected: {r}")
# the packet

packet = "hi im packet"
# send packet
result = server.sendpacket()
print(result)
```



### Receive data from a server.

```python
data = server.recv(bufsize=1048)

print(data)
```



### Close connection.

```python
server.close()
```



# server.socket.

#### server.socket unlike set_socket It's unstatic better to work with it while using multiple socket's and multithreading.



## Create a socket.

```python
from hek import server
# get the server value
server = server.socket()
# create socket
sock = server.socket()
```

### connect to a server.

```python
# connect to a server
result = server.connect(sock, host="192.168.0.1", port=80)
# connection result True if connected
print(result)
```

### send packet.

```python
# the packet
packet = "im a packet"
# send packet
result = server.sendpacket(sock, packet=packet, host="192.168.0.1", port=80)
print(result)
```

### Receive data.

```python
# receive data
server.recv(sock, bufsize=1048)
```

### Close connection.

```python
# close connection
server.close(sock)
```









# Network and trafficking.







#### Sniff  and monitor any device traffic on your network.

```python
import hek, threading

# start sniffing network
def sniff():
    hek.network.arp.start_arp(
        # your interface mostly It'll be wlan0
        interface="wlan0",
        # ip of the router that the device is connected to
        router="192.168.0.1",
        # device ip address that you want to sniff
        device="192.168.0.112"
    )

# this function will run wireshark according to the entered data
def monitor_traffic():
    
    hek.wireshark.monitor_device(
        # your interface mostly It'll be wlan0
        interface="wlan0",
        # device ip address
        device="192.168.0.112" 
    )
    
threading.Thread(target=monitor_traffic).start() # run wireshark
threading.Thread(target=sniff).start() # start sniffing
```

##### You can use this if you just want to sniff device traffic without needing to open wireshark.

```python
import hek

# start sniffing network
def sniff():
    hek.network.arp.start_arp(
        # your interface mostly It'll be wlan0
        interface="wlan0",
        # ip of the router that the device is connected to
        router="192.168.0.1",
        # device ip address that you want to sniff
        device="192.168.0.112"
    )
sniff()
```



#### Connect to wifi using hek library.

This function is for linux also requires wifi adapter.

```python
import hek

# connect to wifi
result = hek.wifi.connect(ssid="Wifi ssid/Name", # wifi ssid/name
                          password="wifi-password" # wifi password
                          )
# connection result
print(result) 
```



#### Start monitor mode.

This function for linux.

```python
import hek

# Start monitor mode
result = hek.net.monitor_start(name="wlan0")

# Output
print(result)
```



#### Stop monitor mode.

This function for linux.

```python
import hek

# stop monitor mode
result = hek.net.monitor_stop(name="wlan0mon")

# Output
print(result)
```











## Recording , videos, images stuff.

###### While recording a video you could display your choice of fps like fps=30 or 60 or higher.

#### Extracting image exif data.

```python
import hek

data = hek.Image.extracexif(filename="hek.jpg") # grab exif data

print(data) # print data
```



#### Screen shot.

```python
import hek

hek.screen.screenshot(filename="test.png")
```

#### Webcam picture.

```python
import hek

hek.webcam.webcamshot(filename="test.png")
```

#### Screen video capture.

```python
import hek

hek.screen.capture_video(filename="filename.avi", seconds=5)
```

#### Webcam video capture.

```python
import hek

hek.webcam.capture_video(filename="webname.avi", seconds=3)
```

This program uses MIT license. 

