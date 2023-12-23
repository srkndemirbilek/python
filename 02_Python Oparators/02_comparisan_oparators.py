#username, password => database

#'sadıkturan', '123456'
# == eşit mi
# != eşit değil mi 
# > büyük mü
# < küçük mü
# >= büyük yada eşitmi
# <= küçük yada eşitmi
a,b,c,d=5,5,10,4
password='1234'
username='sadıkturan'
result = a == b #a b ye eşitmi gerecek olan değer True 
print (result) #True
result = a == c #False

result= ('sdktrn'==username) #False
result= ('sadıkturan'==username) #True

result= ('sdktrn'!=username) #True
print(result)
result= (a > c)# False

result=(True == 1)#True
result=(False == 0)#True