import serial
import matplotlib.pyplot as plt
import numpy

# pl = plt.plot([], [], 'ro')
# i = [0.02, 0.03]
a = 5
# def update_line(hl, new_data):
#     hl.set_xdata(numpy.append(hl.get_xdata(), new_data))
#     hl.set_ydata(numpy.append(hl.get_ydata(), new_data))
#     # plt.draw()
#     plt.show()
line_value1 = 0.0
line_value2 = 0.0
plt.ion()
plt.axis([0, 10, 0, 10])
pl, = plt.plot([line_value1], [line_value2], 'ro')
plt.pause(0.000001)
# plt.show()
with serial.Serial('/dev/tty.usbmodem1411', 115200, timeout=1) as ser:
    while True:
        print "Hello\n"
        line = ser.readline()
        if(a > 10):
            print line,
            if(line != ""):
                line_value1 = float(line)
                print "line value 1 = ",
                print line_value1
                line_value2 = line_value1
        	value = [line_value1, line_value2]
        	pl.set_xdata(line_value1)
        	pl.set_ydata(line_value2)
        	plt.pause(0.000001)
        	plt.draw()
        	# print value
        a = a + 1
ser.close()