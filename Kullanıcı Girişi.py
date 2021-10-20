print("""*****************
Kullanıcı Girişi Programı
*****************""")
sys_kullanıcı_adı = "Mert"
sys_parola="12345"
hak=3
while True:
    kullanıcıadı=input("Kullanıcı Adınız:")
    parola=input("Parolanız:")
    if (kullanıcıadı==sys_kullanıcı_adı and parola!=sys_parola):
        print("Parolanız Yanlış")
        hak-=1
        print("Kalan Giriş Hakkınız",hak)
    elif (kullanıcıadı!=sys_kullanıcı_adı and parola==sys_parola):
        print("Kullanıcı Adınız Yanlış")
        hak-=1
        print("Kalan Giriş Hakkınız",hak)
    elif (kullanıcıadı != sys_kullanıcı_adı and parola != sys_parola):
        print("Kullanıcı Adı ve Parolanız Yanlış")
        hak-=1
        print("Kalan Giriş Hakkınız",hak)
    else:
        print("Sisteme giriş yapıldı")
        break
    if (hak==0):
        print("Lütfen daha sonra tekrar deneyiniz.")
        break
