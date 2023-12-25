def square(num): return num **2

numbers=[1,3,5,9]
            
result=list(map(square,numbers))#list koymadan aktarırsak adresi atar <map object at 0x7f6e2cbd3580>
print(result)#[1, 9, 25, 81] list adres içindekileri listeler
#map(square,number)    / squre