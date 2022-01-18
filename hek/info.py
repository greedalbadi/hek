
class sock:
    DEFAULT_SOCKET_TIMEOUT = 10
    RDP_PORT = 3389
    SSH_PORT = 22


class httpbin:
    IP = "http://httpbin.org/ip"

class system:
    WIN_DEFAULT_CMD_SAFE_RETURNCODE = 0
    LINUX_DEFAULT_CMD_SAFE_RETURNCODE = 0
class request:
    DEFAULT_REQUEST_TIMEOUT = 10

class Tools:
    class nmcli:
        SSID_ONLY = "sudo nmcli dev wifi connect (ssid)"
        SECRET_CONNECT = 'sudo nmcli dev wifi connect (ssid) password "(secret)"'

    class aircrack:
        MONITOR_START = "airmon-ng start"
        MONITOR_STOP = "airmon-ng stop"

    class ettercap:
        ARP_START = "sudo ettercap -T -S -i (interface) -M arp:remote /(router)// /(device)//"

    class wireshark:
        MONITOR_DEVICE = 'wireshark -i (interface) -k -Y "ip.addr == (device)"'


class API:
    IPINFO_API = 'http://ip-api.com/json'