# try:
#     file = open("newfile.txt","r",encoding="utf-8")
#     print(file)
# except FileExistsError:
#     print("Dosya okuma Hatası / Dosya mevcut konumda yok")
# finally:
#     print("Dosya kapandı")
#     file.close()

file = open("newfile.txt","r",encoding="utf-8")

#for döngüsü
# for i in file:
#     print(i,end="")

#read fonsiyonu
# print ("içerik 1 ")
# content=file.read()
# print (content)

# print ("içerik 2")
# content2 =file.read()

# content=file.open(5)
# content=file.open(3)


# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")

liste = file.readlines()
print(liste[0])
print(liste[1])
print(liste[2])
file.close()


