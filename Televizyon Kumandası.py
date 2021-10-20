import random
import time

class Kumanda():
    def __init__(self,tvdurum="Açık",tvses = 0,kanallistesi = "TRT",kanal = "TRT") :
        self.tvdurum= tvdurum
        self.tvses = tvses
        self.kanallistesi = kanallistesi
        self.kanal = kanal
    def tvac(self):
        if (self.tvdurum == "Açık"):
            print("Televizyon zaten açık")
        else:
            print("Televizyon Açılıyor...")
            self.tvdurum = "Açık"
    def tvkapat(self):
        if (self.tvdurum == "Kapalı"):
            print("Televizyon zaten kapalı")
        else:
            print("Televizyon Kapanıyor...")
            self.tvdurum="Kapalı"
    def sesayar(self):
        while True:
            cevap= input("Sesi azaltmak için : <\n Sesi arttırmak için : >\nÇıkış için: çıkış")
            if (cevap=="<"):
                if (self.tvses!=0):
                    self.tvses-=1
            elif (cevap==">"):
                if(self.tvses!=32):
                    self.tvses+=1
            else:
                print("Ses güncellendi :",self.tvses)
                break
    def kanalekle(self,kanalismi):
        print("Kanal Ekleniyor...")
        time.sleep(1)
        self.kanallistesi.append(kanalismi)
        print("Kanal Eklendi.")
    def rastgelekanal(self):
        rastgele = random.randomint(0,len(self.kanallistesi)-1)
        self.kanal=self.kanallistesi(rastgele)
        print("Şuanki kanal",self.kanal)
    def __len__(self):
        return len(self.kanallistesi)
    def __str__(self):
        print("Tv durumu : {}\nTv ses : {}\nKanal Listesi : {}\nŞuanki Kanal: {}\n".format(self.tvdurum,self.tvses,self.kanallistesi,self.kanal))
kumanda = Kumanda()
print("""
Televizyon Uygulaması
1. Tv Aç
2. Tv Kapat
3. Ses Ayarları
4. Kanal Ekle
5. Kanal Sayısını Öğrenme
6. Rastgele Kanal Geçme
7. Televizyon Bilgileri
Çıkış için 'q' ya basın.
""")
while True:
    işlem=input("İşlemi Seçiniz:")
    if (işlem=="q"):
        print("Program Sonlandırılıyor")
        break
    elif (işlem=="1"):
        kumanda.tvac()
    elif (işlem=="2"):
        kumanda.tvkapat()
    elif (işlem=="3"):
        kumanda.sesayar()
    elif (işlem=="4"):
        kanalismi=input("Kanal isimlerini , ile ayırarak girin:")
        yeniliste = kanalismi.split(",")
        for eklenecekler in yeniliste:
            kumanda.kanalekle(eklenecekler)
    elif (işlem=="5"):
        print("Kanal listesi :",len(kumanda))
    elif (işlem=="6"):
        kumanda.rastgelekanal()
    elif (işlem=="7"):
        print(kumanda)
    else:
        print("Geçersiz İşlem")
