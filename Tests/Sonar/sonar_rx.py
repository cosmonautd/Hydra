import socket
import sys

import matplotlib.pyplot as plt
import numpy as np
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.1.5', 3333)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

plt.ion()
fig, ax = plt.subplots()
plt.ylim([0, 250])

ydata = [0]*50
line, = plt.plot(ydata)

while True:
    try:
        data = sock.recv(1024)
        try:
            sonar_reading = (float(bytes.decode(data)))
        except:
            continue
        ydata.append(sonar_reading)
        #ymin = float(min(ydata))-10
        #ymax = float(max(ydata))+10
        #plt.ylim([ymin,ymax])
        del ydata[0]
        line.set_xdata(np.arange(len(ydata)))
        line.set_ydata(ydata)
        fig.canvas.draw()
        fig.canvas.flush_events()
    except Exception as e:
        print (str(e))
        print("Closing socket")
        sock.close()
        sys.exit()
