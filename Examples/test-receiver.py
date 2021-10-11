import numpy as np
import time

from binarySerialReceiver import binaryReceiver

def main():
  port = './virtual-tty-recv'
  len = 100
  a = np.array([0] * len)
  b = np.array([0] * len)
  c = np.array([0] * len)
  receiver = binaryReceiver([a, b, c], 'fff', port, 115200, packetHeader=b'\xFD\xFE')
  
  try:
    receiver.start()
  except Exception:
    exit()

  try:
    while(1):
      print(a)
      time.sleep(0.5)
  except KeyboardInterrupt:
    receiver.stop()

if __name__ == '__main__':
  main()