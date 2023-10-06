import random
a = random.randrange(1,12)
s = ""

for x in range(1, 2 * a, 2):
  s = s + str(x) + ", "

print(s.removesuffix(", "))

s = ""

for x in range(x, x + 3 * a, 3):
  s = s + str(x) + ", "

print(s.removesuffix(", "))

#s = ""
#step = 3
#for x in range(x, x + step * a, step):
  #s = s + str(x) + ", "

#print(s.removesuffix(", "))

# initiate $a as random INT (integer) from 1 to 11
# with the help of FOR loop, create a concatinated string starting from 1, 
# ", " as glue, with $a numbers, with step 2 (i.e. 1, 3, ..) 

# with the help of another FOR loop, create another concatinated string 
# which starts with the number at the end of the first string, glue ", ", 
# with $a numbers, with step 3 (i.e. 21, 24, ..)