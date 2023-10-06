import random

a = random.randrange(1, 101)
b = random.randrange(1, 101)
if a < 26:
  cat_a = 1
elif a < 51:
  cat_a = 2
elif a < 76:
  cat_a = 3
elif a < 101:
  cat_a = 4
else:
  cat_a = 5

print("a =",a,"category",cat_a)

if b < 26:
  cat_b = 1
elif b < 51:
  cat_b = 2
elif b < 76:
  cat_b = 3
elif b < 101:
  cat_b = 4
else:
  cat_b = 5

print("b =",b,"category",cat_b)

if cat_a == cat_b:
   print("a and b are both in category",cat_a)
else:
  print("a and b are in different categories,",cat_a,"and",cat_b)

# generate 2 random numbers, a and b, from 1 to 100, and initialize $a and $b with it
# find out in which range both variables land: 
# if it is < 26 - category 1; 
# if it's > 25 but less than < 51  - category 2 
# if it's > 50 but less than < 76  - category 3 
# if it's > 75 but less than < 101 - category 4 
# print 'a = ' + $a + ' - category $x'
# print 'b = ' + $b + ' - category $y'
# if a and b are in the same category - print "a and b are in the same category $x"
# if not - print "a and b are in different categories, $x and $y"