# #Karakter Dizileri:String


name = "Serkan" #6 karakterli bir dizi
surname = "Demirbilek" # 10 karakteli bir dizi
age = 39
print("My name is "+name+' '+surname+' and \nI am '+str(age)+' years old.')

metin="My name is "+name+' '+surname+' and \nI am '+str(age)+' years old.'
# # print(metin)

print(metin[0]) #M
print(metin[3]) #n
print(len(metin)) #52    len metodu metin içerisinde kaç karakter olduğunu verir.
print(metin[len(metin)-1]) #son karakteri yazdırmak için len metodunun verdiği rakamın -1 değeri vermek gerekiyor
print(metin[3:10]) #name is   3 karekterden 10. karaktere kadar olanları yazdırdı




