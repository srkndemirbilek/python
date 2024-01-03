liste=["1","2","Sa","10b","abc","10","50"]

# 1: liste elemanları içindeki sayısal değerleri bulunuz.
for x in liste:
    try:
        result = int(x)
        print (result)
    except ValueError:
        continue

# 2: kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayı
#olduğundan emin olunuz aksi halde hata mesajı yazınız.
while True:
    sayı=input('Sayı: ')
    if sayı == 'q':
        break
    try:
        result = float(sayı)
        print ('girdiğiniz sayı',result)
        break
    except ValueError:
        print ('Geçersiz sayu')
# 3: Girilen parola içinde türkçe karakter hatası veriniz.



def checkPassword(parola):
    turkce_karakterler= 'şçğöüıİ'
    for i in parola:
        if i in turkce_karakterler:
            raise TypeError('Parola türkçe karakter içermez.')
        else:
            pass
    print ("Geçerli parola")

parola = input('parola: ')

try:
    checkPassword(parola)
except TypeError as err:
    print(err)
# 4: Faktöriyel fonksiyonu oluşturup foksiyona gelen değer için 
#hata mesajı verin
    
def faktoriyel(x):
    x=int(x)
    if x<0:
        raise ValueError('Negative değer')
    result = 1

    for i in range(1,x+1):
        result *=i
    return result

for x in [5,10,20,-3,'10a']:
    try:
        y=faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)
