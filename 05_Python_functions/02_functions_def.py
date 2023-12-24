def sayHeloo(name='Users'):
    print('Hello '+name)

def sayHelo(name='Users'):
    return'Hello '+name



name=input('adınız: ')
sayHeloo(name)#Hello Serkan

sayHeloo()#Hello Users

msg=sayHelo('Çınar')
print(msg) #Hello Çınar

print('################################')
def total(num1,num2):
    return num1+num2


result=total(10,20)
print(result)#30
print(total(10,20))#30

def yashesapla(dogumyılı):
    '''
    DOCSTRING: dogum yılınıza gore yasınızı hesaplar
    INPUT:dogumyılı
    OUTPUT: yasınız
    '''
    return 2023-dogumyılı

print(str(yashesapla(1984))+' yaşındasın')#39 yaşındasın
print(help(yashesapla))
