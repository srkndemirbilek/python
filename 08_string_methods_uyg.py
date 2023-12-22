website="http://www.sadikturan.com"
course="Python Kursu:Baştan sona Python Programlama Rehberiniz(40 saat)"

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
print(result)
result=website.find('.com')#başladığı index numarasını verir
print(result)
result=course.count('Python',0,50)
print(result)