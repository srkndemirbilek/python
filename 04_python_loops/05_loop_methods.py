lis=[1,2,3]

for x in lis:
    print(x)

#liste elimizde yoksa
for item in range(100):#0 dan 100 e kadar 100 dahil değil
    print(item)

for item in range(2,10):#2 dan 10 e kadar 10 dahil değil
    print(item)

for item in range(2,10,2):#2 dan 10 e kadar 2 artırarak 10 dahil değil
    print(item)

print(list(range(2,10,2)))

#enumarete
greeting='Hello'
for i,l in enumerate(greeting):
    print(f'index:{i} letter.{l}')

#zip
    
list1=[1,2,3,4,5]
list2=['a','b','c','d','e']
list3=[100,200,300,400,500]
print(list(zip(list1,list2)))#[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
print(list(zip(list1,list2,list3)))#[(1, 'a', 100), (2, 'b', 200), (3, 'c', 300), (4, 'd', 400), (5, 'e', 500)]

for item in zip(list1,list2,list3):
    print(item)
    '''
    (1, 'a', 100)
    (2, 'b', 200)
    (3, 'c', 300)
    (4, 'd', 400)
    (5, 'e', 500)
    '''
for a,b,c in zip(list1,list2,list3):
    print(a,b)
    '''
    1 a
    2 b
    3 c
    4 d
    5 e
    '''

