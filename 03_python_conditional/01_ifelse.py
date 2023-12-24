#########################
İsloggedin=True

if İsloggedin==True : #Eğer isloggedins True ya eşit ise Ekrana Hoşgeldiniz yazdır.
    print('Hoşgeldiniz')

##########################
username='sadıkturan'
password='1234'

İsloggedin=(username=='sadıkturan') and (password=='123')
#              True               and      True    =>   True
if İsloggedin==True:
    print('sisteme Giriş yaptınız')
else:
    print('sisteme Giriş yapamadınız Bilgiler yanlış')

###################################
username='sadıkturan'
password='1234'

if (username=='sadıkturan'):
    if (password=='1234'):
        print('sisteme Giriş yaptınız')
    else:
        print('Parola bilgileri yanlış')
else:
    print('kullanıcı ismi yanlış')