def changeName(n):
    n='serkan'

ad='yiğit'
changeName(ad)
print(ad) #Yiğit Parametre çalışmadı value type olmasından adres kopyalaması olmamamsından değişmedi


   
def change(n):
    n[0]='istanbul'

sehirler=['ankara','eskişehir']
change(sehirler[:])
print(sehirler)#['ankara', 'eskişehir'] value type dan dolayı değişmesi 

change(sehirler) 
print(sehirler)#['istanbul', 'eskişehir'] parametre çaıştı referans type 

def add(a,b,c=0,d=0,):
    return sum((a,b,c,d,))#sum python topla parametresi
print(add(5,6)) #iki adet gönderildiğinde c ve d boş olması durumunda sıfır atandığı içi toplamı 11 verdi
print(add(5,6,1,1))#13

#yukarıdaki örneğer alternatif arguman

def add1(*params):
    print(f'girilen sayılar toplanacak {params}')
    return sum(params)
print(add1(10,3,5,6,4,8,9,3,5))#53

#sum fonksiyonunu kulllanmak istemez isek

def add1(*params):#* tek yıldız tuple listesi oluşturur
    print(f'girilen sayılar toplanacak {params}')
    top=0
    for n in params:
        top=top+n
    return top
print(add1(10,3,5,6,4,8,9,3,5))#53

#######################################
def displayUser(**arg):#** çift tıldız dict oluşturur.
    for key,value in arg.items():
        print('{} is {}'.format(key,value))

displayUser(name='Çınar',age=2, city='İstanbul')
displayUser(name='Ada',age=12, city='Kocaeli',phone='1234567')
displayUser(name='Yiğit',age=14, city='Ankara',phone='1234567',email='sdad@adsdas.com')
# name is Çınar
# age is 2
# city is İstanbul
# name is Ada
# age is 12
# city is Kocaeli
# phone is 1234567
# name is Yiğit
# age is 14
# city is Ankara
# phone is 1234567
# email is sdad@adsdas.com
#####################
def myFunc(a,b,c,*args,**kworgs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kworgs),

myFunc(10,20,30,40,50,key1='value1',key2='value2')
# 10
# 20
# 30
# (40, 50)
# {'key1': 'value1', 'key2': 'value2'}


