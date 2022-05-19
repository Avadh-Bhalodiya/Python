#   Inheritance

class teacher:
    def __init__(self,name,salary,age):
        self.n = name
        self.s = salary
        self.a = age

    def display(self):
        print("name = ",self.n, "\nsalary = ",self.s, "\nage = ",self.a)


class student(teacher):
    def __init__(self, name, roll, subject, year):
        print("\nHello")
        print("\naccess init method by class name")
        teacher.__init__(self, name, roll, subject)     #   parent init method call 
        print("name = ",self.n, "\nsalary = ",self.s, "\nage = ",self.a)
        print("\naccess init method by super() method")
        super().__init__(name, roll, subject)       #   parent init method call 
        print("name = ",self.n, "\nsalary = ",self.s, "\nage = ",self.a)
        print("\nover child class methods")
        self.year = year
        print("Year= ", year)

    def welcome(self):
        print("welcome ", self.n, "to join our team", self.year)

c1 = student("sanjay", 202020, 40, 1992)
print("\naccess child object through parent display function")
c1.display()
c1.welcome()
print()