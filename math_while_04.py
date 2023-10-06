import random

a = random.randrange(1, 12)
a = 3
x = a + a
i = 1
s = ""

while i <= x:
  s = s + str(i) + ", "
  i += 2

print(s.removesuffix(", "))

s = ""
z = i - 2
y = x + a - 2

while z <= y:
  s = s + str(z) + ", "
  z += 1
  
print(s.removesuffix(", "))

# initiate $a as random INT (integer) from 1 to 11
# with the help of WHILE loop, create a concatinated string starting from 1, 
# ", " as glue, with $a numbers, with step 2 (i.e. 1, 3, ..) 

# with the help of another WHILE loop, create another concatinated string 
# which starts with the number at the end of the first string, glue ", ", 
# with $a numbers, step 1