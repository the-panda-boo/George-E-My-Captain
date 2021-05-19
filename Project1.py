from math import pi
print("The following is the Project on Data Structures for My Captain.\n")
def question():
    print("Choose one of the following.\n\n   1. Area of a Circle from it's radius.\n   2. Extention from a file name.")
    global choice
    choice = input("\nEnter your choice (1/2) : ")
def math():
    print("\n\nProgram to calculate area of a circle from the radius.")
    global rad
    rad = float(input("\nInput the radius of the circle : "))
    print ("The area of the circle with radius "+str(rad)+" is : "+str(pi*rad**2)+"\n\n")
def ext():
    global name
    global ex
    name = input("\n\nEnter Filename: ")
    ex = name.split(".")
    print ("Extension of the file is : " + ex[-1]+"\n\n")  
question()
check = "2"
while (check == "2"):
    if (choice == "1"):
        math()
        again = input("\nWould you like to find the area of another circle?\nY/N : ")
        while (again == "y" or again == "Y"):
            math()
            again = input("\nWould you like to find the area of another circle?\nY/N : ")
        check = "1"
    if(choice == "2"):
        ext()
        again = input("\nWould you like to find the extention of another file?\nY/N : ")
        while (again == "y" or again == "Y"):
            ext()
            again = input("\nWould you like to find the extention of another file?\nY/N : ")
        check = "1"
    if(choice != "1" and choice != "2"):
        print("\n\nReally!!!..... \nIt's not that hard....\nIt's a Simple Choice between 1 and 2.... Lets try that again.\n Remember.... It's easy Just 1 or 2.\n")
        question()
    if(check == "1"):
        restart = input("\n\nWould you like to try the other program?\nY/N : ")
        if(restart == "Y"or restart == "y"):
            check = "2"
            if(choice == "1"):
                choice = "2"
            else:
                choice = "1"
print("\n\n\nThank you!!\n\n")#123hahahehe
