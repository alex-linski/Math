import random
lst = []
z = 0
for a in range (1,21):
  b = random.randrange(1,11)
  lst.append(b)

print(lst)
print()
print()
dict = {}

for x in lst:
  y = x
  i = 0
  for s in lst:
    if s == y:
      i += 1
  dict[z] = i
  z += 1

print(dict)
      
        

# generate a list $lst, containing 20 members, each member a random INT, from 1 to 10; 
# print this list 
# create a dictionary $dict, of the length of $lst, where index memebers correspond to indexes of $lst, and values are the number of times $lst member is found in $lst (number of it's duplicates) 
# i.e., if $lst = [ 1, 2, 2, 3, ], 
# then $dict = { 0: 1, 1: 2, 2: 2, 3: 1, }