import ctypes
from select import select
import time
import struct
import copy
import logging
# from threading import Thread, Lock
import multiprocessing as mp

import serial
from serial.serialutil import Timeout

class binaryReceiver():
  def __init__(
      self, data: list, dataFormat: str, 
      serialPort: str, serialBaud: int, packetHeader=b'\xFD',
      packetBufferLen=100, onReceiveCallback=None, crcEnable=False
    ):
    self.outData = data
    self.dataFormat = dataFormat
    self.port = serialPort
    self.baud = serialBaud
    self.bufferLength = data[0].__len__()
    # print(self.bufferLength)
    self.header = packetHeader
    self.packetBufferLen = packetBufferLen
    self.onReceiveCallback = onReceiveCallback

    self.nData = data.__len__()
    
    """ Thread Variables """
    self.serialProcess = None
    self.isReceiving = mp.Value(ctypes.c_bool, False)
    self.isRun = mp.Value(ctypes.c_bool, False)
    self.isPaused = mp.Value(ctypes.c_bool, False)
    # self.updateLock = Lock()

    """ Serial Connection """
    self.serialConnection = None

  def start(self):
    if self.serialProcess == None:
      self.serialProcess = mp.Process(target=self.readingThread)
      self.serialProcess.start()
      logging.info('Reading thread started')
      # Block till we start receiving values
      while self.isReceiving.value != True:
        time.sleep(0.1)

  def pause(self):
    self.isPaused.value = True

  def resume(self):
    self.isPaused.value = False

  def stop(self):
    self.isRun.value = False
    self.serialProcess.join()
  
  def setReceiveCallback(self, onReceiveCallback):
    self.onReceiveCallback = onReceiveCallback

  def readingThread(self):
    logging.info(f'Connecting to {self.port} at {self.baud} BAUD.')
    try:
      self.serialConnection = serial.Serial(self.port, self.baud, timeout=0.1)
      logging.info('Connected')
    except Exception as e:
      logging.error(f'Failed to connect: {e}')
      raise e
    self.isRun.value = True

    packetHeaderLen = self.header.__len__()
    packetSize = struct.calcsize(self.dataFormat) + packetHeaderLen
    packets = 100
    # packets = self.packetBufferLen

    invalid = 0
    time.sleep(1.0)  # give some buffer time for retrieving data
    while (self.isRun.value): 
      dataValid = False
      while (dataValid == False):
        self.rawData = self.serialConnection.read(size=packets * packetSize)
        # self.serialConnection.flushInput()
        readLen = self.rawData.__len__()
        # print(readLen)
        if (bytes(self.rawData[:packetHeaderLen]) != self.header):
          self.serialConnection.reset_input_buffer()
          invalid += 1
          if (invalid > 10):
            logging.warn('Receiving invalid data')
        else:
          invalid = 0
          dataValid = True
      self.isReceiving.value = True
      
      unpacked_arr = [[], [], []]
      if (self.isPaused.value == False):
        n = int(readLen / packetSize) 
        for i in range(n):
          # with self.updateLock:
          privData = copy.deepcopy(self.rawData[i * (packetSize) + packetHeaderLen:(i + 1) * packetSize])
          unpacked = list(struct.unpack(self.dataFormat, privData))
          # print(unpacked)
          for i in range(self.nData):
            unpacked_arr[i] += [unpacked[i]]
        # print(unpacked_arr)
        for i in range(self.nData):
          self.outData[i][:] =  self.outData[i][n:] + unpacked_arr[i]

  


