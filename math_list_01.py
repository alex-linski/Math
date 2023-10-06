import random
a = random.randrange(3,10)
b = 0
s = ""
c = ""

lst = [1,2,3,4,5,6,7,8,9,10,]

print("Total list members = ",len(lst))
print("a = ",a)

for x in lst:
  b = x * a
  s = s + str(x) + ", "
  c = c + str(b) + ", "

print(s.removesuffix(", "))
print(c.removesuffix(", "))




# you are given a list lst = [1,2,3,4,5,6,7,8,9,10,]
# calculate and print the LENGTH of this list
# initiate $a as random INT from 3 to 9; print it, as 'a = $a'
# print 2 lines of numbers, first row is list members 
#(divided by ', ', no comma in the end) 
# second line is a result of multiplication of a respective list number 
# and $a - i.e. if $a = 2, second line will be like 2, 4, 6, ...