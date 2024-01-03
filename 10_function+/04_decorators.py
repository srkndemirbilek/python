# def my_decoctator(func):
#     def wrapper(name):
#         print('fonsiyondan önce işlemler')
#         func(name)
#         print('fonsiyondan sonraki işlemler')
#     return wrapper

# @my_decoctator
# def sayhello(name):
#     print('Hello',name)

# sayhello('ali')

# sayhello = my_decoctator(sayhello)@my_decoctator yazılmaz ise
# sayhello()

import math, time

def calculate_time(func):
    def inner(*args,**kwargs):
        start=time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish=time.time()
        print ('fonsiyon : '+func.__name__+' '+str(finish-start)+' saniye sürdü')
    return inner
@calculate_time
def usalma(a,b):
    # start=time.time()
    # time.sleep
    print (math.pow(a,b))
    # finish=time.time()
    # print ('fonsiyon : '+str(finish-start)+' saniye sürdü')
@calculate_time
def faktoriyel(a):
    # start=time.time()
    # time.sleep
    print(math.factorial(a))
    # finish=time.time()
    # print ('fonsiyon : '+str(finish-start)+' saniye sürdü')

usalma(2,3)
faktoriyel(4)
