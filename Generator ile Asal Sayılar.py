def asalsayı():
  
  for sayı in range(2,1000):
    i=2
    durum=0
    while (sayı>i):
      if (sayı%i==0):
        durum+=1
      i+=1
    if (durum==0):
      yield sayı

generator = asalsayı()

for a in generator:
  print(a)
