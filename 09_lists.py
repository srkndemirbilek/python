message='Hello There. My name is Sadık Turan'.split()
print(message)
#['Hello', 'There.', 'My', 'name', 'is', 'Sadık', 'Turan']

my_list=[1,2,3]
print(my_list) #[1, 2, 3]
my_list=['bir',2,True,5.6]
print(my_list) #['bir', 2, True, 5.6]
list1=['one','two','three']
list2=['four','five','six']
numbers=list1+list2
print(numbers)
print(len(numbers))

userA=['Ali',32]
userB=['Ahmet',36]
users=userA+userB
print(users) #['Ali', 32, 'Ahmet', 36]
userlist=[userA,userB] #liste içinde liste
print(userlist) #[['Ali', 32], ['Ahmet', 36]]
print(userlist[0]) #['Ali', 32]