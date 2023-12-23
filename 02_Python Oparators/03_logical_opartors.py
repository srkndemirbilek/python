x=6

result = 5 < x < 10 #True

#and      true,true=>true     true,false=>false
result= (x>5) and (x<10) # her iki tarafta true ise true gelir

print(result)
#or bir tanesi true olması durumunda true değeri alır
x=5
result=(x>0) and (x%2 ==0) #false
result=(x>0) or (x%2 ==0) #true
print(result)#true
#not

result = not(x>0)# parantez içi true değerini verir resulta false atanır
print(result)