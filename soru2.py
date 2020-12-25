
adres = "www.alierbey.com"

uzantilar = ['.com', '.net', '.org', '.com.tr']

def adresdogrula(adres):
    for x in range(len(adres)) :
        for y in range(len(uzantilar)):
            if adres[x:] == uzantilar[y]:
                print("İnternet adresi doğrulandı ")
                return True
    else :
        print('bu bir adres değil')
        return False

adresdogrula(adres)