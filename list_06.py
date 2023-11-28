import random
print("list_06 starts here")
print()
a = random.randrange(5,16)
print("a = ",a)
print()
lst = []
lst2 = []
x = 0
randomwasted = 0

while x < a: # len(lst) < a
  b = random.randrange(0,a)
  if b not in lst:
    lst.append(b)
    x += 1
  else:
    randomwasted += 1

print(lst)
print()
print("random wasted = ",randomwasted)

# generate random int $a from 5 to 15; print it
# create list of unique integers $lst, from 0 to $a - 1, the size of $a 
# (i.e. if $a = 5, list should be 5 members and consist of 0,1,2,3 and 4)
# fill the list with .append() function with random numbers, check if integer is unique 
# if not unique, count it as "random wasted" operation, and generate integer again 
# print $lst every time you add a member to it
# print resulting $lst in the end
# print the final counter for "random wasted" operations