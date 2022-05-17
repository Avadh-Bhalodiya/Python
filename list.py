# List
print("List")

plante=["mercury","venus","earth","mars","jupiter","saturn","uranus","neptune","earth"]
mix=["avadh",56,True,"male"]
l = len(plante)
print("length of plante",l)
print("Type of plante = ",type(plante))
print("Type of mix = ",type(mix))
print()
# Access List item
print("Access List item")

print("no. of 3 plante = ",plante[3])
print("no. of 4 plante using reverse = ",plante[-5])
print("show 3 to 7 = ",plante[3:8])     # 8th term is not included
print("show 3 to last = ",plante[3:])       # 3rd to last term show
print("show 3 to 7 = ",plante[-7:-4])       #  range of negative index, -4 term not included
if "earth" in plante:     #   Check if Item Exists
    print("Yes , 'Earth' is in our solar system")
print()

#      Change List Items
print("Change List Items")

plante[8] = "mars"
print("Change last term earth to mars = ",plante)

plante[3:5] = ["sun", "moon"]
print("Replace mars,jupiter to sun,moon = ",plante)

plante[1:2] = ["sun-2", "moon-2"]
print("Replace venus to sun-2,moon-2 = ",plante)

plante[1:3] = ["Black hole"]
print("Replace sun-2,moon-2 to Black hole = ",plante)

print()
#   Append Items
print("Append Items")

mix.append("raju")          # Append method
print("add item end of the list = ",mix)

plante.insert(0,"Galaxy")       # Insert method
print("Insert 0th position Galaxy = ",plante)

mix.extend(plante)          # Extend method
print("Extend mix's list = ",mix)

temp = (6,"rajesh") #  Add Any Iterable
plante.extend(temp)
print("Mixup List and Tuple with extend method",plante)

plante=["mercury","venus","earth","mars","jupiter","saturn","uranus","neptune","earth"]
mix=["avadh",56,True,"male"]
print()
#   Remove List Items
print("Remove List Items")

plante.remove("mars")
print("remove specific item like mars = ",plante)

plante.pop(2)
print("Specific location item remove like earth = ",plante)

plante.pop()
print("Remove last item = ",plante)

del plante[1]
print("Remove venus = ",plante)

del mix
# print(mix)
print("Delete whole mix's list")

plante.clear()
print("Full clear plante list",plante)
print()

plante=["mercury","venus","earth","mars","jupiter","saturn","uranus","neptune","earth"]
mix=["raju",56,True,"male"]

#   Loop Lists
print("Loop Lists")
print()

print("access list using for loop")
for a in plante:    # access list using loop
    print(a)
print()

print("access list using for loop by length")
for a in range(len(plante)):    # access list using loop by length
    print(plante[a])
print()

print("access list using while loop")
a=0
while a<len(plante):
    print(plante[a])
    a+=1
print()

print("Looping Using List Comprehension")
[print(a) for a in plante]
print()

plante2=[]      #   list comprehension
for i in plante:
    if "e" in i:
        plante2.append(i)
print("plante2 = ",plante2)
print()

plante3 = [i for i in plante if "e" in i]
print("plante3 = ",plante3)
print()

plante4 = [i for i in plante if i != "earth"]       #   filter that only accepts the items
print("plante4 = ",plante4)
print()

plante5 = [i for i in plante]       #   With no if statement
print("plante5 = ",plante5)
print()

number = [x for x in range(100) if x <= 20]    #   use the range() function to create an iterable
print("Number = ", number)
print()

u = [i.upper() for i in plante]         #   Expression
print("Upper Case",u)
print()

#r = ['avadh' for i in mix]
#print("Set all values in the new list to 'avadh' = ",mix)

r2 = [i if i != "mars" else "pluto" for i in plante]
print("replace mars to pluto",r2)
print()

#   Sort Lists
print("Sort Lists")

plante.sort()
print("Sorting = ",plante)
print()

n1 = [100,142,5,37,78,45]
n1.sort()
print("Sorting = ",n1)
print()

plante.sort(reverse=True)       #   Reverse sorting
print("Sorting = ",plante)
print()

n1 = [100,142,5,37,78,45]          #   Reverse sorting
n1.sort(reverse=True)
print("Sorting = ",n1)
print()

def newfunc(x):                  # Customize Sort Function 
    return abs(x-50)

n1 = [100,142,5,37,78,45]            #   Sort the list based on how close the number is to 50
n1.sort(key = newfunc)
print("Sorting with cust fun. = ",n1)
print()

plante1=["Mercury","venus","Earth","mars","Jupiter","Saturn","uranus","neptune","earth"]
plante1.sort()                      #   Case Insensitive
print("Sorting Case sensitive = ",plante1)
print()

plante1=["Mercury","venus","Earth","mars","Jupiter","Saturn","uranus","neptune","earth"]
plante1.sort(key = str.lower)                     #   Case Insensitive But start with lower ASCI value
print("Sorting Case sensitive = ",plante1)
print()

plante=["mercury","venus","earth","mars","jupiter","saturn","uranus","neptune","earth"]
plante.reverse()           #   Reverse sorting
print("Reverse Sorting = ",plante)
print()

print("Copy List")
mix=["raju",56,True,"male"]

mix2 = mix          #   Copy List
print("Mix = ",mix)
print("Mix2 = ",mix2)
print()

mix3 = mix2.copy()          #   Copy List
print("Mix2 = ",mix2)   
print("Mix3 = ",mix3)
print()

mix4 = list(mix3)       #   Copy List
print("Mix3 = ",mix3)   
print("Mix4 = ",mix4)
print()

#   Join Lists
print("Join Lists")

l1 = ["karan","Krutarth","Sunil","Yash"]
l2 = [35,905,77,88]

l3 = l1+l2
print("L3 = ",l3)
print()

for i in l2:
    l1.append(i)
print("L1 = ",l1)
print()

l1 = ["karan","Krutarth","Sunil","Yash"]
l2 = [35,905,66,88]

l1.extend(l2)
print("L1 = ",l1)
print()