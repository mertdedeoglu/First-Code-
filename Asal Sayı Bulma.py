def asalmı(sayı):
    if (sayı==1 or sayı==0):
        return False
    elif (sayı==2):
        return True
    else:
        for i in range(2,sayı):
            if sayı%i==0:
                return False
        return True
while True:
    sayı=input("Sayı:")
    if sayı=="q":
        break
    else:
        sayı=int(sayı)
        if asalmı(sayı):
            print(sayı,"Asaldır.")
        else:
            print(sayı,"Asal değildir.")
