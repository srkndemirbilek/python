def square(num): return num **2

result = square(2)

print(result)#4

#######elimizde 1 tane liste var ise
numbers=[1,3,5,9]
for i in numbers:
    result= square(i)
    print(result)
#map kullanarak map dizin elemanlarını fonksiyona tek tek göndermek
#1.
result=list(map(square,numbers))#list koymadan aktarırsak adresi atar <map object at 0x7f6e2cbd3580>
print(result)#[1, 9, 25, 81] list adres içindekileri listeler
#map(square,number)    / squre
    
#2.
for item in map(square,numbers):
    print(item) 
# 1
# 9
# 25
# 81   
    
#lambda bir defaya mahsus kullanılacak fonsiyonu tanımlamak yerine komut içinde kullamak
#def squre(num): return num ** 2
#           /          / 
#          /         /
#         v         v    
#lambda num : num**2
    
#1
result=list(map(lambda num:num ** 2,numbers))
print(result)   

#2
for item in map(lambda num:num ** 2,numbers):
    print(item) 

#3
square1 = lambda num : num**2
result=list(map(square1,numbers))
print(result)   

def check_even(num): return num%2==0
