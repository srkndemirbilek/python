#value types ==> string , number
x=5
y=25

x=y
y=10
print(x,y)#25 10


#reference types => list
a=['apple','banana']
b=['apple','banana']
a=b

b[0]="grape"
print(a,b) #['grape', 'banana'] ['grape', 'banana']