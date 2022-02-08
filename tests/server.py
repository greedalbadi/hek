from hek import server


'''server = server.set_socket(host="192.168.0.1", port=80)

s = server.connect()
print(f"connected: {s}")

s2 = server.sendpacket(packet="niah")
print(s2)'''

from hek import server
# get the server value
server = server.socket()
# create socket
sock = server.socket()
# connect to a server
result = server.connect(sock, host="192.168.0.1", port=80)
# connection result True if connected
print(result)

# the packet
packet = "im a packet"
# send packet
result = server.sendpacket(sock, packet=packet, host="192.168.0.1", port=80)
print(result)

# close connection
server.close(sock)
# receive data
server.recv(sock, bufsize=1048)