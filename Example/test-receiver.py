import numpy as np
import time

from binarySerialReceiver import binaryReceiver

def main():
  """ Defines the serial port """
  """ Would be something like /de/ttyUSB0 or COM5 on linux and windows respectively. """
  port = './virtual-tty-recv'

  """ Defines the arrays length """
  len = 100
  a = np.array([0] * len)
  b = np.array([0] * len)
  c = np.array([0] * len)

  """ Initializes the receiver object """
  receiver = binaryReceiver([a, b, c], 'fff', port, 115200, packetHeader=b'\xFD\xFE')
  
  try:
    """ Start the receiving thread """
    receiver.start()
  except Exception:
    """ Exits if fails to fin the serial port """
    exit()

  try:
    while(1):
      print(a)
      time.sleep(0.5)
  except KeyboardInterrupt:
    """ Recommend to call stop when KeyboardInterrupt happens 
        so the background thread wonk keep active """
    receiver.stop()

if __name__ == '__main__':
  main()