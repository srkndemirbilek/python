#class
class Person: 
    #class attributes
    address='no information'
    #constructor (yapıcı method)
    def __init__(self,name,year):
        #object attributes
        self.name=name
        self.year=year
        print('init methodu çalıştı')
    #instance methods
    def intro(self):
        print('hello There '+ self.name)
    def calculateAge(self):
        return 2019 - self.year
#object(instance)
p1=Person('ali',1990)   #    p1=Person(name='ali',year=1990)
p2=Person('yağmur',1984)#    p2=Person(name='yağmur',year=1984) şeklindede yazılabilir

#updating
p1.name='ahmet'
p1.address='kocaeli'

p1.intro()


#accessing object attributes
print(f'p1 :name: {p1.name} year: {p1.year}')
print(f'p2 :name: {p2.name} year: {p2.year}')
print(p1)#<__main__.Person object at 0x7f4ec99d6b60>
print(p2)#<__main__.Person object at 0x7f4ec99d6f20>
print(type(p1))#<class '__main__.Person'>
print(type(p2))#<class '__main__.Person'>
print(p1==p2)#False