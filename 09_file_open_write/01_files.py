# Dosya Açmak ve oluşturmak için open() fonsiyonu kullanılır.
# Kullanımı: open('dosya_adı','dosya_erişim_modu')
# dosya_erişim_modu => dosyanın hangi amaçla açtığımızı belirtir.
#    "w" : (Write) yazma modu. 
#       ** Dosyayı konumda oluşturur.
#       ** Dosya içeriğini siler ve yeniden yazar
# file=open("/home/serkan/newfile.txt","w")
# file.close()
file = open ("newfile.txt","w",encoding='utf-8')
file.write("Serkan DEmirbilek")
file.close()

    # "a" : (Append) ekleme. Dosyayı konumda yoksa oluşturur.
file = open ("./09_file_open_write/a.txt","a",encoding="utf-8")
file.write("Serkan Demirbilek\n")
file.close()
    # "x" : (Create) oluşturma. Dosya konumda varsa hata verir.
file = open ("newfile2.txt","x")
    # "r" : (Read) okuma. varsayılan. dosya konumda yoksa hata verir.