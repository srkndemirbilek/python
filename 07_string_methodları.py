message=' hello There. My name is Sadık Turan'
message=message.upper() #HELLO THERE. MY NAME IS SADIK TURAN
print(message)
message=message.capitalize() #ilk harfini büyük yapar diğerleri küçük Hello there. my name is sadık turan
print(message)
message=message.lower() #her karakteri küçük harfe çevirir.
print(message)
message=message.title() #her kelimenin baş harfi büyük
print(message)
message=message.strip()#Baştaki boşluk karakteri gider
print(message) 
message=message.split() #her boşluktan sonraki kelimeleri diziye çevirir
print(message) #['Hello', 'There.', 'My', 'Name', 'Is', 'Sadik', 'Turan']
#message=message.split('.') #her noktadan sonraki cümleyi dizine çevirir.
#print(message) #['Hello There', ' My Name Is Sadik Turan']
message=" ".join(message) #['Hello', 'There.', 'My', 'Name', 'Is', 'Sadik', 'Turan'] dizini birleştirir "Hello There. My Name Is Sadik Turan"
print(message)
message=message.replace('Sadik','Çınar')#message içerisinde geçen Sadik kelimesini Çınar İle Değiştir.
print(message)