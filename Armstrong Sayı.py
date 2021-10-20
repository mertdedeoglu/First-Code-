sayımız=input("Lütfen bir sayı giriniz:")
list=[i for i in sayımız]
b=len(list)
toplam=0
for a in list:
    carpım=int(a)**b
    toplam+=carpım

if toplam==int(sayımız):
    print("Armstrong Sayı,",sayımız)
else:
    print("Bu bir armstrong sayı değildir.")
