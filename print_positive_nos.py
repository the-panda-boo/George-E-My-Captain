# Enter number of elements with Instruction
n = int(input("Enter number of elements : "))
 
# Instructions
print("Enter the elements below, use space and press enter only after inputing all the elements.")
# Below line read inputs from user using map() function 
a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]

#for loop calculating each element and creating element
positive = []
for num in list(a):
    if (num>0): 
        positive.append(num)
print(len(positive))
if (len(positive) == 0):
    print("All the elements you've entered are negative.")
else:
    print("The positive elements are:", positive)