class student:
    def __init__ (self,name,enrollment_number,stream,major,blood_group):
        self.name = name
        self.enrollment_number = enrollment_number
        self.stream = stream
        self.major = major
        self.blood_group = blood_group

    def __str__ (self):
        return (f"Name: {self.name} \nEnrollment Number: {self.enrollment_number} \nStream: {self.stream} \nMajor: {self.major} \nBlood Group: {self.blood_group}")
    

students = []

f = open("Student_List.txt", "r")
lines = f.readlines()
f.close()

for line in lines:
    parts = line.strip().split(",")
    s = student(parts[0], int(parts[1]), parts[2], parts[3], parts[4])
    students.append(s)
                

def search(search_id):
    for ideas in students:
        if search_id == ideas.enrollment_number:
            print(ideas)
            break
    else:
        print("Student Not Found")

while True:
    a = input("1. Search student \n2. Add student \n3. Remove Student \n4. Print all Students  \n5. Exit  \n:")
    try:
        a = int(a)
    except ValueError:
        print("Enter number for 1 to 3")
        continue
    if a == 1:
        search_id = input("Enter Enrollment Number: ")
        if search_id == "exit":
            break
        else:
            try:
                search_id = int(search_id)
                search(search_id)
            except ValueError:
                print("Invalid Error")
                continue
    if a == 2:
        while True:
            name = input("Enter The Name: ")
            n = name.title()
            enrollment = input("Enter Enrollment number: ")
            try:
                enrollment = int(enrollment)
                e = int(enrollment)
            except ValueError:
                print("Invalid Input")
                continue
            stream = input("Enter Stream: ")
            s = stream.title()
            major = input("Enter subject Major: ")
            m = major.title()
            blood = input("Enter Blood Group: ")
            b = blood.capitalize()

            f = open("Student_List.txt" , "a")
            f.write(f"{n},{e},{s},{m},{b}\n")
            f.close()
            new_student = student(n, e, s, m, b)  
            students.append(new_student)  
            break

    if a == 3:
        while True:
            g = input("1. Delete \n2. Edit \n:")
            try:
                g = int(g)
                break
            except ValueError:
                print("Enter eithr 1 or 2")
                continue

        if g == 1:
            d = input("Enter Enrollment Number: ")
            try:
                d = int(d)
                id = int(d)
            except ValueError:
                print("Invalid Input")

            for student in students:
                if student.enrollment_number == id:
                    p = input("Are you sure you want to delete? (y/n): ").lower()
                    if p == 'y':
                        students.remove(student)
                        f = open("Student_List.txt", "w")
                        for s in students:
                            f.write(f"{s.name},{s.enrollment_number},{s.stream},{s.major},{s.blood_group}\n")
                        f.close()
                        print("Student deleted successfully!")
                        break
                    else:
                        break

            else:
                student.enrollment_number != id
                print("Student Not Found")
                continue



        if g == 2:
                l = input("Enter Enrollment number: ")
                try:
                    l = int(l)
                except ValueError:
                    print("Enter Valid Number")
                    continue
                    

                for student in students:
                    if student.enrollment_number == l:
                        i = input("----Chose the field----\n1. Name\n2. Enrollment Number\n3. Stream\n4. Major\n5. Blood Group\n: ")
                        try:
                            i = int(i)
                        except ValueError:
                            print("Invalid Input")
                            break
                        
                        if i == 1:
                            student.name = input("Enter new name: ").title()
                        elif i == 2:
                            student.enrollment_number = int(input("Enter new enrollment number: "))
                        elif i == 3:
                            student.stream = input("Enter new stream: ").title()
                        elif i == 4:
                            student.major = input("Enter new major: ").title()
                        elif i == 5:
                            student.blood_group = input("Enter new blood group: ").upper()
                        
                        f = open("Student_List.txt", "w")
                        for s in students:
                            f.write(f"{s.name},{s.enrollment_number},{s.stream},{s.major},{s.blood_group}\n")
                        f.close()
                        print("Updated successfully!")
                        break
                else:
                    print("Student Not Found")
                    

    if a == 4:
          for s in students:
            print(s)

    if a == 5:
        break
        


            

    


