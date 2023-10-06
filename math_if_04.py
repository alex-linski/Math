import random

#print(12%5)
#print(12%6)
#print(12%7)
#print(12%8)
# a % b = remainder of a/b

a = random.randrange(1, 51)
primefactor = 0

if a % 2 == 0:
  print(a,"is prime") if a == 2 else print(a,"is divisible by 2")
  primefactor = 1
 
#if a % 3 == 0:
if not a % 3:
  print(a,"is prime") if a == 3 else print(a,"is divisible by 3")
  primefactor = 1

if a % 5 == 0:
  print(a,"is prime") if a == 5 else print(a,"is divisible by 5")
  primefactor = 1
  
if a % 7 == 0:
  print(a,"is prime") if a == 7 else print(a,"is divisible by 7")
  primefactor = 1

if a % 11 == 0:
  print(a,"is prime") if a == 11 else print(a,"is divisible by 11")
  primefactor = 1

if a % 13 == 0:
   print(a,"is prime") if a == 13 else print(a,"is divisible by 13")
   primefactor = 1

if primefactor == 0:
  print(a,"is prime")

# try to Run the following: print(12%5); print(12%6); print(12%7); print(12%8); 
# guess what is the meaning of operator '%'  
# initiate $a as random INT (integer) from 1 to 50 
# check if $a id divisible by: 2,3,5,7,,11,13
# print eaach time '$a is divisible by' INT above if it is true 
# after all checks, print '$a is not divisible by 2,3,5,7,,11 or 13' if you have found that it is NOT divisible to anything