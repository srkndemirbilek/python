'''
    Daire Alanı   :πr^2
    Dairenin cevresi: 2πr
    *Yarı çapı verilen bir dairenin alan ve cevresini hesaplayınız.(π=3.14)
'''
r = float(input('Dairenin yarı çapını giriniz.r = '))
pi=3.14
alan=pi*(r**2)
cevre=2*pi*r
print("çevre :"+str(cevre))
print("alan:"+str(alan))