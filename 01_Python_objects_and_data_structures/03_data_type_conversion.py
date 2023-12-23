x = input('1.sayı: ') #kullanıcı tarafından girilen değerler string olarak algılanır3 
y = input('2.sayı: ')
toplam = (x+y)
print(type(x))
print(type(y))
print (toplam) #2030

toplam=int(x)+int(y) #string olarak girilen x ve y geğişkeni 'integer' a çevrilerek toplandı 
print(toplam) #toplam değişkenine int olarak atandı

x=5             #int
y=2.5           #float
name="Çınar"    #str
isOnline=True   #bool

print(type(x))
print(type(y))
print(type(name))
print(type(isOnline))

##ekran görüntüsü##
# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'bool'>


#TYPE CONVERSİON

#int to float   integerdan floata çevirme

print(x)        # 5
x=float(x)
print(x)        # 5.0
print(type(x))  # <class 'float'>

#float to int
print(y)       #2,5
y=int(y)
print(y)       #2
print(type(y)) #<class 'int'>

result = x + y
print(result)           #7
print(type(result))     #<class 'float'

# bool to str
isOnline=str(isOnline)
print(isOnline)        #True
print(type(isOnline))  #<class 'str'>

#bool to int
isOnline=int(isOnline)
print(isOnline)        #1   True integer karşılığı 1 , false un 0 dır.
print(type(isOnline))  #<class 'int'>

