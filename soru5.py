komut = input("Değer giriniz : ")

komutlar = komut.split("\\n")

def birinci(deger):
    deger = int(deger)
    if deger >= 0 and deger <= 50:
        return "Çok zayıf sinyal"
    elif deger >= 51 and deger <= 100:
        return "Zayıf sinyal"
    elif deger >= 101 and deger <= 150:
        return "Orta Sinyal"
    elif deger >= 151 and deger <= 200:
        return "Güçlü Sinyal"
    elif deger >= 201 and deger <= 205:
        return "Çok güçlü sinyal"

def ikinci(deger):
    deger = int(deger)
    if deger == 1:
        return "Televizyon"
    elif deger == 2:
        return "Çamaşır makinesi"
    elif deger ==3 :
        return "buzdolabı"
    elif deger == 4:
        return "Fırın"
    else:
        return "Geçersiz"

def ucuncu(deger):
    deger=int(deger)
    if deger == 0:
        return "Off"
    elif deger == 1:
        return "On"
    else:
        return "Geçersiz"

def dorduncu(deger):
    deger = int(deger)
    if deger == 0:
        return "Cevap istenmiyor"
    elif deger == 1:
        return "Cevap isteniyor"
    else:
        return "Geçersiz"

for kod in range(len(komutlar)-1):
    parametre=komutlar[kod].split('-')

    if (parametre[0]=="send"):
        if len(parametre) == 5:
            if birinci(parametre[1]) =="Geçersiz":
                print("error : birinci bolum hatali")
                print(parametre[1])
            elif ikinci(parametre[2]) == "Geçersiz":
                print("error : ikinci bolum hatali")
            elif ucuncu(parametre[3]) == "Geçersiz":
                print("error : ucuncu bolum hatali")
            elif dorduncu(parametre[4]) == "Geçersiz":
                print("error : dorduncu bolum hatali")
            else:
                print("Kod Tipi : send - Giden")
                print("Sinyal Gücü : " + parametre[1] +" - "+birinci(parametre[1]))
                print("Cihaz : " + parametre[2] + " - " + ikinci(parametre[2]))
                print("Durumu : " + parametre[3] + " - " + ucuncu(parametre[3]))
                print("Cevap : " + parametre[4] + " - " + dorduncu(parametre[4]))
        else:
            print("error : kinci bölüm hatalı")

    elif parametre[0] == "receive":
        if len(parametre)==4:
            if birinci(parametre[1]) == "Geçersiz":
                print("error : birinci bolum hatali")
            elif ikinci(parametre[2]) == "Geçersiz":
                print("error : ikinci bolum hatali")
            elif ucuncu(parametre[3]) == "Geçersiz":
                print("error : dorduncu bolum hatali")
            else:
                print("Kod Tipi : receive - Gelen")
                print("Sinyal Gücü : " + parametre[1]+" - "+ ikinci(parametre[1]))
                print("Cihaz : " + parametre[2]+" - " + ucuncu(parametre[2]))
                print("Durumu : " + parametre[3]+" - " + dorduncu(parametre[3]))
        else:
            print("error : ikinci bölüm hatalı")
    else:
        print("error : send ya da receive içermiyor")

    print("-----")