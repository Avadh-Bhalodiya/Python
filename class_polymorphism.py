#   polymorphism
def add(a,b,c=0):
    return a+b+c
print(add(8,8))         #   same fun name but parameter are diffrent
print(add(8,8,10))

#   Method overriding       same name, same parameter
class India:            #   Method overloading  same name, diff parameter
    def capital(self):
        print("\nDelhi")
    def language(self):
        print("hindi")
    #def language(self,e):
    #    print("secondry language = ",e)
    def money(self):
        print("Rupee")

class USA:
    def capital(self):
        print("\nwashigton")
    def language(self):
        print("english")
    #def language(self,e):
    #    print("secondry language = ",e)    
    def money(self):
        print("doller")

i = India()
u = USA()
for country in (i, u):
   country.capital()
   country.language()
   country.money()
#i.language("english")
#u.language("france")

print("\nwith function")
def func(obj):
    obj.capital()
    obj.language()
    obj.money()

func(i)
func(u)