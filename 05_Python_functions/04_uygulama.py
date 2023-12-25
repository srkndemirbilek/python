#1- gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonsiyon yazınız
# uygulamadan girilen veriler       v       kod ile girilen veriler
def yazdır(yazı,tekrar):            #   def yazdır(kelime,adet)
    for x in range(tekrar):         #       print(kelime * adet)
        print(yazı)                 #   yazdır('merhaba\n',10)
a=input('bir kelime girin')
b=int(input('kaç kez yazdırılsın'))
yazdır(a,b)


#2- kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren

def listeyeCevir(*args):
    list=[]
    for i in args:
        list.append(i)
    return list

print(listeyeCevir(10,20,'a',58,'ahmet'))

#3- gönderilen 2 syı arasındaki tüm asal sayıları bulan

def asalSayıbul(sayı1,sayı2):
    for sayı in range(sayı1,sayı2+1):
        if sayı>1:
            for i in range(2,sayı):
                if (sayı%i==0):
                    break
            else:
                print(sayı)
sayı1=int(input('sayı1 '))
sayı2=int(input('sayı2'))
asalSayıbul(sayı1,sayı2)

#kendisine gönderilen bir sayının tam bölenlerini bir liste oluşturun

def tambolbul(gelen):
    list=[]
    for i in range(2,gelen+1):
        if (gelen%i==0):
            list.append(i)
    print(f'{gelen} e tam bölünen sayılar {list}')

tambolbul(100)