import os
from sys import argv
import csv

if len(argv) == 1:
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    os.chdir(script_dir)
    filename = os.path.join(script_dir, 'lab2.csv')
else:
    filename = argv[1]

def load_filename(filename):
    list = []
    with open(filename) as file:
        reader = csv.DictReader(file)

        for row in reader:
            lowercased_row = {key.lower(): value for key, value in row.items()}
            list.append(lowercased_row)
    params = tuple(list[0].keys()) if list else ('name', 'phone')

    return list, params


def get_new_params(param_tuple) -> dict:
    new_params = {}
    for param in param_tuple:
        new_params[param] = input(f'Please enter student {param}: ')
    return new_params


def print_all_list(param_tuple, students_list):
    print("#" * 10 + '  All list  ' + '#' * 10)
    for elem in students_list:
        print('Student : ', end='')
        for param in param_tuple:
            str_for_print = f"{param} is " + f"{elem[param]}"
            print(str_for_print, end=', ')
        print('\n')
    print("#" * 20)


def add_new_element(students_list, param_tuple):
    new_item = get_new_params(param_tuple)
    insert_position = 0
    for item in students_list:
        if new_item['name'] > item["name"]:
            insert_position += 1
        else:
            break
    students_list.insert(insert_position, new_item)
    print("New element has been added")


def delete_element(students_list):
    name = input("Please enter name to be deleted: ")
    delete_position = next((i for i, item in enumerate(students_list) if item["name"] == name), -1)
    if delete_position == -1:
        print("Element was not found")
    else:
        del students_list[delete_position]
        print("Element has been deleted")


def update_element(students_list, param_tuple):
    name = input("Please enter name to be updated: ")
    update_position = next((i for i, item in enumerate(students_list) if item["name"] == name), -1)
    if update_position == -1:
        print("Element was not found")
    else:
        print('Enter new params:')
        new_params = get_new_params(param_tuple)
        if new_params['name'] == students_list[update_position]['name']:
            students_list[update_position] = new_params
        else:
            del students_list[update_position]
            insert_position = 0
            for item in students_list:
                if new_params['name'] > item["name"]:
                    insert_position += 1
                else:
                    break
            students_list.insert(insert_position, new_params)
        print('Element has been updated')


def main(students_list, param_tuple):
    while True:
        choice = input("Please specify the action [C create, U update, D delete, P print, X exit]: ")
        match choice.lower():
            case "c":
                print("New element will be created:")
                add_new_element(students_list, param_tuple)
                print_all_list(param_tuple=param_tuple, students_list=students_list)
            case "u":
                print("Existing element will be updated")
                update_element(students_list=students_list, param_tuple=param_tuple)
                print_all_list(param_tuple=param_tuple, students_list=students_list)
            case "d":
                print("Element will be deleted")
                delete_element(students_list)
                print_all_list(param_tuple=param_tuple, students_list=students_list)
            case "p":
                print("List will be printed")
                print_all_list(param_tuple=param_tuple, students_list=students_list)
            case "x":
                print("Exiting the program")
                break
            case _:
                print("Wrong choice")


def save_all_list(students_list, params, path):
    with open(path, "w", newline='') as csvfile:
        fieldnames = params
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in students_list:
            writer.writerow(item)
    print('All list saved!')


if __name__ == '__main__':
    if len(argv) == 1:
        filename = 'lab2.csv'
    else:
        filename = argv[1]

    student_list, parameters = load_filename(filename)
    main(student_list, parameters)
    save_all_list(student_list, parameters, "lab2_out.csv")
