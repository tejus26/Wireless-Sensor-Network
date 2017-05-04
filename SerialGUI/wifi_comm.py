
import serial
import matplotlib.pyplot as plt
import localization as lx
import time
from mpl_toolkits.mplot3d import Axes3D
import sys
import telnetlib

import numpy as np

a = 5

line_value1 = 0.0
line_value2 = 0.0
line_value3 = 0.0

#Adding 3D PLOT
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
c = 'b'
m = 'o'

ax.set_xlim3d(0, 12)
ax.set_ylim3d(0,12)
ax.set_zlim3d(0,12)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.scatter(0.0, 0.0, 0.0, c=c, marker=m)
plt.pause(0.000000001)
plt.show()
tn = telnetlib.Telnet("192.168.240.1")


while True:
    line = tn.read_until("\n")
    print line