import subprocess
import os


class Getmac:

    def getmac(self, ip: int):

        if os.name == "nt":

            index = 1
        else:

            index = 3

        cmd = f'arp -a "{ip}"'

        return Getmac._getmac_command(self, cmd, index)



    def _getmac_command(self, cmd: str, index: int):

        command = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

        stdout = command.stdout.read().decode("utf-8")

        for i in stdout.splitlines():
            ''

        return i.split()[index].replace("-", ":")

getmac = Getmac()