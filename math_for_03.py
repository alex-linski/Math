import random
a = random.randrange(1,16)
a = 6
s = ""

for x in range(1, a * a + 1):
  s = s + str(x) + ", "
  if x % a == 0: 
    print(s.removesuffix(", "))
    s = ""

print("")
s = ""
z = 1

for x in range(1, a + 1):
  for y in range(z, z + a):
    s = s + str(y) + ", "  
  print(s.removesuffix(", "))
  s = ""
  z = z + a
  
  
# initiate $a as random INT (integer) from 1 to 15
# with the help of 2 (two) FOR loops, print $a number of concatinated strings, 
# first starts with 1, 2,.. $a, step=1, the second starts with $a+1, $a+2, .., the step=1
# each string should contain $a numbers
# to sum up: $a rows of strings, $a numbers in each, glue ', ', step=1 for all rows