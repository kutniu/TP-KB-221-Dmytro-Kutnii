import os
from functions import *
from operations import *

log_file_path = r"D:\Документи\Універ\3 семестр\Технології програмування\TP-KB-221-Dmytro-Kutnii\topic_06\task1\calculator_log.txt"


if not os.path.isfile(log_file_path):
    with open(log_file_path, "w") as log_file:
        log_file.write("Calculator Log:\n")

print("Виберіть операцію:")
print("1. Додавання")
print("2. Віднімання")
print("3. Множення")
print("4. Ділення")

choice = input("Ваш вибір (1/2/3/4): ")

if choice == "1":
    perform_addition(log_file_path)
elif choice == "2":
    perform_subtraction(log_file_path)
elif choice == "3":
    perform_multiplication(log_file_path)
elif choice == "4":
    perform_division(log_file_path)
else:
    print("Неправильний вибір операції")
