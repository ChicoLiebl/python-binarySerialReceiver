import serial
import numpy as np
import struct
import copy

DATA_FORMAT='IHH'
PACKET_HEADER=b'\xFD'

if __name__ == '__main__':
  try:
    conn = serial.Serial('/dev/ttyACM0', '115200', timeout=0.1)
    print('Connected')
  except Exception as e:
    print(f'Failed to connect: {e}')
    exit()

  packetSize = struct.calcsize(DATA_FORMAT) + PACKET_HEADER.__len__()
  packets = 100

  while 1:
    try:
      invalid = 0
      dataValid = False
      readLen = 0
      while (dataValid == False):
        rawData = conn.read(size=packets * packetSize)
        # conn.flushInput()
        readLen = rawData.__len__()
        # print(readLen)
        if (bytes(rawData[:PACKET_HEADER.__len__()]) != PACKET_HEADER):
          conn.reset_input_buffer()
          invalid += 1
          if (invalid > 10):
            print(rawData)
            # print('Receiving invalid data')
          continue
        invalid = 0
        dataValid = True

      for i in range(int(readLen / packetSize)):
        privData = copy.deepcopy(rawData[i * (packetSize) + PACKET_HEADER.__len__():(i + 1) * packetSize])
        unpacked = list(struct.unpack(DATA_FORMAT, privData))
        print(unpacked)

    except KeyboardInterrupt:
      exit(0)