import random
lst = []
lst2 = []
lst3 = []

for a in range (1,21):
  b = random.randrange(1,16)
  lst.append(b)
  lst2.append(b)

print(lst)
print()

for x in lst:
  z = 0
  for y in lst2:
    if x == y:
      z += 1
  if z > 1:
    lst2.remove(x)

print(lst2)
print()
lst3 = lst2.copy()

for x in lst3:
  for y in range (12,16):
    if x == y:
      lst3.remove(x)
      
print(lst3)
print()

import calendar
months = calendar.month_name[1:]

dict = {}
dict1 = {}

for x in lst3:
  dict[x] = months[x -1]

print(dict)
print()

days = calendar.day_name[0:]

for x in lst3:
  if x < 8:
    dict1[x] = days[x -1]
  else:
    dict1[x] = ""

print(dict1)
# generate a list $lst, containing 20 members, each member a random INT, from 0 to 15; print it
# remove all duplicates from this list
# remove all list members bigger than 11
# create a list $months of month names, by using "calendar" library, here is how:
'''
from calendar import month_name
months = month_name[1:]
'''
# note that this is a different format of using import; previously we were using import function this way:
'''
import calendar
months = calendar.month_name[1:]
'''
# print $months list; try both ways of using import functionality
# print $months list; try both ways of using import functionality
# try to use calendar.month_name[0:] instead of calendar.month_name[1:], see the difference

# create a dictionary $dict, where indexes are numbers from $lst
# and dictionary members are corresponding month names from $months list; print it

# create list of weekdays, as 
'''
days = calendar.day_name[0:]
'''
# create a dictionary $dict1, where indexes are numbers from $lst and 
# dictionary members are respective weekday names from $days list - if they exist;
# if index is too big, dictionary member should be "-"
# print $dict1