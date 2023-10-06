import random

a = random.randrange(1, 21)
i = 1
s = ""

while i <= a:
  s = s + str(i) + ( "" if i == a else ", " )
  i += 1

#print(s.removesuffix(", "))
print(s)

i = 2
s = ""
x = a + 1

while i <= x:
  i += 1
  a += 1
  s = s + str(a) + ", "
  
print(s.removesuffix(", "))

# initiate $a as random INT (integer) from 1 to 20
# with the help of WHILE loop, create a concatinated string 1, 2,.. $a
# print this string at the end of the loop
# with the help of another WHILE loop, create a concatinated string $a+1, $a+2,.. with the same $a numbers as the first string
# while still inside this loop, print a loop counter at every run of the loop
# print this string at the end of the loop