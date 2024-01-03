import random
# result = dir(random)
# result= help(random)
result = random.random()  #0.48802299190285436
result1 = random.random()*100 #35.27546600486262

result = int(random.uniform(20,30))#27
result1 = random.randint(20,30) #28
greeting ='hello there'
names = ['ali','yağmur','deniz','cenk']
result=names[random.randint(0,len(names)-1)]
result = random.choice(names)
result1 = random.choice(greeting)

liste=list(range(10))
random.shuffle(liste)
result = liste

liste = range(100)
result =random.sample(liste,3)
print (result)
print (result1)
