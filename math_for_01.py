import random
a = random.randrange(1,21)
s = ""

for x in range(1, a + 1):
  s = s + str(x) + ", "

print(s.removesuffix(", "))

s = ""

for x in range(a + 1, 2 * a + 1):
  s = s + str(x) + ", "

print(s.removesuffix(", "))

# initiate $a as random INT (integer) from 1 to 20
# with the help of FOR loop, create a concatinated string 1, 2,.. $a
# print this string at the end of the loop

# with the help of another FOR loop, create a concatinated string $a+1, $a+2,.. with the same $a numbers as the first string
# while still inside this loop, print a loop counter at every run of the loop
# print this string at the end of the loop