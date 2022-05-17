#   Tuple
games = ("chess", "swimming", "cricket" ,"badminton", "football", "hockey")
print(games)
print()

flower = ("rose",)      #   Create Tuple With One Item
print(type(flower))
print()

games = tuple(("chess", "swimming", "cricket" ,"badminton", "football", "hockey"))
print(games)
print()

mix = ("raju", 59, "apple", 78.6)
print(mix)
print()

#   Access Tuple Items

print(games[3])
print(games[-2])
print(games[3:5])
print(games[3:])
print(games[:4])

if "chess" in games:
    print("Chess in games tuple")
print()

#  Tuple Don't Add value and delete value , but one way tuple convert in list than change values and list convert tuple it can be possible

#   Add two Tuple

games += flower
print("Two tuple Add = ",games)
print()

del games
# print(games)      Because games tuple is deleted


#   Unpacking a Tuple

flower = ("rose", "lotus", "lily")
(bike, car, plane) = flower

print(bike)
print(car)
print(plane)
print()

games = tuple(("chess", "swimming", "cricket" ,"badminton", "football", "hockey"))
(bike, *car, plane) = games
print("Using Asterisk * = ")
print(bike)
print(car)
print(plane)
print()

#   Loop Tuples
games = ("chess", "swimming", "cricket" ,"badminton", "football", "hockey")

for i in games:
    print(i)
print()

for i in range(len(games)):
    print(games[i])
print()
#   Join Tuples

flower = ("rose", "lotus", "lily")
games = ("chess", "swimming", "cricket" ,"badminton", "football", "hockey")

t = flower + games
print("Merge tuple = ",t)
print()

t1 = flower * 3
print("Multiply Tuple = ",t1)
print()
