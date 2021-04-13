from math import pi
print("The following is the Project on Data Structures for My Captain.\n")
def question():
    print("Choose one of the following.\n\n   1. Area of a Circle from it's radius.\n   2. Extention from a file name.")
    global choice
    choice = input("\nEnter your choice (1/2) : ")
def math():
    print("Program to calculate area of a circle from the radius.")
    global rad
    rad = float(input("Input the radius of the circle : "))
    print ("The area of the circle with radius "+str(rad)+" is: "+str(pi*rad**2) )
question()
check = "2"
while (check == "2"):
    question()
    if (choice == "1"):
        math()
        check = "1"
    if(choice == "2"):
        ext()
        check = "1"