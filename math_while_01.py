import random

a = random.randrange(1, 11)
i = 1
s = ""

while i <=a:
  s = s + str(i) + ", "
  i += 1

print(s.removesuffix(", "))
# initiate $a as random INT (integer) from 1 to 10
# with the help of WHILE loop, create a concatinated string 1, 2,.. $a
# print this string at the end of the loop