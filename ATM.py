print("""
ATM Makinesine Hoşgeldiniz
İşlem için;
1. Bakiye Sorgulama
2. Para Yatırma
3. Para Çekme
Programdan çıkmak için q ya basınız.""")
anapara=1500
while True:
    ıslem=input("Lütfen işleminizi seçiniz:")
    if ıslem=="q" or ıslem=="Q":
        print("Yine Bekleriz.")
    elif ıslem=="1":
        print("Bakiyeniz {} Tl".format(anapara))
    elif ıslem=="2":
        mıktar=int(input("Lütfen Miktarı Yazınız:"))
        anapara += mıktar
        print("Paranız Yatırılmıştır. Bakiyeniz {}TL olarak güncellenmiştir.".format(anapara))
    elif ıslem=="3":
        mıktar = int(input("Lütfen Çekme Miktarını Yazınız:"))
        if anapara-mıktar<0:
            print("Bu miktarda para çekemezsiniz lütfen tekrar deneyiniz.")
            continue
        anapara-=mıktar
        print("{} TL çekilmiştir.Bakiyeniz {} TL olarak güncellenmiştir.".format(mıktar,anapara))
