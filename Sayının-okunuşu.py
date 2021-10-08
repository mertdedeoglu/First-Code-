birler = [" ","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
onlar = [" ","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]

def okunma(sayı1):
    birinci=sayı1%10
    ikinci=sayı1//10

    return onlar[ikinci] + " " + birler[birinci]

sayı1=int(input("Sayı giriniz:"))
print(okunma(sayı1))
