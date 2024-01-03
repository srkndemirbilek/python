#inheritance(Kalıtım):clasların birbirinden miras alma

#Person=> name, lastname,age, eat(), run(), drink()
#Student(Person), Teacher(Person)

class Person():
    def __init__(self,fname,lname):
        self.firstName=fname
        self.lastName=lname
        print('Person Created')
    
    def who_am_i(self):
        print('I am a Person')
    
    def eat(self):
        print('I am eating') 

class Student(Person):
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)
        self.studentnumber = number
        print('Student Created')
    #override
    def who_am_i(self):
        print('I am a Student')

    def sayHello(self):
        print('Hello I am a Student')
class Teacher(Person):
    def __init__(self, fname, lname,branch):
        super().__init__(fname, lname)
        self.branch = branch

    def who_am_i(self):
        print (f'I am a {self.branch} teacher')

p1 = Person('ayşe','turgut')
p2 = Student('veysel','tozlu',125)
t1 = Teacher('aysun','yılmaz','math')

t1.who_am_i()
print (p1.firstName +' '+ p1.lastName)
print (p2.firstName + ' '+ p2.lastName + ' '+ str(p2.studentnumber))

p1.who_am_i()
p2.who_am_i()
p1.eat()
p2.eat()
p2.sayHello()
