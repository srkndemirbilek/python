website="http://www.sadikturan.com"
course="Python Kursu:Baştan sona Python Programlama Rehberiniz (40 saat)"

#1- ' Hello World ' karakter dizisinde baş ve sondaki boşluk karakterlerini silin
result=' Hello World '.strip() #her iki tarafıda siler
result=' Hello World '.lstrip() #sol tarafı başı siler
result=' Hello World '.rstrip() #sağ tarafı sonu siler
print(result)
#2- 'www.sadikturan.com' içindeki sadıkturan bilgisi haricindeki her karakteri silin
result='www.sadikturan.com'.strip('w.moc')
print(result)

#3- 'course' karakter dizisindeki tüm karakterleri küçük harf yapın
result=course.lower()
print(result)

#4- 'website' içinde kaç tane a karakteri vardır?(count('a))
result=website.count('a')
print(result)

#5- 'website' "www" ile başlatıp com ile bitiyormu?
result=website.startswith('www') and website.endswith('com')
print(result)

#6- 'website' içinde '.com' ifadesi varmı
result=website.count('.com') #adet verir
print(result) #1
result=website.find('.com')#başladığı index numarasını verir
print(result) #21
result =course.count('Python',0,50)
print(result)#2
result=course.find('Python')
print(result)#0
result=course.index('Python')
print(result) #0
result=course.rindex('Python')
print(result) #25

#7- 'Course' içindeki karakterlerin hepsi alfabetik mi?
result=course.isalpha()
print(result) #False
result='Hello'.isalpha()
print(result) #True

#8 'Contents' ifadesini satırda 50 karakter içinde yerleştirip sağına ve soluna * ekleyiniz.
result='Contents'.center(50,'*')
print(result)

#9 'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
result=course.replace(' ','-')
print(result)

#10- 'Hello World' karakter dizisinde 'World ifadesini 'There' olarak değiştirin
result='Hello World'.replace('World','There')
print(result) 

#11- 'course' karakter dizisindeki boşluk karakterlerinden ayırın.
result=course.split()
print(result)