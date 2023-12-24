numbers=[1,2,3,4,5]

# print(numbers[0]);
# print(numbers[1]);
# print(numbers[2]);
# print(numbers[3]);
# print(numbers[4]);

for num in numbers: #number liste eleman sayısı kadar for döngüsü dönüp her döngüde o elemanı numa atar
    print(num)

names=['çınar','ahmet','sena']
for n in names:
    print(n)

tuple=(1,2,3,4,5)
for t in tuple:
    print(t)
print('#########################')
tuple=[(1,2),(1,3),(1,4),(3,5)]
for a,b in tuple:
    print(a,b)

dic={'k1':1,'k2':2,'k3':3}
for a in dic:
    print(a) #sadece key bilgileri gelir

for a in dic.items():
    print(a) #('k3', 3) hrr ikiside gelir

for a,b in dic.items():
    print(a,b) # k1 1 her ikiside gelir


