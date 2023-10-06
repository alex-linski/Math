import random
a = random.randrange(10,17)
b = random.randrange(1,21)
print("a = ",a)
print()
lst = []

for x in range (1, a + 1):
  lst.append(b)
  b = random.randrange(1,20)
    
print(lst)

lst_max = 1
lst_min = 20

for z in lst:
  if z > lst_max:
    lst_max = z
  if z < lst_min:
    lst_min = z

print()
print("lst_max = ",lst_max)
print()
print("lst_min = ",lst_min)
  
# generate a random INT $a, from 10 to 16
# print it as 'a = $a'
# generate a list, containing $a members, each member a random INT, from 1 to 20; print it
# find the biggest member of this list, $lst_max; print ii as 'lst_max = $lst_max'
# find the smallest member of this list, $lst_min; print ii as 'lst_min = $lst_min' 