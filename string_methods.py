s1 = "hello, and welcome to my aldorado."
print("1.   ",s1.capitalize())
s2 = "Hello, and Welcome to my aldorådo to."
print("2.   ",s2.casefold())
print("3.   ",len(s1))
print("4.   ",len(s2))
print("5.   ",s2.center(50))
print("6.   ",s2.count("to"))
print("7.   ",s1.encode())
print("8.   ",s1.endswith("aldorado"))
s3 = "5\t43\tavadh\thehe"
print("9.   ",s3.expandtabs(4))
print("10.   ",s1.find("welcome"))
print("11.   ",s1.index("to"))
s4 = "lion123."
print("12.   ",s1.isalnum())    #   false   because "." is not alphabetic or number
s5 = "raju"
print("13.   ",s5.isalpha())
print("14.   ",s5.isascii())
s6 = "\u0019"
print("15.   ",s6.isdecimal())
s7 = "52266"
print("16.   ",s7.isdigit())
print("17.   ",s4.isidentifier())   #   identifier include a-z,0-9,"_"
print("18.   ",s1.islower())
print("19.   ",s7.isnumeric())  #   -2,4.6 means negetive & flote value not consider in numeric
print("20.   ",s1.isprintable())
print("21.   ",s1.isspace())    #   only blank string consider in whitespace
s8 = "Hello, And Welcome To My Aldorådo To."
print("22.   ",s8.istitle())
s9 = "HELLO"
print("23.   ",s9.isupper())
s10 = ("aarti", "rina", "maya")
print(" * ".join(s10))
s11 = "KGF      "
print(s11.ljust(30),"Aldorado")
print("24.   ",s9.lower())
print("Aldorado",s11.lstrip(),"Aldorado")
s12 = "Hello! tank tories boy"
x = s12.maketrans("t","T")
print(s12.translate(x))
print("25.   ",s12.partition("tank"))
print("26.   ",s12.replace("tank","stark"))
print("27.   ",s12.rfind("boy"))
print("28.   ",s12.rfind("boy"))
print("29.   ",s9.rjust(20), "Smith")
print("30.   ",s12.rpartition("tank"))
s13 = "fruits , flower , vehicle"
print("31.   ",s13.rsplit(", "))
print("32.   ",s11.rstrip(),"check")
print("33.   ",s2.split())
s14 = "Thank you for the music\nWelcome to the jungle"
print("34.   ",s14.splitlines())
print("35.   ",s14.startswith("Thank"))
print("Hey", s11.strip(), "welcome")
print("36.   ",s2.swapcase())
print("37.   ",s2.title())
s15 = "This is my Set"
y = {83: 80}
print(s15.translate(y))
print("38.   ",s15.upper())
print("39.   ",s7.zfill(15))