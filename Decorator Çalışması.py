def ekstra(func):
  print("Mükemmel sayılar")
  def wrapper():
    for sayı in range(1,1001):
      i=1
      toplambölen=list()
      
      while sayı >= i:
        if sayı%i==0:        
          toplambölen.append(i)
        i +=1
      if (sayı*2)==(sum(toplambölen)):
        print(sayı)
    func()
  return wrapper    

@ekstra
def asalsayıbul():
  asalsayılar=[]
  print("Asal Sayılar...")
  for sayı in range(2,1000):
    i=2
    sayaç=0
    while (i<sayı):
      if sayı%i==0:
        sayaç+=1
      i+=1
    if sayaç==0:
      asalsayılar.append(sayı)
  print(asalsayılar) 

asalsayıbul()
