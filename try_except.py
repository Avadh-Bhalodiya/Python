#   try .... except
try:
    print(x)
except NameError:
    print("Variable x is not define")
except:
    print("Somethings went wrong")

#   try .... except  & finally
try:
    print("raju")
except:
    print("Somethings went wrong")
else:
    print("Every thing is fine")
finally:
    print("try...except and else is finished")

try:
    f = open("avadh.txt")
    try:
        f.write("Hello")
    except:
        print("you are didn't write in this file")
    finally:
        f.close()
except:
    print("file didn't open")

#   Raise 

i = 10

#if i < 20:
#    raise Exception("don't write below 20 number")


s = "banana"

if not type(s) is int:
    raise TypeError("Only integers")