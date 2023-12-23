my_list=['bir',2,True,5.6]   #list
tuple=(1,'iki',3)            #tuple
plakalar={'kocaeli':41,'istanbul':34} #dict
fruits={'orange','apple','banana'} #set
print(type(my_list)) #<class 'list'> 
print(type(tuple)) #<class 'tuple'>
print(type(plakalar)) #<class 'dict'>
print(type(fruits)) #<class 'set'>

print(fruits)
#print(fruits[1]) indexlenemez

for x in fruits:
  print(x) #orange
           #apple
           #banana
  
fruits.add('cherry')
fruits.update(['mango','grape','apple']) #apple listede olduğu için eklenmez.
print(fruits)

fruits.remove('mango') #mangoyu siler
fruits.discard('apple')
print(fruits)
fruits.pop() #sırasız olak ilk elemanı siler
print(fruits)
fruits.clear()#seti temizler
print(fruits)


# mylist=[1,2,3,3,5,6,6,9,]
# print(set(mylist)) #{1, 2, 3, 5, 6, 9}

