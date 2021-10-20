import random
import time

print("""******* Oyunumuza Hoşgeldiniz ******""")

rastgele=random.randint(1,50)
hakkımız=7
while hakkımız!=0:
    sayınız=int(input("Tahmininiz:"))
    if sayınız<rastgele:
        print("Sorgulanıyor...")
        time.sleep(2)
        print("Lütfen daha büyük bir sayı söyleyiniz.")
        hakkımız-=1
    elif sayınız>rastgele:
        print("Sorgulanıyor...")
        time.sleep(2)
        print("Lütfen daha küçük bir sayı söyleyiniz.")
        hakkımız-=1
    else:
        print("Sorgulanıyor...")
        time.sleep(2)
        print("Tebrikler Doğru Bildiniz. Sayımız: ",rastgele)
        break
    if hakkımız==0:
        print("Hakkınız bitmiştir. Lütfen daha sonra tekrar deneyiniz.")
