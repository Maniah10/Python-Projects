class phonebook():
    # What's in the Phonebook
    def __init__ (self, name, contact_number):
        self.name = name
        self.contact_number = contact_number


    # Structure of the phonebook
    def __str__(self):
        return (f"Name:{self.name},Contact Number:{self.contact_number}")
    

# Reading the txt file
f = open("Phonebook.txt" , "r")
lines = f.readlines()
f.close()

# Empty list loaded with the data from the file
contacts = []
for line in lines:
    part = line.strip().split(",")
    p = phonebook(part[0], part[1])
    contacts.append(p)

while True:
    a = input("---Main Menu---\n1. Add contact \n2. Search by name\n3. Delete contact\n4. Display all contacts\n5. Exit \n: ")
    try:
        a = int(a)
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 5.")

    # If someone press 1
    if a == 1:
        # New Name 
        b = input("Enter the name: ")
        n = b.title()

        # New Number
        while True:
            c = input("Enter contact number: ")
            if len(c) == 10:
                pass
            elif len(c) != 10:
                print("Invalid number")
                continue
            else:
                print("Invalid number")
                continue
            try:
                c = int(c)
                break
            except ValueError:
                print("Enter only numbers!")

        f = open("Phonebook.txt" , "a")
        f.write(f"{n},{c}\n")
        f.close()
        
        new_contact = phonebook(n,c)
        contacts.append(new_contact)
        print("Contact added successfully!")


    # If someone press 2
    if a == 2:
        d = input("Enter the name: ")
        k = d.title()
        for contact in contacts:
            if k == contact.name:
                print(contact)    
                break
        else:
            print("Contact not found!")


    # If someone press 3
    if a == 3:
        e = input("Enter the contact number: ")
        try:
            e = int(e)
        except:
            print("Invalid number! Enter number only")
        
        # Seaarching for conntact in the list
        for contact in contacts:
            if e == int(contact.contact_number):
                print(contact)
                while True:
                    g = input("Confirm delete this contact? (y/n): ").lower()
                    if g == "y":
                        contacts.remove(contact) 
                        f = open("Phonebook.txt" , "w")
                        for each in contacts:
                            f.write(f"{each.name},{each.contact_number}\n")
                        f.close()
                        print("Contact deleted!")
                        break
                    elif g == "n":
                        break
                    else:
                        print("Enter y or n!")
                break        
        else:
            print("Contact not found!")


    # If someone press 4
    if a == 4:
        for contact in contacts:
            print(contact)
        
    # If someone press 5
    if a == 5:
        h = input("Do you want to exit (y/n): ").lower()
        if h == "y":
            break
        elif h == "n":
            continue
        else:
            print("Enter y/n only!")
    







    
