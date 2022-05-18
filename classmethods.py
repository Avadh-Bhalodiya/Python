#   class method without parameter
class subject:
    s = "Thermodynamics"    #   class vriable
    @classmethod        #   Decorator
    def buy(self):      #   class method
        print()
        print("The buy course name is "+ self.s)

#   subject.buy = classmethod(subject.buy)
subject.buy()           #   calling class method
print()

#   class method with parameter

class subject:
    s = "Thermodynamics"    #   class vriable
    @classmethod        #   Decorator
    def buy(cls,p):
        cls.part = p     #   class method
        print()
        print("The buy course name is "+ cls.s +" "+ cls.part)

#   subject.buy = classmethod(subject.buy)      both type calling
subject.buy("part-2")           #   calling class method
print()

#   Instace method

class mobile:               #   without argument
    def show_mobile(self):
        print("Samsung")
        print()

sam = mobile()
sam.show_mobile()


class mobile:               #   with argument
    def __init__(self):
        self.model = "iqoo"

    def show_mobile(self,p):
        self.price = p
        print(self.model, " = ", self.price)
        print()

sam = mobile()
sam.show_mobile(40000)

#   Accessor method / getter method
class animal:
    def __init__(self):
        self.name = "dog"
    
    def get_name(self):         #   Only data read perpose use this method
        return self.name

a1 = animal()
a = a1.get_name()
print(a)
print()

#   Mutator method              #   without argument
class animal:
    def __init__(self):
        self.name = "dog"
    
    def set_name(self):         #   Only data read and modified
        self.name = "Tiger"

a1 = animal()
a1.set_name()
print(a1.name)
print()

#   Mutator method / setter method             #   with argument
class animal:

    def set_name(self,a):         #   Only data read and modified
        self.name = a

a1 = animal()
a1.set_name("Monkey")
print(a1.name)
print()

#   Static method       #   without parameter
class flower:
    @staticmethod
    def test():
        print("Red Rose")

f1 = flower()
flower.test()
print()

#   Static method       #   with parameter
class flower:
    @staticmethod
    def test(l, s):
        r1 = l
        r2 = s
        print(r1," and ",r2)

f1 = flower()
flower.test("lily","sunflower")
print()