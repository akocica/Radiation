import serial
import datetime
from time import time_ns


port = serial.Serial('/dev/ttyUSB0')
print("connected to: " + port.portstr)

t = 0
i = 0

file = datetime.datetime.now().strftime("geiger_%Y%m%d_%H%M%S.txt")
f = open(file , "a")

while True:
	d = port.read()
	if len(d) > 0:
		c = d.decode('utf-8')
		if c in ['0','1']:
			ns = time_ns()
			if i > 0:
				s ='{}\t{}\t{}\t{}\n'.format(i, c, ns-t, ns)
				f.write(s)
				f.flush()
			t = ns
			i+=1