import random
lst = []
lst2 = []
z = 0
print()
for a in range (1,21):
  b = random.randrange(1,11)
  lst.append(b)
  lst2.append(b)
 
    
print(lst)
print()

for x in lst:
  y = x
  i = 0
  for s in lst2:
    if s == y:
      i += 1
      if i > 1:
        lst2.remove(y)
        z += 1
      
print(lst2)
print()
print("# of duplicates = ",z)

# generate a list, containing 20 members, each member a random INT, from 1 to 10; 
# print this list 
# find and remove duplicates from the list; print the new list
# print the number of found duplicates