#identity Operator: is
x=y=[1,2,3]
z=[1,2,3]

print(x==y)#True
print(x==z)#True

print(x is y)#True     /içlerindeki değerleri değil 
print(x is z)#False    /referans aldıkları yerleri karşılaştırıyor

#membership operators: in
x=['apple','banana']
print('banana' in x) #true
