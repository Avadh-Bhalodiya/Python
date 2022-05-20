#   DATE & TIME
from datetime import datetime
a = datetime.now()
print("\n",a)
print(a.year)
print()

b = datetime(1999,9,29)
print(b)
print()


print(a.strftime("%%"))     # print %

print(a.strftime("%A"))     # day name
print(a.strftime("%a"))

print(a.strftime("%B"))     # month name
print(a.strftime("%b"))

print(a.strftime("%C"))     # current Cntury
print(a.strftime("%c"))     # local version of date

print(a.strftime("%d"))     # day

print(a.strftime("%f"))     # micro-second

print(a.strftime("%G"))     # ISO 8601 year

print(a.strftime("%H"))     # hour  0-24
print(a.strftime("%I"))     # hour 0-12

print(a.strftime("%j"))     # day number 1-366

print(a.strftime("%m"))     # month as number
print(a.strftime("%M"))     # minute

print(a.strftime("%p"))     # am , pm

print(a.strftime("%S"))     # seconds

print(a.strftime("%u"))     # ISO 8601 weekday 0-7
print(a.strftime("%U"))     # week number 0 -53     Sunday as the first day of week, 00-53

print(a.strftime("%V"))     # ISO 8601 weeknumber 1-53

print(a.strftime("%w"))     # day of week
print(a.strftime("%W"))     # week number   0 - 53      Monday as the first day of week, 00-53

print(a.strftime("%X"))     # local version of time
print(a.strftime("%x"))     # local version of date

print(a.strftime("%Y"))     # year  full
print(a.strftime("%y"))     #       half

print(a.strftime("%Z"))     # Timezone
print(a.strftime("%z"))     # UTC offset