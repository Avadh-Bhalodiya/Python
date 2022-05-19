a = 460
b = "nike"
c = "wooden"
str = "The bat price is {:.2f} {} {}"
print(str.format(a, b, c))

str1 = "The bat price is {0:.2f} {1} {2} {0} {d}"
print(str1.format(a, b, c, d="model air-bat-252"))