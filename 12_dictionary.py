# key    -  value
# 41   =>   kocaeli
# 34   =>   istanbul

## dictinary kullanmadan
sehirler=["kocaeli","istanbul"]
plakalar=[41,34]

print(plakalar[sehirler.index('kocaeli')]) #41
print(plakalar[sehirler.index('istanbul')]) #34

##dictionary kullanarak
#print(plakalar['kocaeli'])===> 41

#plakalar={key : value , key : value}

plakalar={'kocaeli':41,'istanbul':34}
print(plakalar['istanbul']) #34

plakalar['kocaeli']='new value' #var olan bir key de günceller
print(plakalar) #{'kocaeli': 'new value', 'istanbul': 34}
plakalar['izmir']=35 #olmayan key i ekler
print(plakalar) #{'kocaeli': 'new value', 'istanbul': 34, 'izmir': 35}


#########################################################################
users={
    'sadıkturan':{
        'age':36,
        'roles':['user'],
        'email':'sadıkturan@gmail.com',
        'address':'kocaeli',
        'phone':'5552564864'
    },
    'cınarturan':{
        'age':16,
        'roles':['admin','user'],
        'email':'cınarturan@gmail.com',
        'address':'kocaeli',
        'phone':'5552564864'
    }
}
print(users['cınarturan']) # {'age': 16, 'roles': ['admin', 'user'], 'email': 'cınarturan@gmail.com', 
                           # 'address': 'kocaeli', 'phone': '5552564864'}
print(users['cınarturan']['roles']) #['admin', 'user']
print(users['cınarturan']['roles'][1]) #user
print(type(users)) #<class 'dict'>