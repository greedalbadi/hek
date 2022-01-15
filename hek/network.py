import subprocess
import os
from .info import Tools
from .exceptions import *


class Net_info: # info container
    op = ["nt"]
    # thous who contain monitor_ are for monitor functions
    monitor_shell = True # is shell
    monitor_stdout = subprocess.PIPE # being able to read response
    monitor_stderr = subprocess.DEVNULL # throw error to null
    # thous who contain arp_ are for Arp functions
    arp_shell = True
    arp_stdout = subprocess.DEVNULL
    arp_stderr = subprocess.DEVNULL
    arp_device = None
    arp_router = None

    # thous who contain wireshark_ are for wireshark functions
    wireshark_shell = True
    wireshark_stdout = subprocess.DEVNULL
    wireshark_stderr = subprocess.DEVNULL
    wireshark_device = None
class Net:
    def monitor_start(self, name: str="wlan0"):
        if os.name in Net_info.op: # making sure that os supported
            raise OperatingSystemERROR("this operating system is not supported")
        # process command and adding adapter name
        command = Tools.aircrack.MONITOR_START + ' ' + name
        # running command then read and decode it
        result = subprocess.Popen(
            command,
            shell=Net_info.monitor_shell,
            stdout=Net_info.monitor_stdout,
            stderr=Net_info.monitor_stderr
        ).stdout.read().decode()
        # return command decoded result
        return result

    def monitor_stop(self, name: str = "wlan0mon"):
        if os.name in Net_info.op:  # making sure that os supported
            raise OperatingSystemERROR("this operating system is not supported")
        # process command and adding adapter name
        command = Tools.aircrack.MONITOR_STOP + ' ' + name
        # running command then read and decode it
        result = subprocess.Popen(
            command,
            shell=Net_info.monitor_shell,
            stdout=Net_info.monitor_stdout,
            stderr=Net_info.monitor_stderr
        ).stdout.read().decode()

        # return command decoded result
        return result



class Arp:

    def start_arp(self, interface: str="wlan0", router:str=Net_info.arp_router, device:str=Net_info.arp_device):
        if os.name in Net_info.op:  # making sure that os supported
            raise OperatingSystemERROR("this operating system is not supported")

        # process command and adding interface name, router ip and device ip
        command = Tools.ettercap.ARP_START.replace("(interface)", interface).replace("(router)", router).replace("(device)", device)
        result = subprocess.Popen(
            command,
            shell=Net_info.arp_shell,
            stdout=Net_info.arp_stdout,
            stderr=Net_info.arp_stderr
        )

        result.wait()
        # If command interrupted error
        if result.returncode != 0:
            raise ArpError("running Arp error.")

        return "ended"

class Wireshark:


    def monitor_device(self, interface: str="wlan0", device:str=None, http=False):
        if os.name in Net_info.op:  # making sure that os supported
            raise OperatingSystemERROR("this operating system is not supported")

        # process command and adding interface and device ip
        command = Tools.wireshark.MONITOR_DEVICE.replace("(interface)", interface).replace("(device)", device)


        # running command
        result = subprocess.Popen(
            command,
            shell=Net_info.wireshark_shell,
            stdout=Net_info.wireshark_stdout,
            stderr=Net_info.wireshark_stderr
        )
        result.wait() # wait for command end

        # return command status code
        return result.returncode


net = Net()
arp = Arp()
wireshark = Wireshark()