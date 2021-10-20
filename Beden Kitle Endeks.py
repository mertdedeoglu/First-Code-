boy = float(input("Boyunuzu giriniz:"))
kilo = float(input("Kilonuzu giriniz:"))

bki = kilo/(boy*boy)
print("Beden kitle endeksiniz : {:.2f} ".format(bki))
if bki<= 18.5:
    print("**Zayıf**")
elif 18<bki<=25:
    print("**Normal**")
elif 25<bki<=30:
    print("**Fazla Kilolu**")
elif bki>30:
    print("**Obez**")
