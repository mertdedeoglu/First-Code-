class kareler():
  def __init__(self,max):
    self.max = max
    self.kuvvet = 0
  def __iter__(self):
    return self
  def __next__(self):
    if (self.max >= self.kuvvet):
      sonuc = self.kuvvet**2
      self.kuvvet+=1
      return sonuc
    else:
      self.kuvvet=0
      raise StopIteration
KARE=kareler(6)

for i in KARE:
  print(i)
