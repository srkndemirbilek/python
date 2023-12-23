numbers=[1,10,5,16,4,9,10]
letters=["a","g","s","b","y","a","s"]

val=min(numbers) #numbers içindeki minimum değeri alır
print(val) #1

val=max(numbers) #numbers içindeki maximum değeri alır
print(val) #16

val=min(letters)
print(val) #a

val=max(letters)
print(val) #y

val=numbers[3:6]
print(val) #[16, 4, 9]

val=numbers[:3]
print(val) #[1, 10, 5]

val=numbers[4:]
print(val) #[4, 9, 10]

numbers[4]=40                  #v
print(numbers) #[1, 10, 5, 16, 40, 9, 10]

numbers.append(49)                        #v
print(numbers) #[1, 10, 5, 16, 40, 9, 10, 49]

numbers.insert(3,78)       #v
print(numbers) #[1, 10, 5, 78, 16, 40, 9, 10, 49]

numbers.insert(-1,50)                         #v -1 sondan bir önceki indexe ekledi
print(numbers) #[1, 10, 5, 78, 16, 40, 9, 10, 50, 49]

numbers.pop()                                     #v     index belirtilmez ise son veriyi siler
print(numbers) #[1, 10, 5, 78, 16, 40, 9, 10, 50]

numbers.pop(3)           #v   üçünçü indexteki veriyi siler
print(numbers) #[1, 10, 5, 16, 40, 9, 10, 50]

numbers.remove(40) #40 girilen veriyi index içinde bulup siler
print(numbers) #[1, 10, 5, 16, 9, 10, 50]

numbers.sort()
print(numbers) #[1, 5, 9, 10, 10, 16, 50]

numbers.reverse() #sorttan sonra kullanılırsa büyükten küçüğe sıralar
print(numbers) #[50, 16, 10, 10, 9, 5, 1]

letters.sort()
print(letters) #['a', 'a', 'b', 'g', 's', 's', 'y']

letters.reverse() #sorttan sonra kullanılırsa büyükten küçüğe sıralar
print(letters) #['y', 's', 's', 'g', 'b', 'a', 'a']

print(len(letters)) #7
print(len(numbers)) #7
print(numbers.count(10)) #2
print(letters.count('a')) #2