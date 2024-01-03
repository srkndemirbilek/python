# def greeting(name):
#     print('Hello', name)

# print(greeting('ali'))
# print(greeting)

# sayHello = greeting    
# print(sayHello)
# print(greeting)

# del sayHello
# print(greeting)

#encapsulation
# def outher(num1):
#     print ('outher')
#     def inner_increment(num1):
#         print('inner')
#         return num1+1
#     num2= inner_increment(num1)
#     print (num1,num2)

# outher(10)
def faktorial(number):
    if not isinstance(number,int):
        raise TypeError("number must be an integer") 
    
    if not number >=0:
        raise ValueError ("number must be zero or positive")
      
    def inner_factorial(number):
        if number <=1:
            return 1
        
        return number * inner_factorial(number - 1)
    
    return inner_factorial(number)
try:
    print (faktorial(0))
except Exception as ex:
    print (ex)
