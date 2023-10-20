import random
a = random.randrange(4,10)
b = random.randrange(2,6)

print("a = ",a)
print("b = ",b)
print()

lst = [1,3,5,7,9,11,13,15,17,19]
print(lst)

z = lst[0]
y = lst[-1]

lst[-1] = z
lst[0] = y
print(lst)

s = ""
for x in lst:
  s = s + str(x) + ", "
print(s.removesuffix(", "))
print()

w = 0
v = 1
c = ""
for y in range (1,a+1):
  for x in lst:
    w = x * b * v
    c = c + str(w) + ", "
  
  print(c.removesuffix(", "))
  c = ""
  v = v * b

# you are given a list lst = [1,3,5,7,9,11,13,15,17,19]
# initiate $a as random INT from 4 to 10; print it, as 'a = $a'
# initiate $b as random INT from 2 to 5; print it, as 'b = $b'

# swap first and last members of the list
# print a lines of numbers, first row is list members multiplied by b each
#(divided by ', ', no comma in the end) 
# every next line is a result of multiplication of a  
# respective number from the previous row