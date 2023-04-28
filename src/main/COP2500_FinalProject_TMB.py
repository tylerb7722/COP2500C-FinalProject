# Tyler Boudreau
# 04/14/2023
# Final Project
# COP 2500C

# This Programs purpose is to add and calculate students final grades and stores them in a database,
# allowing you to see the list of all students names and both their letter and numerical grades,
# as well as add or remove students as needed from the database.

    # Displays main menu and options awaiting user input.
def Main_Menu():
    print("Which option would you like to do?")
    print("1. Calculate new students final grade.\n2. Remove a students final grade.\n3. List all students final grades.\n4. Exit\n")

    # Exits the program with goodbye message.
def exit():
    print("Goodbye!\n")

def option1(): # Option 1: Calculates new students final grade.
    SName = str(input("Please enter the name of the student you wish to add.\n"))
    grades_list.append(SName)
    GradelistCalc = [] # initialize empty list
    total = 0 # initialize value
    Grades = 0 # initialize value
    while(Grades != "done"):
        try:
            Grades = input("Please enter the students grades one at a time. When done type 'done'\n")
            if (Grades == "Done"):
                Grades = "done"
            if (Grades != "done"):
                Grades = int(Grades)
                GradelistCalc.append(Grades)
        except ValueError: # Prevents ValueError for invalid input
            print("Invalid Input, try again!\n")
    length = len(GradelistCalc)
    for i in range(length):
        total = total + GradelistCalc[i]
    average = float("{:.2f}".format(total/length)) #Calculates final grade average and rounds to two decimal places.
    grades_list.append(average)
    #Calculates the corresponding letter grade with +'s and -'s for all letter grades except A, C, and F.
    if(average>=93):
        grades_list.append("A")
    elif(average>=90):
        grades_list.append("A-")
    elif(average>=87):
        grades_list.append("B+")
    elif(average>=83):
        grades_list.append("B")
    elif(average>=80):
        grades_list.append("B-")
    elif(average>=77):
        grades_list.append("C+")
    elif(average>=70):
        grades_list.append("C")
    elif(average>=67):
        grades_list.append("D+")
    elif(average>=63):
        grades_list.append("D")
    elif(average>=60):
        grades_list.append("D-")
    else:
        grades_list.append("F")
    print("Student and Grade successfully added!\n")
    Action = 0 # Resets Action value

def option2(): # Option 2: Removes a students final grade.
    Remove = str(input("Which Student would you like to remove?\n"))
    try:
        RIndex = grades_list.index(Remove)
        grades_list.pop(RIndex+2)
        grades_list.pop(RIndex+1)
        grades_list.pop(RIndex)
        print("Student has been removed.\n")
        Action = 0 # Resets Action value
    except ValueError: # Prevents ValueError for invalid input
        print("Student not found, try again.\n") #Prints error message if student is not found in database
    Action = 0 # Resets Action value

def option3(): # Option 3: Lists all students final grades.
    LLength = len(grades_list)
    length = len(grades_list)/3
    length = int(length)
    if(LLength>0):
        Index = 0
        for i in range(length):
            print("Name:",grades_list[Index]," - Grade:",grades_list[Index+1],"-",grades_list[Index+2])
            Index +=3
    else:
        print("No Students currently added!\n") #Prints error message if no students are currently in the databse.
    Action = 0 # Resets Action value


    # Main function executes the program and calls other functions as needed,
    # and returns to main menu once done with selected option. 
def main():
    print("Welcome to the UCF Grade Calculation Tool!\n")
    print("This tool will calculate the Students final grade by taking the average of the grades entered, weighing them equally.\n")
    Main_Menu()
    Action = int(input())
    #Runs program until user enters choice 4 to exit the program
    while(Action != 4):
        #Runs code for Action 1 which is adding a student and final grade to the databse.
        if(Action == 1):
            option1()
        # Runs code for Action 2, which removes the desired student from the database if that student was already entered previously.
        if(Action == 2):
            option2()
        # Runs code for Action 3, whcih prints all the students and their final grades currently in the database.
        if(Action == 3):
            option3()  
        Main_Menu()
        Action = int(input())
    exit()


if __name__ == "__main__":
    grades_list = [] # Initializes with empty list
    main()

