import ctypes
import multiprocessing as mp
import time
import numpy as np
from numpy.core.multiarray import array

class TestClass():
  def __init__(self, l):
    self.l = l
    self.p = mp.Process(target=self.some_process)
    self.p.start()

  def stop(self):
    self.p.join()

  def some_process(self):
    i = 0
    while 1:
      i += 1 
      # self.l[0] += self.l[0]
      self.l[:] = [i] + self.l[:-1]

      time.sleep(0.5)

if __name__ == '__main__':
  mp.set_start_method('spawn')
  arr = mp.Array('d', 3)
  arr[0] = 1
  test = TestClass(arr)
  print(arr.__len__())
  np_arr = np.frombuffer(arr.get_obj())
  while 1:
    try:
      # print(list(arr))
      print(np_arr)
      time.sleep(0.5)
    except KeyboardInterrupt:
      test.stop()
      exit(0)
      



