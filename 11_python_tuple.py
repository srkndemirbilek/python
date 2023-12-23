list=[1,2,3,5]
tuple=(1,'iki',3)

print(type(list)) #<class 'list'>
print(type(tuple))#<class 'tuple'>

print(len(tuple)) #3
print(len(list)) #4

print(tuple[1]) #iki
print(list[2]) #3

print(list) #[1, 2, 3, 5]
print(tuple) #(1, 'iki', 3)

list[1]=10 
#tuple[1]='üç' # tuple lar listeler gibi değiştirilez ve atanamaz
print(list) #[1, 10, 3, 5]
print(tuple) #TypeError: 'tuple' object does not support item assignment