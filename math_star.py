a = 7
s = ""
z = 0

for x in range(1, 2 * a + 2):
  if z == 0:
    print("¯\_(ツ)_/¯")
  
  if x >= a + 1:
    z = z - 2
  
  z = z + 1
  
  for y in range(1, z + 1):
    s = s + "* "  
  
  if s:
    print(s)
  s = ""
  


# Write a code to print the following pattern using the for loop:
# ¯\_(ツ)_/¯
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * * 
# *
# ¯\_(ツ)_/¯