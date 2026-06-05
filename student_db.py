class student:
    def __init__(self , name , id , year , major , blood_group):
        self.name = name
        self.id = id
        self.year = year
        self.major = major
        self.blood_group = blood_group

    def __str__(self):
        return f"Student Name: {self.name}  \nStudent ID: {self.id}  \nYear: {self.year}  \nMajor: {self.major} \nBlood: {self.blood_group}"

        
            
student1 = student("Manish" , 1000001 , "Fouth Year" , "Computer Science" , "A+")
student2 = student("Rohan" , 1000002 , "Third Year" , "Information Technology" , "AB+")
student3 = student("Vijay" , 1000003 , "First Year" , "Mechanical Engineering" , "o+")
student4 = student("Andy" , 1000004 , "Second Year" , "Electrical Engineering" , "B+")
student5 = student("Sara" , 1000005 , "Fouth Year" , "Mechanical Engineering" , "O-")
student6 = student("Jimmy" , 1000006 , "Second Year" , "Bio Technology" , "A+")
student7 = student("Nicola" , 1000007 , "Third Year" , "Literature" , "B+")
                        
students = [student1, student2, student3, student4, student5, student6, student7]

while True:
    search_id = input("Enter Student ID (or type 'exit' to quit): ")
    if search_id == "exit":
        break
    try:
        search_id = int(search_id)
        for ides in students:
            if search_id == ides.id:
                print(ides)
                break
        else:
            print("Student not found")
    except ValueError:
        print("Student not found")
        
            
  