import subprocess
import os
from .info import Tools
from .exceptions import *

class Connect_sub:
    shell = True # is shell
    stdout = subprocess.PIPE # being able to read response
    stderr = subprocess.DEVNULL # throw error to null
    found_return = "successfully activated"
    op = ["nt"] # not supported os list (I didn't add all unsupported os's)
class Wifi:
    def connect(self, ssid: str, password: str=None): # connect to network function
        if os.name in Connect_sub.op: # making sure that os supported
            raise OperatingSystemERROR("this operating system is not supported")
        if password == None: # checking if uses password or not (value change)
            result =  wifi.ssid_only( ssid)
        else:
            result = wifi.secret_connect( ssid, password)

        if "successfully activated" in result: # checking command result
            return "Connected"
        else:
            return "Failed"

    def ssid_only(self, ssid): # this function will run if network not using secret/password
        command = Tools.nmcli.SSID_ONLY.replace("(ssid)", ssid) # adding ssid to command
        # running the command
        result = subprocess.Popen(
            command,
            shell=Connect_sub.shell,
            stdout=Connect_sub.stdout,
            stderr=Connect_sub.stderr
        ).stdout.read().decode()
        return result

    def secret_connect(self, ssid, password): # It'll run if ssid and password are both entered
        # adding ssid and password to command.
        command = Tools.nmcli.SECRET_CONNECT.replace("(ssid)", ssid).replace("(secret)", password)
        # running the command
        result = subprocess.Popen(
            command,
            shell=Connect_sub.shell,
            stdout=Connect_sub.stdout,
            stderr=Connect_sub.stderr
        ).stdout.read().decode()
        return result
# naming class
wifi = Wifi()