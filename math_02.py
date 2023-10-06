import random
"""
a = 1
b = 1
if a > b: 
  print("Small:",b,)
  print("Big:",a)
elif a == b:
  print ("a equals b:",b)
else:
  print ("Small:",a,)
  print ("Big:",b)
"""
a = random.randrange(1, 11)
b = random.randrange(1, 11) 
print ("Random a =",a)
print ("Random b =",b)
if a > b: 
  print("Small:",b,)
  print("Big:",a)
elif a == b:
  print ("a equals b:",b)
else:
  print ("Small:",a,)
  print ("Big:",b)

# initialize 'a' as a number from 1 to 10
# initialize 'b' as a number from 1 to 10
# if $a is bigger than 'b' - print 'small: $a' then 'big: $b'
# if $b is bigger than 'a' - print 'small: $b' then 'big: $a'
# if $a equals $b - print 'a equals b: $a'
# 
# now, find the way how, in PYTHON, to randomly generate number from 
# 1 to 10
# generate random number twice and initialize a and b with it
# print 'random a = ' + $a
# print 'random b = ' + $b
# and implement IF structure written above to this $a and $b