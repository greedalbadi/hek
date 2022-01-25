[![Downloads](https://pepy.tech/badge/hek)](https://pepy.tech/project/hek)
[![LICENSE](https://img.shields.io/badge/LICENSE-MIT-g)](https://pepy.tech/project/hek)
[![Python](https://img.shields.io/badge/Python-3.9-blue)](https://pepy.tech/project/hek)
# Hek

###### A python library mostly used for pentesting and automation some tasks.

### Installation.

```bash
pip install hek
```



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

#### Ge device current username.

```python
import hek

# get device current username
user = hek.system.username()

# print username
print(user)
```

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

if device is rdp by the device ip.

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

#### Code to grab site ip address.

```python
import hek

url = "github.com" # targeted url

ip = hek.ipstuff.siteip(url) # grap ip by url

print(ip)
```



#### Extracting image exif data.

```python
import hek

data = hek.Image.extracexif(filename="hek.jpg") # grab exif data

print(data) # print data
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



#### Doing http request using tor proxy

##### With this way you can do all kinds of requests like post/get/options, before using the function you need to setup and run tor bundle you could download it from tor official site

```python
import hek

# request tor session
tor_session = hek.tor.get_session()

# tor get request
result = tor_session.get("http://httpbin.org/ip").text

# print result
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

#### Request device os name

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

This program uses MIT license. 

