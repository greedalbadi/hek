# Hek



### Installation.

```bash
pip install hek
```





#### Simple code to check if ip does exist or not.

```python
import hek

ip = "192.168.0.1" # targeted ip address

result = hek.checkip(ip) # checking if ip exist, It'll return True is exist and False if not.

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

result = hek.checkrdp(ip) # checking if device is rdp by the device ip.

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

result = hek.checkssh(ip) # checking if device is shh by the device ip

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

result = hek.portscan(ip=ip, port=port, timeout=3) # checking if opened port or not


if result == True:
    print("Opened port.")
elif result == False:
    print("Closed port.")
```

#### Code to grab site ip address.

```python
import hek

url = "github.com" # targeted url

ip = hek.siteip(url) # grap ip by url

print(ip)
```





This program uses MIT license. 