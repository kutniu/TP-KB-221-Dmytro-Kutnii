import os

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def save_to_file(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as file:
        for item in data:
            file.write(f"Ім'я: {item.name}, Вік: {item.age}\n")

students = [
    Student("Аліса", 20),
    Student("Боб", 22),
    Student("Віктор", 19),
    Student("Григорій", 21)
]

sort_choice = input("Бажаєте сортувати за 'алфавітом' чи 'віком'? ")

if sort_choice == 'алфавітом':
    name_order = input("Сортувати 'за алфавітом' чи 'проти алфавіту'? ")
    if name_order == 'за алфавітом':
        students = sorted(students, key=lambda x: x.name)
    elif name_order == 'проти алфавіту':
        students = sorted(students, key=lambda x: x.name, reverse=True)
else:
    age_order = input("Сортувати 'за зростанням' віку чи 'за спаданням'? ")
    if age_order == 'за зростанням':
        students = sorted(students, key=lambda x: x.age)
    elif age_order == 'за спаданням':
        students = sorted(students, key=lambda x: x.age, reverse=True)

for student in students:
    print(f"Ім'я: {student.name}, Вік: {student.age}")

current_directory = os.path.dirname(os.path.abspath(__file__))
file_name = input(f"Введіть назву файлу для збереження у теку {current_directory}: ") + ".txt"
file_path = os.path.join(current_directory, file_name)

if os.path.exists(file_path):
    print(f"Файл з іменем {file_name} вже існує. Будь ласка, виберіть інше ім'я файлу.")
    
else:
    save_to_file(file_path, students)
    print(f"Файл {file_name} успішно збережено.")
