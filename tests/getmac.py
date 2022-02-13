''''import subprocess
import os

def getall():
    cmd = "arp -a"
    command = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

    stdout = command.stdout.read().decode('utf-8')
    d = {}
    for line in stdout.splitlines():
        result = line.split()
        try:
            print(result)
            d[result[0]] = result[1].replace("-", ":")
        except IndexError:
            pass
    print(d)

def getone(ip):
    cmd = 'arp -a "192.168.0.1"'

    if os.name == "nt":
        index = 1
    else:
        index = 3

    command = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

    stdout = command.stdout.read().decode('utf-8')
    for i in stdout.splitlines():
        i = i
    print(i.split()[index].replace("-", ":"))
getone()'''

import hek

add = hek.getmac.getmac("192.168.0.1")
print(add)





