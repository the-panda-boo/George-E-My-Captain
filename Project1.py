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
def ext():
    print("Waiting")
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
    if(choice != "1" and choice != "2"):
        print("Really!!!..... It's a Simple Choice between 1 and 2.... Lets try that again.\n Remember.... It's easy Just 1 or 2.")
    