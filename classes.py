#   Class
class test:
    a = 5
print(test)
print()

o1 = test()
print("a = ", o1.a)
print()

class student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks

p1 = student("ram","29",89)

print(p1.name)
print(p1.age)
print(p1.marks)
print()

class teacher:
    def __init__(own,name,age,salary):
        own.name = name
        own.age = age
        own.salary = salary
    
    def test(own):
        print("This is test function and our teacher is " + own.name)

p1 = teacher("rajvir", 39, 40000)
p1.test()
p1.name = "krutika"
p1.test()
print()
print(p1.age)
del p1.age
#   print(p1.age)       age has been deleted
print()
del p1
#   print(p1)       p1 object has been deleted

class animal:
    pass
print("pass statement work")
print()