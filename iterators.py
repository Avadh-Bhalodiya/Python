animal = ("dog", "cat", "monkey")
x = iter(animal)

print(next(x))
print(next(x))
print(next(x))
print()

s = "Astronaut"
y = iter(s)

print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print()

#   for loop

for i in animal:
    print(i)
print()

for j in s:
    print(j)
print()

class number:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        b = self.a
        self.a += 1
        return b

o = number()
i = iter(o)

print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print()

#   stop iteration

class number:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            b = self.a
            self.a += 1
            return b
        else:
            raise StopIteration

o1 = number()
i1 = iter(o1)

for d in i1:
    print(d)