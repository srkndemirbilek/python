#Error handling =>hata yönetimi
while True:
    try:
        x=int(input('x: '))
        y=int(input('y: '))
        print(x/y)
        #except ZeroDivisionError:
        #print('y için 0 girilemez')
        #except ValueError:
        #print ('x ve y için sayısal değer girmelisiniz')
    except Exception as ex:
        print ('x ve y için sayısal değer girmelisiniz',ex)
    else:
        break
    finally:
        print('try except sonlandı')