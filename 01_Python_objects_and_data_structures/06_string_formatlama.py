name = "Serkan"
surname = "Demirbilek"
age = 39
# print('My name is {} {}'.format(name,surname))  #My name is Serkan Demirbilek
# print('My name is {1} {0}'.format(name,surname))  #My name is Demirbilek Serkan
print("My name is {} {} and I'm {} years old.".format(name,surname,age))  #My name is Demirbilek Serkan and I'm 39 years old. age int olmasına rağmen hata vermeden yazdırıldı.


result=200/700
print("The result= {}".format(result)) #The result= 0.2857142857142857
print("The result= {r:1.4}".format(r=result)) #The result= 0.2857

print(f"My name is {name} {surname} and I'm {age} years old.")  #My name is Demirbilek Serkan and I'm 39 years old. age int olmasına rağmen hata vermeden yazdırıldı.
