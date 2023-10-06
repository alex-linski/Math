import random
import math

a = random.randrange(2,23)
i = 1
s = ""
total_sum = 0

while i <= 200:
  total_sum += i 
  #print("step " + str(i) + ": " + str(total_sum) )
  i += 1
#print("Total Sum = ",total_sum)

i = 1
factorial = 1

while i <= a:
  #factorial = math.factorial(i)
  factorial *= i
  print(i,": ",factorial)
  i += 1
print(a,"factorial = ",factorial)

  
  
# part 1
# write a while loop that adds all numbers from 1 up to 100 (inclusive)
# inside the loop, print $i (counter) and current $total_sum (i.e. 'step 6: 21')
# print $total_sum at the end of the loop

# part 2
# generate INT $a between 2 and 22
# write a while loop that multiplies all numbers from 1 up to $a (inclusive)
# inside the loop, print $i (counter) and current $factorial (i.e. '4: 24')
# print $factorial at the end of the loop