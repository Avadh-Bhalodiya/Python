#   In inhertance we use a static method
class animal:
    @staticmethod
    def name():             #   we don’t need the self to be passed as the first argument in static method
        print("zebra")
    def color(self):
        print("black \n")

class animal2(animal):
    def color(self):
        print("white \n")

class animal3():
    def color(self):
        print("white black \n")

x = animal()
x.name()
x.color()

y = animal2()
y.name()
y.color()

z =animal3()
z.color()
#z.name()    #   not use name method because static method available for only inherit class or only own class use through object