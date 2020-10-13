import socket
import struct

vortex_socket = socket.socket()
vortex_socket.connect(("vortex.labs.overthewire.org", 5842))

numbersInNetworkOrder = []
for _ in range(4):
    numbersInNetworkOrder.append(vortex_socket.recv(4))

numbersInHostOrder = map(lambda x: struct.unpack("<I", x)[0], numbersInNetworkOrder)

vortex_socket.send(struct.pack("<I", sum(numbersInHostOrder)))

print vortex_socket.recv(100000000)
