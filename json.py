#   JSON  to python
import json

a = '{"name":"aaryan", "age":40, "city":"New York"}'    #   some json
print(type(a))

b = json.loads(a)     #     parse a


print()
c = b["age"]    #    result in dictionary
print(c)
print(type(c))

#   python to json
dict = {
    "name":"rajesh",
    "no":"9834753498",
    "gender":"male"
}

j = json.dumps(dict)


print(j)       #   result in json string
print(type(j))
print()

print("list to json = ",json.dumps(["black","watermelon","mango"]))
print("tuple to json = ",json.dumps(("black","watermelon","mango")))
print("dict to json = ",json.dumps({"key":"lock","king":"queen","car":"mustang"}))
print("string to json = ",json.dumps(("helllooo")))
print("int to json = ",json.dumps((45)))
print("float to json = ",json.dumps((45.97)))
print("true to json = ",json.dumps((True)))
print("false to json = ",json.dumps((False)))
print("none to json = ",json.dumps((None)))
print()

# Python to JSON
# dict	    Object
# list	    Array
# tuple	    Array
# str	    String
# int	    Number
# float	    Number
# True	    true
# False	    false
# None	    null

x = {
  "name": "rutvik",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("raj","sonal"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "kmh": 7.5},
    {"model": "Mustang GT", "mpg": 2.1}
  ]
}

print(json.dumps(x))
print()

print(json.dumps(x, indent=1))
print()

print(json.dumps(x, indent=4, separators=("."," = ")))
#   default value is (", ", ": ")
print()

print(json.dumps(x, indent=10, sort_keys=True))
# sort the result alphabetically by keys:
print()