s = str(input("Enter email address:- \n"))
s = s.strip().lower()
if not "@" in s:
    print("Invalid email \n")
elif not (".com" or ".gov" or ".org" or ".net" or ".edu") in s[-4:]:
    print("Invalid email \n")
else:
    print("Email address is valid")