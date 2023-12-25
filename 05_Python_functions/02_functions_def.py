def sayHeloo(name='Users'):
    print('Hello '+name)

def sayHelo(name='Users'):
    name='serkan'
    return'Hello '+name



name=input('adınız: ')
sayHeloo(name)#Hello Serkana

sayHeloo()#Hello Users

msg=sayHelo('Çınar')
print(msg) #Hello Çınar

print('################################')
def total(num1,num2):
    return num1+num2


result=total(10,20)
print(result)#30
print(total(10,20))#30

def yashesapla(dogumyılı):
    '''
    DOCSTRING: dogum yılınıza gore yasınızı hesaplar
    INPUT:dogumyılı
    OUTPUT: yasınız

    çıkış için
    qqser
    '''
    return 2023-dogumyılı

print(str(yashesapla(1984))+' yaşındasın')#39 yaşındasın
print(help(yashesapla))
    

def emeklilikhesapla(dogumyılı,isim):
    yas=yashesapla(dogumyılı)#yashesapla bir üstteki fonksiyandan hesaplanıyor
    emeklilik=65-yas
    
    if emeklilik > 0: 
        print (f'{isim} emekliliğinize {emeklilik} yıl kaldı')
    else:
        print('Zaten emekli oldunuz')
        
emeklilikhesapla(1983,'ali')
emeklilikhesapla(1950,'ahmet')
emeklilikhesapla(1974,'yağmur')

