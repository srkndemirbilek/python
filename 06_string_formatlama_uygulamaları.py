website="http://www.sadıkturan.com"
course="Python Kursu: Baştan Sona Python Programlama Rehberiniz(40 saat)"

#1- 'course' karakter dizisinde kaç karakter bulunmakta?

length=len(course)
print(f'course dizisinde {length} karakter bulunmaktadır.')

#2- 'website içinden www karakterelerini alın.
al=website[7:10]
print(al)

#3- 'website' içinden com karakterini alın.
al1=website[-3:]
print(al1)
al2=website[22:]
print(al2)

#4- 'course' içinden ilk 15 ve son 15 karakteri alın. Python Kursu: Beriniz(40 saat)
ilk=course[0:15]+course[-15:]
print(ilk)

#5- 'course' ifadesindeki karakterleri tersten yazdırın
ters=course[::-1]#numara belirtmez isek tüm karakteerleri sonuncu : den sonraki -1 de tersten olarak alır
print(ters)

#6- 
name,surname,age,job="Bora","Yılmaz",32,"mühendis"
#Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis.' 
print(f'Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}.')

#7- 'Hello world' ifadesindeki w harfini W ile değiştirin.
a="Hello world"
a=a[:6]+'W'+ a[-4:]
print(a)

#8- 'abc'ifadesini yanyana 3 defa yazdırın
a="abc"
a=a*3
print(a)