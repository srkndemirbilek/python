my_list=[1,2,3]
# my_string='Hello World'

# print(len(my_list))#3
# print(len(my_string))#11

# print(type(my_list))#<class 'list'>
# print(type(my_string))#<class 'str>

class Movie():
    def __init__(self,title,director,duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('movie objesi oluşturuldu.')

    def __str__(self):
        return f"{self.title} by {self.director}"
    
    def __len__(self):
        return self.duration

    def __del__(self):
        print('film objesi silindi')
    
m = Movie('movie Title','director',120)

print (my_list)#[1, 2, 3]
print (m)
print(str(my_list))
print(str(m))
print(len(my_list))
print(len(m))#TypeError: object of type 'Movie' has no len()