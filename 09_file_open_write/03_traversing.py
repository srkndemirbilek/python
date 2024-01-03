# file = open("newfile.txt","r",encoding="utf-8")
# content = file.read()
# print (content)
# file.close()
########################################
with open("newfile.txt","r",encoding="utf-8") as file:
    content = file.read()
    print (content)
    print (file.tell())#kursörün konumunu verir
    content2=file.read()#kursör sonda olduğı için herhangi bir okuma yapmaz
    file.seek(0)#kursörü başa gönderiri
    content2=file.read()
    print(content2)
    #file.close a ihtiyaç tok