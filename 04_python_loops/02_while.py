# numbers=[1,2,3,4,5]
# 1-100 e kadar
x=0
while x <= 100: #while True olduğu sürece döner
    print(x)
    x+=1
print('döngü bitti')

#çift rakamlar
x=0
while x <= 100: #while True olduğu sürece döner
    if x%2==0:
        print(x)
    x+=1
print('döngü bitti')

name=''#false

while not name:#boşluk girilirse koşul biter
    name=input('isminizi giriniz: ')

while not name.strip():#boşluk girilirse strip 
    name=input('isminizi giriniz: ')

