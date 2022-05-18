#   Dictionaries
print()
random = {"cow":"calf", "cat": "kitten", "rose":"red", "dog":"pup", "sunflower": "yellow", "control":True, "vehicle":["car", "bike", "boat"]}
print("random = ",random)
print()
print("print 'cat' value = ",random["cat"])
print()
print("length = ",len(random))
print()
print("check type = ",type(random))
print()

#   Access Dictionary Items
a = random["vehicle"]
print("a = ",a)
print()

b = random.get("sunflower")     #   get method
print("b = ",b)
print()

c = random.keys()               #   get all dict key
print("dict all key = ",c)
print()

random["pet"] = "bulldog"       #   add new key with value
print("dict all key = ",c)
print()

random["dog"] = "black"       #   add old key with replace value
print("dict all key = ",c)
print()

c = random.values()               #   get all dict values
print("dict all values = ",c)
print()

t = random.items()
print("dict value change in tuple = ",t)
print()

random["rose"] = "white"
print("change value in tuple = ",t)
print()

random["color"] = "violet"
print("add value in converted tuple = ",t)
print()

if "vehicle" in random:
    print("vehicle is in dict key")
print()


random = {"cow":"calf", "cat": "kitten", "rose":"red", "dog":"pup", "sunflower": "yellow", "control":True, "vehicle":["car", "bike", "boat"]}

#   Change Dictionary Items
random.update({"dog":"brown"})
print("use update method in dict = ",random)
print()

#   Add Dictionary Items
random.update({"color":"green"})
print("use add method in dict = ",random)
print()

#   Remove Dictionary Items
random.pop("color")
print("use pop remove color = ",random)
print()

random.popitem()
print("last dict term remove = ",random)
print()

del random["control"]
print("remove control using del = ",random)
print()

del random
#   print(random)       random dict complete delete

random = {"cow":"calf", "cat": "kitten", "rose":"red", "dog":"pup", "sunflower": "yellow", "control":True, "vehicle":["car", "bike", "boat"]}

random.clear()
print("clear all value in random dict = ",random)
print()

#   Loop Dictionaries

random = {"cow":"calf", "cat": "kitten", "rose":"red", "dog":"pup", "sunflower": "yellow", "control":True, "vehicle":["car", "bike", "boat"]}

for i in random:        #   display all key in dict
    print(i)
print()

for i in random:        #   display all value in dict
    print(random[i])
print()

print("using values method")
for i in random.values():        #   using values method
    print(i)
print()

print("using keys method")
for i in random.keys():        #   using keys method
    print(i)
print()

for i, j in random.items():     #   item show both values
    print(i, j)
print()

#   Copy Dictionaries
r1 = random
print("copy dict in r1 = ",r1)
print()

r2 = random.copy()
print("copy dict in r2 using 'copy' method = ",r2)
print()

r3 = dict(random)
print("copy dict in r3 using 'dict' method = ",r3)
print()

#   Nested Dictionaries

p = {
    "c1":{
        "name":"raju",
        "age":"23"
    },
    "c2":{
        "name":"karan",
        "age":"26"
    },
    "c3":{
        "name":"amisha",
        "age":"13"
    }
}
print("parent p = ",p)
print()

c1 = {
        "name":"rekha",
        "age":"23"
    }
c2 = {
        "name":"aryan",
        "age":"23"
    }
c3 = {
        "name":"karan",
        "age":"23"
    }

p = {
    "c1":c1,
    "c2":c2,
    "c3":c3,
}
print("parent new p = ",p)