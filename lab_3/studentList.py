from student import Student


        
class StudentList:
    def __init__(self):
        self.students_list = []

    def add_student(self, student):
        
        insert_position = 0
        for item in self.students_list:
            if student.name > item.name:
                insert_position += 1
            else:
                break
        self.students_list.insert(insert_position, student)

    def delete_student(self, name):
        delete_position = -1
        for item in self.students_list:
            if name == item.name:
                delete_position = self.students_list.index(item)
                break
        if delete_position != -1:
            del self.students_list[delete_position]

    def update_student(self, updated_student):
        update_position = -1
        for item in self.students_list:
            if updated_student.name == item.name:
                update_position = self.students_list.index(item)
                break

        if update_position != -1:
            del self.students_list[update_position]
            self.add_student(updated_student)

    def print_all_students(self):
        print("#" * 10 + '  All list  ' + '#' * 10)
        for student in self.students_list:
            print(f'Student: name is {student.name}, phone is {student.phone}')
        print("#" * 20)
