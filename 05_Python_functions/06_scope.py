#global ve local değişkenler
#global scope
x='global x'

def function():
    #local scope içerde tanımlanan değişkenler dışardaki değişkeni etkilemez
    x='local x'
    print(x) #function içinde tnımlanmış bir x olmasaydı dışarda tanımlana x kullanır.

function()
print(x)    

######################################
name='Çınar'
def changeName (newname):
    name = newname
    print(name)

changeName('Ada')
print(name)

##########################

name='global string'
def greeting():
    #name='Çınar'
    def hello():
        #name='Ada' 
        print('hello'+name) 
    hello()
greeting()

#################

x=50
def test():
    global x #dışardaki x değişkenin kullanılacağını belirtir 
    print(f'x:{x}')
    x=100
    print(f'changed x to {x}')

test()
print(x)
