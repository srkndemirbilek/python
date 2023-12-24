sayılar=[1,3,5,7,9,12,19,21]
#1: sayılar listesini while ile ekrana yazdırın
'''
index=len(sayılar)
x=0
while x<index:
    print(sayılar[x])
    x+=1
print ('sayılar içindeki veriler yazdırıldı')

#başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın.

x=int(input('başlangıç değerini giriniz: '))
y=int(input('bitiş değerini giriniz:'))
while x<=y:
    if x%2==1:
        print(x)
    x+=1
    
#1-100 arasındaki sayıları azalan şekilde yazdırın
    
x=[1,100]           # i=100
while x[1]>=x[0]:   # while i > 0:
    print(x[1])     #     print(i)
    x[1]-=1         #     i=-1

#kullanıcıdan aldığınız 5 sayıyı ekrana sıralı bir şekilde yazdırın
    
i=0
veri=[]
while i<5:
    veri.append(int(input('sayı giriniz: ')))
    i+=1
print(f'girdiğiniz sayılar {veri}')
sırala=sorted(veri)
print(sırala)
'''
'''
numbers=[]
i=0
while i<5:
    sayi=int(input('sayı giriniz:'))
    numbers.append(sayi)
    i+1=1
print(f'girdiğiniz sayılar {numbers})
numbers.sort{}
print(numbers)
'''

#kullanıcıdan aldığınız sınırsız ürün bilgisini ürünler listesinde içinde saklayan
#   **ürün sayısı kullanıcıya sorunuz
#   **dictinary liste yapısı (name,price) şeklinde olsun
#   **ürün ekleme işlemi bittiğinde ürünleri ekranda while ile yazdırın

adet=int(input('kaç ürün girilecek: '))
x=0
dict=[]
while x<adet:
    name=input(f'{x+1}.ürün adı: ')
    price=input(f'{x+1}.adet: ')
    dict.append({
       'name':name,
       'price':price
       })
    x+=1

for urun in dict:
    print(f'ürün adı:{urun["name"]} ürün fiyatı {urun["price"]}')
print(type(dict))
print(dict)