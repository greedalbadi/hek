# Hek



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



This program uses MIT license. 

