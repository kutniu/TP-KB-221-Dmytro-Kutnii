from functions import *
from operations import *

print("Виберіть операцію:")
print("1. Додавання")
print("2. Віднімання")
print("3. Множення")
print("4. Ділення")

choice = input("Ваш вибір (1/2/3/4): ")

if choice == "1":
    perform_addition()
elif choice == "2":
    perform_subtraction()
elif choice == "3":
    perform_multiplication()
elif choice == "4":
    perform_division()
else:
    print("Неправильний вибір операції")
