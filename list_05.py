import random
lst = []
lst2 = []
lst3 = []
lst4 = []

for a in range (1,21):
  b = random.randrange(1,13)
  lst.append(b)
  lst2.append(b)
print(lst)
print()

for x in lst:
  z = 0
  for y in lst:
    if x == y:
      z += 1
  if z == 1:
    lst2.remove(x)

for v in range (1,21):
  z = v
  for u in lst2:
    if u == z:
      lst3.append(z)

print(lst3)
print()
z = 0

for w in lst3:
  #if w > z:
  if w not in lst4:
    lst4.append(w)
    #z = w

print(lst4)

# generate the list of random numbers, range from 1 to 21
# remove all the unique members from this list, print out the new list without those numbers
# form another list from this list of duplicates, where every duplicate number shows only once
# i.e. if the initial list lst = [ 1, 2, 2, 3, 4, 3 ]
# then lst1 = [ 2, 2, 3, 3, ] and lst2 =[ 2, 3, ]