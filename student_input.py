while True:
    name = input("Enter the name of the student: ")
    name = name.capitalize()
    id = input("Enter the ID of the student: ")
    try:
        id = int(id)
    except ValueError:
        print("Invalid ID number")
        continue

    year = input("Enter the current studding year of the student: ")
    year = year.title()
    major = input("Enter the name of the major of the student: ")
    major = major.title()
    while True:
        blood = input("Enter blood group of the student: ").upper()
        if blood == "A+" or blood == "B+" or blood == "AB+" or blood == "O+":
            break
        elif blood == "A-" or blood == "B-" or blood == "AB-" or blood == "O-":
            break
        else:
            print("Invalid Input")
    
    a = open("Student_Database.txt" , "a")
    a.write(f"Students Name: {name} \nStudents ID: {id} \nCurrent Year: {year} \nSubject Major: {major} \nBlood Group: {blood}\n")
    a.close ()

    question = input("Do you want to continue(y/n): ").lower()
    if question == "n":
        break
    elif question == "y":
        continue
    else:
        print("Only Y or N")


