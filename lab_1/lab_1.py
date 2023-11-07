students = [
    {"name": "vlad", "phone": "543785412", "email": "bad@email", "address": "tyrtyuihjgfg4"},
    {"name": "djenya", "phone": "54302154", "email": "good@email", "address": "45uiyuo"},
    {"name": "elif", "phone": "865431235", "email": "wow@email", "address": "3w31qqawsa"},
    {"name": "vanya", "phone": "453452244", "email": "some@email", "address": "dgwefsdf"}
]

def printAllList():
    sorted_students = sorted(students, key=lambda x: x["name"])  
    for student in sorted_students:
        strForPrint = f"Student name is {student['name']}, Phone is {student['phone']}, Email is {student['email']}, Address is {student['address']}"
        print(strForPrint)

def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    address = input("Please enter student address: ")
    new_student = {"name": name, "phone": phone, "email": email, "address": address}
    students.append(new_student)
    students.sort(key=lambda x: x['name']) 
    print("New student has been added")

def deleteElement():
    name = input("Please enter name to be deleted: ")
    for student in students:
        if name == student["name"]:
            students.remove(student)
            print(f"{name} has been deleted")
            return
    print("Student not found")

def updateElement():
    name = input("Please enter name to be updated: ")
    for index, student in enumerate(students):
        if name == student["name"]:
            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            newElement = {"name": new_name, "phone": new_phone, "email": new_email, "address": new_address}

            del students[index]
            insertPos = 0
            for pos, elem in enumerate(students):
                if new_name > elem["name"]:
                    insertPos = pos + 1
                else:
                    break
            students.insert(insertPos, newElement)
            print("Element has been updated")
            break
    else:
        print("Student not found")


def main():
    while True:
        choice = input("Please specify the action [C create, U update, D delete, P print, X exit]: ")
        if choice.lower() == "c":
            print("New student will be created:")
            addNewElement()
            printAllList()
        elif choice.lower() == "u":
            print("Existing student will be updated")
            updateElement()
            printAllList()
        elif choice.lower() == "d":
            print("Student will be deleted")
            deleteElement()
            printAllList()
        elif choice.lower() == "p":
            print("List will be printed")
            printAllList()
        elif choice.lower() == "x":
            print("Exiting the program")
            break
        else:
            print("Wrong choice")

main()
