name ='Sadık Turan'

for letter in name: #tüm harfleri aLt altta ekrana yazdırı
    print(letter)
print('********************************')

for letter in name: #a ya geldiğinde döngü durur.
    if letter=='a':
        break            # ekran çıktısı sadece S
    print(letter)
print('********************************')

for letter in name: #a ya continu döngü içindeki kalan komutlar çalışmadan döngüye devam ederi komutlar çalışmadan döngü devam eder.
    if letter=='a':
        continue           # ekran çıktısı nda a yazılmadan devam eder
    print(letter)
print('********************************')


###############################
x=0
while x<5:
    x+=1
    if x==3:
        continue
    print(x)

#1-100 e kadar tek sayıların toplamı
x=0
topla=0
while x<=100:
    x+=1
    if x % 2==0:
        continue
    topla+=x
print(topla)
    

