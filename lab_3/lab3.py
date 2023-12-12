import sys
from sys import argv
from file_manager import FileManager
from file_manager import Student


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_name.csv>")
        sys.exit(1)
        
    file_name = sys.argv[1]
    list = FileManager.load_data(file_name)

    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                name = input("Enter name: ")
                phone = input("Enter phone number: ")
                new_student = Student(name, phone)
                list.add_student(new_student)
                list.print_all_students()
            case "U" | "u":
                print("Existing element will be updated:")
                name = input("Enter students name: ")
                phone = input("Enter new phone number: ")
                updated_student = Student(name, phone)
                list.update_student(updated_student)
                list.print_all_students()
            case "D" | "d":
                print("Element will be deleted")
                name = input("Enter students name: ")
                list.delete_student(name)
            case "P" | "p":
                print("List will be printed")
                list.print_all_students()
            case "X" | "x":
                print("Exit")
                FileManager.save_data(file_name, list)
                break
            case _:
                print("Wrong chouse")


if __name__ == "__main__":
    main()