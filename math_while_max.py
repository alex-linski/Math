import random

a = random.randrange(1, 21)
i = 1
s = ""

while i <= a:
  s = s + str(i) + ", "
  i += 1

print(s.removesuffix(", "))

s = ""
x = a + a

while i <= x:
  s = s + str(i) + ", "
  i += 1
  
print(s.removesuffix(", "))
###################################

a = random.randrange(1, 12)
x = a + a
i = 1
s = ""

while i <= x:
  s = s + str(i) + ", "
  if (i>=x -1):
    break
  else:
    i += 2

print(s.removesuffix(", "))

s = ""
y = x + a - 2

while i <= y:
  s = s + str(i) + ", "
  i += 1
  
print(s.removesuffix(", "))
