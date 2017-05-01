import serial
import matplotlib.pyplot as plt
import localization as lx
import time
from mpl_toolkits.mplot3d import Axes3D

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
with serial.Serial('/dev/tty.usbmodem1411', 115200, timeout=1) as ser:
    while True:

        # print "Hello\n"
        ser.flushInput()
        line1 = ser.readline()
        line2 = ser.readline()
        line3 = ser.readline()
        line4 = ser.readline()

        print line1,
        print line2,
        print line3,
        print line4
        try:
            line1.split(' ') and line2.split(' ') and line3.split(' ') and line4.split(' ')
            id1, r1 = line1.split(' ')
            id2, r2 = line2.split(' ')
            id3, r3 = line3.split(' ')
            id4, r4 = line4.split(' ')
            print r1, 
            print id1
            print r2, 
            print id2
            print r3, 
            print id3
            print r4,
            print id4
            
            if((len(id1) == 8) and (len(id2) == 8) and (len(id3) == 8) and (len(id4) == 8)):
                try:
                    float(r1) and float(r2) and float(r3) #and float(r4)
                    P=lx.Project(mode='3D', solver='LSE')
                    P.add_anchor('FFFFFAFF', (0, 0, 0))
                    P.add_anchor('FFFFFBFF', (12.35, 0 , 0.0))
                    P.add_anchor('FFFFFCFF', (10.43, 5.73, 1.2))
                    P.add_anchor('FFFFFDFF', (9.31, 5.73, -0.72))
                    
                    # P.add_anchor('FFFFFAFF', (0, 0, 0))
                    # P.add_anchor('FFFFFBFF', (12, 0 , 0))
                    # P.add_anchor('FFFFFCFF', (10, 5, 3))
                    # P.add_anchor('FFFFFDFF', (8, 5, -2))
                    t,label=P.add_target()
                    r1 = float(r1)
                    r2 = float (r2)
                    r3 = float(r3)
                    r4 = float (r4)
                    t.add_measure(id1, r1)
                    t.add_measure(id2, r2)
                    t.add_measure(id3, r3)
                    t.add_measure(id4, r4)
                    # start = time.time()
                    P.solve()
                    # end = time.time()
                    # print (end - start)
                    # print r1, 
                    # print id1
                    # print r2, 
                    # print id2
                    # print r3, 
                    # print id3
                    # print r4,
                    # print id4
                    # print "************"
                    # plt.gcf().clear()
                    print round(t.loc.x, 3),
                    print round(t.loc.y, 3),
                    print round(t.loc.z,3)
                    xs = round(t.loc.x, 3)
                    ys = round(t.loc.y, 3)
                    zs = round(t.loc.z, 3)
                    plt.cla()
                    ax.set_xlim3d(0, 12)
                    ax.set_ylim3d(0,12)
                    ax.set_zlim3d(0,12)
                    ax.set_xlabel('X axis')
                    ax.set_ylabel('Y axis')
                    ax.set_zlabel('Z axis')


                    ax.scatter(xs, ys, zs, c=c, marker=m)
                    plt.pause(0.000000001)
                    plt.show()

                except ValueError:
                    a = a + 1
        except ValueError:
            a = a + 1
ser.close()