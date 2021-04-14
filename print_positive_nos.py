test_string = "There are 25 apples for 44 persons 56, 6"
  
# printing original string 
print("The original string : " + test_string)
  
# using List comprehension + isdigit() +split()
# getting numbers from string 
res = [int(i) for i in test_string.split() if i.isdigit()]
  
# print result
print("The numbers list is : " + str(res))