import os
from operations import Operations

class Calculator(Operations):
    def __init__(self):
        super().__init__()
        self.log_file_name = "calculator_log.txt"
        self.current_directory = os.path.dirname(os.path.abspath(__file__))
        self.log_file_path = os.path.join(self.current_directory, self.log_file_name)

        if not os.path.isfile(self.log_file_path):
            with open(self.log_file_path, "w") as log_file:
                log_file.write("Calculator Log:\n")

    def run(self):
        print("Виберіть операцію:")
        print("1. Додавання")
        print("2. Віднімання")
        print("3. Множення")
        print("4. Ділення")

        choice = input("Ваш вибір (1/2/3/4): ")

        if choice == "1":
            self.perform_addition(self.log_file_path)
        elif choice == "2":
            self.perform_subtraction(self.log_file_path)
        elif choice == "3":
            self.perform_multiplication(self.log_file_path)
        elif choice == "4":
            self.perform_division(self.log_file_path)
        else:
            print("Неправильний вибір операції")

calculator = Calculator()
calculator.run()
