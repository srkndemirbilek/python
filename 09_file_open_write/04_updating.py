# with open("newfile.txt","r+",encoding="utf-8")as file:
#     print(file.read())

# with open("newfile.txt","r+",encoding="utf-8")as file:
#     file.seek(20)
#     file.write("deneme")
#sayfa sonu güncelleme
# with open("newfile.txt","a",encoding="utf-8")as file:
#     file.write("\nzeynel turan")
# with open("newfile.txt","r+",encoding="utf-8")as file:
#     print(file.read())
#sayfa başında güncelleme
# with open("newfile.txt","r+",encoding="utf-8")as file:
#     content = file.read()
#     content = "Efe Turan\n"+content
#     file.seek(0)
#     file.write(content)
# with open("newfile.txt","r+",encoding="utf-8")as file:
#     print(file.read())
#sayfa ortasında güncelleme
with open("newfile.txt","r+",encoding="utf-8")as file:
    list=file.readlines()
    print(list)
    list.insert(1,"yılmaz aygün\n")
    file.seek(0)
    # for i in list:
    #     file.write(i)
    file.writelines(list)

with open("newfile.txt","r+",encoding="utf-8")as file:
    content = file.read()
    print(content)
    