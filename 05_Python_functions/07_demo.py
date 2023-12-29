#bankamatik 

SadıkHesap={
    'adı':'Sadık Turan',
    'hesapNo':'13245678',
    'bakiye':3000,
    'ekhesap':2000
}

AliHesap={
    'adı':'Ali Turan',
    'hesapNo':'12345678',
    'bakiye':2000,
    'ekhesap':1000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['adı']}")

    if (hesap['bakiye']>=miktar):
        hesap['bakiye']-=miktar
        print ('paranızı Alabilirsinir.')
    else:
        toplam=hesap['bakiye']+hesap['ekhesap']

        if (toplam>=miktar):
            ekhesapkullanımı=input('ek hesap kullanılsın mı? (e/h): ')
            if ekhesapkullanımı =='e':
                ekhesapkullanMiktar=miktar-hesap['bakiye']
                hesap['bakiye']=0
                hesap['ekhesap']=ekhesapkullanMiktar
                print('paranızı alabilirsiniz.')
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır")
        else:
            print('üzgünüz bakiye yetersiz.')

paraCek(SadıkHesap,5000)