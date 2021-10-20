print("""Faktoriyel Hesaplama\nÇıkmak için q'ya basınız.""")


while True:
    sayı = input("Lütfen bir sayı giriniz:")

    if sayı=="q" or sayı=="Q":
        print("Çıkış Yapılıyor....")
        break
    else:
        sayı=int(sayı)
        a=1
        for i in range(2,sayı+1):
            a*=i
        print("Faktöriyel = ",a)
        continue
