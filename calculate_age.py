from datetime import date


d1 = date(1999,9,29)
d2 = date(2022,5,20)

total_days = d2 - d1
d = total_days.days
print("Total days = ",d)

if d >= 365:
    y = int(d/365)
    temp = int(d%365)
    month = int(temp/30)
    days = int(temp%30)
    print("Year = ", y, "Month = ",month, "days = ",days)

elif d <= 365:
    month = int(d/30)
    days = int(d%30)
    print("Year = 0", "Month = ",month, "days = ",days)