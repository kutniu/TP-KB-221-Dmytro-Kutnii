list = [
    {"name": "Bob", "phone": "543785412", "email": "bad@email", "address": "tyrtyuihjgfg4"},
    {"name": "Emma", "phone": "54302154", "email": "good@email", "address": "45uiyuo"},
    {"name": "Jon", "phone": "865431235", "email": "wow@email", "address": "3w31qqawsa"},
    {"name": "Zak", "phone": "453452244", "email": "some@email", "address": "dgwefsdf"}
]

def printAllList():
    sorted_students = sorted(list, key=lambda x: x["name"])  
    for student in sorted_students:
        strForPrint = f"Student name is {student['name']}, Phone is {student['phone']}, Email is {student['email']}, Address is {student['address']}"
        print(strForPrint)

def addNewElement():
    name = input("Pease enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    address = input("Please enter student address: ")
    newItem = {"name": name, "phone": phone, "email": email, "address": address}
    # find insert position
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for student in list:
        if name == student["name"]:
            deletePosition = list.index(student)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        del list[deletePosition]
        print("Element has been deleted")


def updateElement():
    name = input("Please enter name to be updated: ")
    for index, student in enumerate(list):
        if name == student["name"]:
            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            newElement = {"name": new_name, "phone": new_phone, "email": new_email, "address": new_address}

            del list[index]
            insertPos = 0
            for pos, elem in enumerate(list):
                if new_name > elem["name"]:
                    insertPos = pos + 1
                else:
                    break
            list.insert(insertPos, newElement)
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
