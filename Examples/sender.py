import serial
import struct
import time
import random as rnd

serialPort = 'virtual-tty-send'
serialBaud = 115200

print('Serial Emulator')
print('Trying to connect to: ' + str(serialPort) + ' at ' + str(serialBaud) + ' BAUD.')
try:
  serialConnection = serial.Serial(serialPort, serialBaud, timeout=4)
  print('Connected to ' + str(serialPort) + ' at ' + str(serialBaud) + ' BAUD.')
except:
  print("Failed to connect with " + str(serialPort) + ' at ' + str(serialBaud) + ' BAUD.')

fs = 4.5e3

it = 0.5
header = b'\xFD\xFE'
while (1):
  it += 1
  data = struct.pack('fff', it, rnd.choice(range(100)), rnd.choice(range(80,100)))
  serialConnection.write(header)
  serialConnection.write(data)
  time.sleep(1/fs)
