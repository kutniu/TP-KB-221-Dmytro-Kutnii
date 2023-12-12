import csv
from student import Student
from studentList import StudentList

class FileManager:
    def load_data(file_name):
            list = StudentList()
            with open(file_name) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = Student(row["name"], row["phone"])
                    list.students_list.append(student)
            return list

    def save_data(file_name, list):
        fieldnames = ["name", "phone"]
        with open(file_name, "w", newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for student in list.students_list:
                writer.writerow({"name": student.name, "phone": student.phone})