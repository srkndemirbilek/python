def nothesapla(satır):
    satır=satır[:-1]
    liste = satır.split(':')
    ogradı=liste[0]
    notlar=liste[1].split(',')
    not1=int(notlar[0])
    not2=int(notlar[1])
    not3=int(notlar[2])
    ort=(not1+not2+not3)/3
    if ort>=90 and ort<=100:
        harf='AA'
    elif ort>=85 and ort<90:
        harf='BA'
    elif ort>=65 and ort<85:
        harf='CC'
    else:
        harf='FF'
    return ogradı+":"+harf+"\n"


def ortalamaları_oku():
    with open("sınavnotları.txt","r",encoding="utf-8") as file:
        for satır in file:
            print(nothesapla(satır))
def not_gir():
    ad = input ('Öğrenci Adı:')
    soyad = input('Öğrenci Soyad:')
    not1 = input ('not 1: ')
    not2 = input ('not 2: ')
    not3 = input ('not 3: ')

    with open("sınavnotları.txt","a",encoding="utf-8") as file:
        file.write(ad+' '+soyad+':'+not1+','+not2+','+not3+'\n')

def notları_kayıtet():
    pass

while True:
    islem = input("1- Notları oku\n2- Not gir\n3- notları kayıt et\n4- Çıkış \nSeçim:")
    if islem == '1':
        ortalamaları_oku()
    elif islem == '2':
        not_gir()
    elif islem == '3':
        notları_kayıtet()
    else:
        break