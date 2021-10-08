print("""
Hesap Makinesi
İşlemler; 
1. Toplama
2. Çıkarma
3. Çarpma
4. Bölme
""")

a=int(input("İlk sayı:"))
b=int(input("İkinci sayı:"))

işlem=input("İşlem giriniz:")
if işlem == "1":
    print("{} ile {} toplamı {}'dır.".format (a,b,a+b))
elif işlem == "2":
    print("{} ile {} çıkarması {}'dır.".format(a, b, a - b))
elif işlem == "3":
    print("{} ile {} çarpımı {}'dır.".format (a,b,a*b))
elif işlem == "4":
    print("{} ile {} bölmesi {}'dır.".format (a,b,a/b))
else:
    print("Geçersiz İşlem")
