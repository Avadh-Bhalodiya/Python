f = open("text.txt","r")
print(f.read())
#   f = open("D:\\myfiles\text.txt", "r")    files locate in another location specified path
print()
f = open("text.txt","r")
print(f.read(7))
print()

f = open("text.txt","r")
print("Single line read = ",f.readline())

f = open("text.txt","r")
print(f.readline())
print(f.readline())

print("Whole file read looping:- \n")
f = open("text.txt","r")
for i in f:
    print(i)
f.close()

f = open("text.txt","a")
f.write("\nMore Content ! ")
f.close

f = open("text.txt","r")
print(f.read())

f = open("text.txt","w")
f.write("\nMore and More Content ! ")
f.close

f = open("text.txt","r")
print(f.read())

#f = open("text.txt","x")

f = open("text2.txt","w")

from genericpath import exists
import os

os.remove("text2.txt")

if os.path.exists("text.txt"):
    os.remove("text.txt")
else:
    print("File dose not exist")

os.rmdir("foldername")  #   folder delete