import subprocess
import os
from .info import Tools
from .exceptions import *


class Net_info: # info container
    # thous who contain monitor_ are for monitor functions
    monitor_shell = True # is shell
    monitor_stdout = subprocess.PIPE # being able to read response
    monitor_stderr = subprocess.DEVNULL # throw error to null
    op = ["nt"]



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
net = Net()