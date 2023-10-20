from collections import Counter
import random
lst = []
for a in range (1,21):
  b = random.randrange(1,11)
  lst.append(b)

print(lst)
print()
dict = {}
cnt = Counter(lst)
print(cnt)
print()
z = 0

for x in lst:
  dict[z] = cnt[x]
  z += 1


print(dict)
      
# generate a list $lst, containing 20 members, each member a random INT, from 1 to 10; 
# print this list 
# create a dictionary $dict, of the length of $lst, where index memebers correspond to indexes of $lst,
# and values are the number of times $lst member is found in $lst (number of it's duplicates)
# do that WITHOUT using 2 FOR nested loops, using Counter() function 
# from "collections" library instead (read what this function is for)