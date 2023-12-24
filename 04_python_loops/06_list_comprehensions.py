#
number=[]
for x in range(10):
  number.append(x)
print(number)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('########################') 
#
numbers=[x for x in range(10)]
print (numbers)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for x in range(10):
  print(x**2)
############################
number=[x**2 for x in range(10)]
print(number)
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

number= [x*x for x in range(10) if x%3==0]
print(number)

myString='Hello'
myList=[]

for letter in myString:
  myList.append(letter)
print(myList)
#['H', 'e', 'l', 'l', 'o']

myList=[letter for letter in myString]
print(myList)
#['H', 'e', 'l', 'l', 'o']

years =[1983,1999,2008,1956,1986]
ages=[2019-year for year in years]
print(ages)
#[36, 20, 11, 63, 33]

results = [x if x%2==0 else 'TEK' for x in range(1,10)]
print(results)
#['TEK', 2, 'TEK', 4, 'TEK', 6, 'TEK', 8, 'TEK']

result=[]
for x in range(3):
  for y in range(3):
    result.append((x,y))
print(result)
#[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

number=[(x,y) for x in range(3) for y in range(3) ]
print(number)
#[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
