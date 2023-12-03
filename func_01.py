def rate_name(name):
  if name.lower() == "alex":
    print(name + " is a premium student! Brilliant with Python, and stuff!")
  elif name.lower() == "daniel":
    print("Honestly, "+ name + " is playing too much on his phone. He should spent more time on Python programming.B")
  else:
    print(name + " who? We don't know him. Next!") 

for x in range(0,3):
  name = input("Enter the name of the student >")
  print()
  rate_name(name)
  

    
# write a function that takes a name you receive as an input and prints out the following 
# phrases:
# if the lowercase parameter is "alex": "$name is a premium student! Brilliant with Python, and stuff!"
# if the lowercase parameter is "daniel": "Honestly, $name is playing too much on his phone. He should spent more time on Python programming"
# in case of all other names: "$name who? We don't know him. Next!"
# in the loop of 3 iterations, offer to input a name, and then call the function with this name
# use name = input("Enter the name of the student >") for an input