isim = "Usak Universtesi"
ara = "ver"

if isim.find(ara)>-1:
    bul = isim.find(ara)
    basla =  bul-1
    bitir = bul+len(ara)+1
    print(isim[basla:bitir])
else:
    print("bulunamadı")