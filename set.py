#   Set
print()
vehical = {"turck", "bike", "car", "bus", "plane"}
print(vehical)
print(type(vehical))
print(len(vehical))
print()

mix = {45, 87.09, "karan", True}
print(mix)
print()

s1=set(("turck", "bike", "car", "bus", "plane"))
print(s1)
print()

#   Access Set Items

for i in vehical:
    print(i)
print()

print("car" in vehical)
print()

vehical.add("plan")
print("Add plane in set = ",vehical)
print()

vehical.update(mix)
print("Merge two sets = ",vehical)
print()

mix = {45, 87.09, "karan", True}
l1 = ["raju", 68]

mix.update(l1)
print(mix)
print()

vehical.remove("car")
print(vehical)
print()

vehical.discard("plane")
print(vehical)
print()

vehical.discard("car")
print(vehical)
print()

p = vehical.pop()
print("Pop = ",p)
print(vehical)
print()

mix.clear()
print(mix)
print()

del vehical
#print(vehical)
print()

#   Loop Sets

vehical = {"turck", "bike", "car", "bus", "plane"}
for i in vehical:
    print(i)
print()

#   Join Sets
mix = {45, 87.09, "karan", True, "car", "bus"}

s3 = vehical.union(mix)
print("Union = ",s3)        #   sets item are not reapeat
print()

vehical = {"turck", "bike", "car", "bus", "plane"}
mix = {45, 87.09, "karan", True, "car", "bus"}

vehical.update(mix)
print("Update = ",vehical)        #   sets item are not reapeat
print()

vehical = {"turck", "bike", "car", "bus", "plane"}
mix = {45, 87.09, "karan", True, "car", "bus"}

vehical.intersection_update(mix)
print("intersection_update = ",vehical)
print()

i1 = vehical.intersection(mix)     # intersection perform that time use 3rd variable
print("intersection = ",i1)
print()

i1 = vehical.symmetric_difference(mix)     # intersection perform that time use 3rd variable
print("symmetric_difference = ",i1)
print()

