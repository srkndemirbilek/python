# x=5
# y=10
# z=20
x,y,z=5,10,20
print(x,y,z)#5 10 20

x,y=y,x
print(x,y,z)#10 5 20

x +=5 #  x = x + 5
print(x,y,z)
x *=5 #  x = x * 5
x -=5 # x = x - 5
x /=5 # x = x / 5
y //=5
x %=5
y **=z

#############
values=1,2,3
print(type(values))#<class 'tuple'>

x,y,z = values
print(x,y,z)#1 2 3

values=1,2,3,4,5
x,y,*z = values
print(x,y,z) # 1 2 [3, 4, 5]