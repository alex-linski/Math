
# below you are given 2 dictionaries, with info about 2 students
# generate another dictionary with the same structure, with info about both students in it
# use .update() function for the merge
# print the resulting dictionary

# print info about students marks by year
# format: 
# 2000: Joe Smuth - English: 1, Math: 1, Physics: 1 
#       Smoe Juth - English: 2, Math: 2, Physics: 2 
# 3000: Joe Smuth - English: 3, Math: 3, Physics: 3 
#       Smoe Juth - English: 4, Math: 4, Physics: 4

from pprint import pprint
dict1 = {
        "student": {
          "Alex Linski": {
            "marks": { 
              2022: {               
                "Math": 92,
                "English": 85,
                "Science": 95,
                "Music": 37,
              },
              2023: {              
                "Math": 100,
                "English": 80,
                "Science": 100,
                "Music": 25,
              }                 
            }
          }
        }  
}
dict2 = {
        "student": {
          "Daniel Linski": {
            "marks": {
              2022: {              
                "Math": 100,
                "English": 80,
                "Science": 38,
                "Music": 77,
              },
              2023: {
                "Math": 95,
                "English": 88,
                "Science": 70,
                "Music": 67,
              }                  
            }
          }
        }  
}

dict1["student"].update(dict2["student"])
pprint(dict1)
print("")

a_marks = dict1["student"]["Alex Linski"]["marks"][2023]
print("Alex Linski marks for 2023:")
print(dict1["student"]["Alex Linski"]["marks"][2023])
print("")

s = ""
for k, v in dict1["student"].items():
  
  for k1, v1 in v["marks"].items():
    s += str(k1) + ": " + str(k) + " - "
    
    for k2, v2 in v1.items():
      s += str(k2) + ": " + str(v2) + ", "
    
    print(s)
    s = ""

# 2000: Joe Smuth - English: 1, Math: 1, Physics: 1